# Other Features

## Withdraw rest amount

When mining is completed, a small amount of ETH (roughly equivalent to the gas fee) may remain in the address.
This can occur especially if the withdrawal was executed when Ethereum gas fees were high.
Below is an explanation of the procedure to withdraw this remaining ETH.

1. If there is more ETH remaining than the gas fee in the address used for mining, a "Withdraw Rest Amount" button will be displayed.
   If you wish to withdraw this amount, please click the "Withdraw Rest Amount" button.

![Withdraw Rest Amount](assets/user-guides/other_features_10.webp)

2. The withdrawal destination address can only be the same as the one used previously.
You cannot choose a different address freely.

![Withdraw Rest Amount](assets/user-guides/other_features_20.webp)

3. Review the transaction details and click the "Confirm" button.

![Withdraw Rest Amount](assets/user-guides/other_features_30.webp)

4. Wait until the status changes to "Sync Withdrawals".

![Withdraw Rest Amount](assets/user-guides/other_features_40.webp)

5. Once the status is "Completed," you can safely leave the screen.

![Withdraw Rest Amount](assets/user-guides/other_features_50.webp)

**NOTE**: If you close the screen during the process, please start over from the beginning of the procedure.

## Cancel Mining

You can cancel a mining session even before the lock period has matured. However, please note that if you cancel, **no rewards will be granted**, and only the deposited ETH will be returned.

1. First, click the **"Cancel Mining Session"** button.

2. A confirmation dialog will then appear, warning you that if the lock period has not yet ended, you may lose the chance to receive rewards.
By selecting **"Yes, Proceed"**, the cancellation process will continue, and you will be redirected to the withdrawal screen.

<figure>
  <img src="assets/user-guides/cancel_mining_10.webp" alt="Cancel Mining" />
  <img src="assets/user-guides/cancel_mining_20.webp" alt="Cancel Mining" />
</figure>

3. Here, you can enter the destination Ethereum address and click the **"Cancel + Withdrawal"** button to withdraw the deposited ETH.

![Cancel Mining](assets/user-guides/cancel_mining_30.webp)

## Resuming an Interrupted Claim

Usually, in a mining session that is ready for claiming, you can claim your rewards by clicking the “Withdraw” or “Redeposit” button and following the on-screen instructions.
However, this process may be interrupted if, for example, you close the browser before it is completed.

If you open the details page of such a mining session, a “Claim Rewards” button and a warning message will be displayed.
You can resume the interrupted process by clicking the “Claim Rewards” button.

![Claim Rewards](assets/user-guides/claim-rewards_10.webp)

The button display will change and attempt to execute the claim process.

![Claim Rewards](assets/user-guides/claim-rewards_20.webp)

If the claim fee payment has not been made, a "Top Up for Claim Fee" button will be displayed. Click the button.

![Claim Rewards](assets/user-guides/claim-rewards_30.webp)

A modal like the one below may appear, but click the “Next” button.

![Claim Rewards](assets/user-guides/claim-rewards_40.webp)

Click the "Yes, Proceed" button.

![Claim Rewards](assets/user-guides/claim-rewards_50.webp)

Review the transfer details and click the Send button.

Your connected wallet will request a signature.

![Claim Rewards](assets/user-guides/claim-rewards_60.webp)

Once the signature is complete, you will see the transfer waiting screen.

![Claim Rewards](assets/user-guides/claim-rewards_70.webp)

When the transfer request is complete, the status will change. Clicking the "Go to Active Mining" button will return you to the mining session details screen.

![Claim Rewards](assets/user-guides/claim-rewards_80.webp)

The "Claim Rewards" button will be unclickable for approximately 5 minutes.

Once the gas fee top-up is complete, the "Claim Rewards" button will become clickable again. Click the button.

![Claim Rewards](assets/user-guides/claim-rewards_10.webp)

When the "Claim Rewards" button is no longer displayed, the ITX token reward claim is complete.

If the "Top Up for Claim Fee" button appears again at this point, wait about 10 minutes and then check the mining session again.

![Claim Rewards](assets/user-guides/claim-rewards_90.webp)

## Withdraw ETH to a Contract Address

We would like to provide a clear explanation the procedure for withdrawing ETH to a contract address in mining.

### :warning: **Important Notice**

When specifying a withdrawal destination address, please make sure that it is **your own address**.
In particular, specifying a **contract address** or an **exchange address** as the withdrawal destination is **not covered by our support**, and we do not take any responsibility in such cases.
If you choose to send ETH to a contract address, please carefully confirm that the contract is able to **receive ETH deposits**.

### 1. Purpose

The purpose of this function is to enable the transfer of ETH that has entered a “withdrawable state” — for example, when attempting to withdraw to a contract address — so that it can actually be sent to the specified address.

**NOTE**: In contrast, when sending to a regular address (EOA), the ETH is delivered directly to the address.

### 2. When the Button Appears

- The button will be displayed when your destination account has a withdrawable ETH balance.
- If you have pending withdrawals, the button will trigger a claim process.

![Withdraw ETH](assets/user-guides/withdraw_eth_to_contract_10.webp)

### 3. How the Withdrawal Works

- When you click the button, you will be asked to **sign a transaction with your connected wallet**.
- This operation makes your funds available on Ethereum.

![Withdraw ETH](assets/user-guides/withdraw_eth_to_contract_20.webp)
