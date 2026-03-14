from config.llm import ask_llm

def audit_contract(contract_code, slither_output):

    prompt = f"""
You are a blockchain smart contract security expert.

Analyze the Solidity contract and detect vulnerabilities.

Common vulnerabilities:
- reentrancy
- integer overflow
- access control issues
- front running
- gas inefficiencies

Smart Contract Code:
{contract_code}

Static Analysis Result:
{slither_output}

List vulnerabilities with severity and explanation.
"""

    result = ask_llm(prompt)

    return result