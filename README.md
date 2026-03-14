# BlockGuard-AI 🛡️

**Autonomous AI Smart Contract Security Auditor**

BlockGuard-AI is an AI-powered system that analyzes Solidity smart contracts for security vulnerabilities using a combination of **static analysis tools and Large Language Models (LLMs)**.

The system performs automated security reviews by integrating **Slither static analysis** with **Gemini AI reasoning** to detect vulnerabilities, generate exploit scenarios, and produce professional security audit reports.

---

## 🚀 Features

* 🔍 **Static Analysis** using Slither
* 🤖 **AI-powered vulnerability reasoning** using Gemini
* 📄 **Automated security audit reports**
* ⚠️ Detection of common smart contract vulnerabilities:

  * Reentrancy
  * Integer overflow / underflow
  * Access control flaws
  * Unsafe external calls
  * Gas inefficiencies
* 🧠 **Exploit scenario generation**

---

## 🏗️ Project Architecture

```
Smart Contract
      │
      ▼
Static Analysis (Slither)
      │
      ▼
AI Audit Agent
      │
      ▼
Exploit Analysis Agent
      │
      ▼
Security Report Generator
```

---

## 📂 Project Structure

```
contract_reviewer/
│
├── agents/
│   ├── audit_agent.py
│   ├── exploit_agent.py
│   └── report_agent.py
│
├── config/
│   └── llm.py
│
├── contracts/
│   └── vulnerable.sol
│
├── tools/
│   ├── file_loader.py
│   └── slither_runner.py
│
├── main.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Avverma250106/BlockGuard-AI.git
cd BlockGuard-AI
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install Solidity compiler

```bash
pip install solc-select
solc-select install 0.8.20
solc-select use 0.8.20
```

---

### 4️⃣ Install Slither

```bash
pip install slither-analyzer
```

---

### 5️⃣ Add your Gemini API key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

Run the auditor:

```bash
python main.py
```

Example output:

```
Loading contract...
Running static analysis...
Auditing contract...
Generating exploit idea...
Generating report...

======= SECURITY REPORT =======
```

The system will produce a full **security audit report** including detected vulnerabilities and exploit explanations.

---

## 🧪 Example Vulnerability Detected

The example contract included demonstrates a **Reentrancy vulnerability** caused by calling an external address before updating the contract state.

Example vulnerable pattern:

```solidity
(bool success,) = msg.sender.call{value: amount}("");
balances[msg.sender] -= amount;
```

Recommended fix:

Follow the **Checks-Effects-Interactions pattern**.

---

## 🔮 Future Improvements

* Automatic **exploit contract generation**
* **Hardhat attack simulation**
* **Web interface for uploading contracts**
* **Security scoring system**
* **Multi-agent orchestration**

---

## 🛠️ Tech Stack

* Python
* Gemini API
* Slither
* Solidity
* Static analysis + LLM reasoning

---

## ⚠️ Disclaimer

This tool is intended for **educational and research purposes only**.
It should not be relied upon as a complete security audit for production smart contracts.

---

## 📜 License

MIT License
