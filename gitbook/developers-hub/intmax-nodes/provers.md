# Provers

### What is Provers?

In the Intmax network, user balances are verified using Zero-Knowledge Proofs (ZKPs) to ensure sufficient funds and validate withdrawal conditions.

This document describes nodes responsible for generating various ZKPs used in Intmax.

### **Balance Prover**

This server allows users to create cryptographic proofs of their account balances. Requests to the server are encrypted, and the data is only decrypted and processed within secure, confidential storage. As a result, even the server administrator cannot view users' balances or transaction histories.

### **Validity Prover**

This server generates proofs confirming the correctness of the state of the Intmax blockchain.

### **Aggregator Prover**

This server aggregates withdrawal (claim) requests from users into a single withdrawal (claim) proof. It is capable of aggregating multiple requests from different users into one unified proof.

### **Gnark Prover**

This server converts aggregated withdrawal (claim) proofs into Solidity-verifiable proofs. The Withdrawal Aggregator submits aggregated proofs to the Gnark Prover, receives back a Solidity-verifiable proof, and submits this proof directly to the smart contract.
