#!/usr/bin/env python3
"""Docusaurus → GitBook 変換スクリプト

処理内容:
1. ファイルコピー（user-guides, developers-hub, community, 画像）
2. _category_.json 削除
3. .mdx → .md リネーム
4. front matter 除去
5. Docusaurus import 削除（コードブロック保護付き）
6. 画像パス置換（/img/ → assets/）+ <figure><img> → Markdown画像記法
7. <Tabs>/<TabItem> → {% tabs %}/{% tab %} 変換
"""

import os
import re
import shutil
import sys


def remove_front_matter(content):
    """YAML front matter を除去"""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:].lstrip("\n")
    return content


def remove_docusaurus_imports(content):
    """コードブロック外の import 文を削除"""
    lines = content.split("\n")
    result = []
    in_code_block = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        if in_code_block:
            result.append(line)
            continue
        if re.match(r'^import\s+.*from\s+["\']@theme/', line):
            continue
        if re.match(r'^import\s+Tabs\s', line):
            continue
        if re.match(r'^import\s+TabItem\s', line):
            continue
        result.append(line)
    return "\n".join(result)


def convert_image_paths(content):
    """画像パスを /img/ → assets/ に変換"""
    content = re.sub(
        r'<figure>\s*<img\s+src="(/img/[^"]+)"\s*alt="([^"]*)"\s*/?\s*>\s*</figure>',
        lambda m: '![{}](assets/{})'.format(m.group(2), m.group(1).lstrip("/img/")),
        content,
    )
    content = content.replace("(/img/", "(assets/")
    content = content.replace('="/img/', '="assets/')
    return content


def convert_tabs(content):
    """Docusaurus <Tabs>/<TabItem> → GitBook {% tabs %}/{% tab %} に変換"""
    content = re.sub(r'<Tabs>', '{% tabs %}', content)
    content = re.sub(r'</Tabs>', '{% endtabs %}', content)

    def tab_item_replace(m):
        label = m.group(2) if m.group(2) else m.group(1)
        return '{{% tab title="{}" %}}'.format(label)

    content = re.sub(
        r'<TabItem\s+value="([^"]+)"(?:\s+label="([^"]+)")?[^>]*>',
        tab_item_replace,
        content,
    )
    content = re.sub(r'</TabItem>', '{% endtab %}', content)
    return content


def process_file(filepath):
    """単一の .md ファイルを変換"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    content = remove_front_matter(content)
    content = remove_docusaurus_imports(content)
    content = convert_image_paths(content)
    content = convert_tabs(content)
    content = content.lstrip("\n")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def convert(src_root, dest_root):
    """原文リポジトリから gitbook/ に変換コピーする"""
    gitbook_dir = os.path.join(dest_root, "gitbook")

    # 1. ファイルコピー
    for subdir in ["user-guides", "developers-hub"]:
        src = os.path.join(src_root, subdir)
        dst = os.path.join(gitbook_dir, subdir)
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print("  ok {}/ copied".format(subdir))

    community_src = os.path.join(src_root, "src", "pages", "community.mdx")
    community_dst = os.path.join(gitbook_dir, "community.md")
    if os.path.exists(community_src):
        shutil.copy2(community_src, community_dst)
        print("  ok community.md copied")

    src_img = os.path.join(src_root, "static", "img")
    dst_assets = os.path.join(gitbook_dir, "assets")
    if os.path.exists(dst_assets):
        shutil.rmtree(dst_assets)
    shutil.copytree(src_img, dst_assets)
    img_count = sum(1 for _, _, files in os.walk(dst_assets) for _ in files)
    print("  ok assets/ copied ({} files)".format(img_count))

    # 2. _category_.json 削除
    cat_count = 0
    for root, dirs, files in os.walk(gitbook_dir):
        for f in files:
            if f == "_category_.json":
                os.remove(os.path.join(root, f))
                cat_count += 1
    print("  ok _category_.json removed ({})".format(cat_count))

    # 3. .mdx → .md リネーム
    mdx_count = 0
    for root, dirs, files in os.walk(gitbook_dir):
        for f in files:
            if f.endswith(".mdx"):
                old_path = os.path.join(root, f)
                new_path = os.path.join(root, f[:-4] + ".md")
                os.rename(old_path, new_path)
                mdx_count += 1
    print("  ok .mdx -> .md renamed ({})".format(mdx_count))

    # 4-7. 各 .md ファイルを変換
    md_count = 0
    for root, dirs, files in os.walk(gitbook_dir):
        for f in files:
            if f.endswith(".md"):
                filepath = os.path.join(root, f)
                if filepath == os.path.join(gitbook_dir, "README.md"):
                    continue
                if filepath == os.path.join(gitbook_dir, "SUMMARY.md"):
                    continue
                process_file(filepath)
                md_count += 1
    print("  ok markdown converted ({} files)".format(md_count))

    # 検証
    print("\n--- verify ---")
    verify(gitbook_dir)


def verify(gitbook_dir):
    """変換結果を検証"""
    issues = []
    for root, dirs, files in os.walk(gitbook_dir):
        for f in files:
            if not f.endswith(".md"):
                continue
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8") as fh:
                content = fh.read()
            rel = os.path.relpath(filepath, gitbook_dir)
            if "import Tabs" in content or "import TabItem" in content:
                issues.append("  warn {}: Docusaurus import remains".format(rel))
            if "<Tabs>" in content or "<TabItem" in content:
                issues.append("  warn {}: <Tabs>/<TabItem> remains".format(rel))
            if "(/img/" in content or '="/img/' in content:
                issues.append("  warn {}: /img/ path remains".format(rel))
            if content.startswith("---"):
                issues.append("  warn {}: front matter may remain".format(rel))
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("  ok no issues found")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 convert.py <source-docs-repo-path>")
        sys.exit(1)
    src = sys.argv[1]
    dest = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("convert: {} -> {}/gitbook/\n".format(src, dest))
    convert(src, dest)
    print("\ndone.")
