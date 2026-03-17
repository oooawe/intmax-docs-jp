# Vibe Coding for Coding Prompt

## Boost Your Productivity with These AI Tools

Using an AI pair-programmer will **dramatically speed you up** during the hackathon.

We **highly recommend**:

- **Cursor**
- **Cline**
- **GitHub Copilot (VS Code)**
- **Gemini CLI**
- **Claude Code**
- **Replit**
- **v0**

Best-performing models:

- **GPT-5**
- **Gemini 2.5 Pro**
- **Claude Sonnet 4**

💡 _Tip: Paste the Copilot Starter Template below into your assistant to scaffold quickly._

## 🚀 Starter Template Prompt

**Title:** Vite + TypeScript starter using `intmax2-client-sdk`
(wallet connect & INTMAX2 balance; env switch: testnet/mainnet)

**Context:**
Build a minimal web dApp starter for the VibeCoding Contest. Use **`intmax2-client-sdk`** to:

1. Connect a wallet
2. Fetch & display INTMAX2 balance

**Tech Stack (must-follow):**

- Vite + React + TypeScript
- SDK: `intmax2-client-sdk`
- Clean modular `/src` structure
- `.env` for env vars (never hardcode secrets)
- Minimal UI (headless or lightweight CSS ok)

**Environment Switching:**

- `VITE_INTMAX_ENV = 'testnet' | 'mainnet'` (default: **testnet**)
- On startup: validate required vars for active env → error if missing

---

### 📝 MVP Requirements

1. **Wallet Connect**
   - Detect `window.ethereum`
   - Connect wallet → show shortened address
2. **Balance Fetch**
   - “Refresh Balance” button
   - Show INTMAX2 balance
3. **UX Basics**
   - Loading states
   - Inline/toast error messages
4. **Type Safety**
   - No `any` types
5. **README**
   - Steps for running on **testnet** (default)
   - Switching to mainnet explained clearly
   - Explicit MetaMask requirement

---

### 📂 Project Skeleton

```
vite.config.ts
src/
  lib/
    env.ts         # Reads VITE_INTMAX_ENV & validates config
    sdk.ts         # Initializes SDK; exposes connectWallet/getBalance
  components/
    WalletConnect.tsx
    BalancePanel.tsx
  App.tsx
.env.local.example  # with testnet defaults + mainnet block
README.md
```

---

### ⚙️ Example `.env.local.example`

```
# Select environment: testnet (default) or mainnet
VITE_INTMAX_ENV=testnet
```

---

### 📖 README Must Include

**Prereqs:** Node.js (LTS), MetaMask (or EIP-1193 wallet)

**Run on Testnet (default):**

```bash
cp .env.local.example .env.local
npm i
npm run dev
```

**Switch to Mainnet:**

```bash
# edit .env.local
VITE_INTMAX_ENV=mainnet
# fill mainnet values
npm run dev
```

## 🚀 How to Use (Scaffold)

1. Open the app in a browser **with MetaMask installed** _(if no wallet is detected, see Troubleshooting below)_
2. Click **Connect Wallet** → approve the request in MetaMask
3. Click **Refresh Balance** → your current INTMAX2 balance will appear

✅ **Validation:** If you see your wallet address and a balance, your setup is complete.

## 🔜 What’s Next?

Now that your scaffold works, here are suggested next steps:

- **Basic Extension** → Implement a “Deposit” button enabling token deposits to the INTMAX Network
- **UI Upgrade** → Show a list of past balances or transactions.
- **AI Integration** → Connect with an AI API (OpenAI, Claude, Gemini) to trigger payments automatically.
- **Creativity** → Extend the scaffold into your hackathon idea (e.g. P2P payments, games, agents).

👉 This scaffold is only the **starting point**.

Your goal is to **build on top of it and showcase something unique** during the hackathon!

## 🛠 Troubleshooting (Quick Guide)

| Problem (What you see)                                        | Cause / Symptom                       | Solution                                                             |
| ------------------------------------------------------------- | ------------------------------------- | -------------------------------------------------------------------- |
| ❌ **No wallet found** _"Connect Wallet" button does nothing_ | Browser has no injected provider      | ✅ Install MetaMask (or any EIP-1193 wallet) and refresh the page    |
| ❌ **Missing env vars** _App crashes on startup_              | `.env.local` not set or incomplete    | ✅ Copy `.env.local.example` → `.env.local` and fill required values |
| ❌ **Wrong chain** _Wallet shows “unsupported network”_       | Wallet is connected to a different L1 | ✅ Switch wallet network to the required L1 chain (testnet/mainnet)  |
| ❌ **RPC unreachable** _Balance shows “0/unavailable”_        | RPC endpoint is down or blocked       | ✅ Retry after a few seconds, or check DevTools console for errors   |

## Common / Useful Prompts

### **Debugging Prompt**

```
Here is my current code for the INTMAX agent.
It should send a payment, but fails.

1. Review for bugs or missing steps
2. Improve error handling & readability
3. Make it demo-ready
```

### **Optimization Prompt**

```
I have a working INTMAX agent prototype.

1. Reduce unnecessary calls
2. Improve UX flow
3. Suggest enhancements to impress judges
```

### **Integration Prompt (Add AI or External API)**

```
I want to integrate an AI API (OpenAI, Claude, Gemini).

1. Show how to connect external AI in TypeScript
2. Example: AI makes a decision → triggers INTMAX payment
3. Keep demo-ready and simple
```
