from config.llm import ask_llm

def generate_report(vulnerabilities, exploit):

    prompt = f"""
Generate a professional smart contract security audit report.

Vulnerabilities:
{vulnerabilities}

Exploit analysis:
{exploit}

Structure:

1. Summary
2. Vulnerabilities
3. Exploit scenario
4. Recommended fixes
"""

    return ask_llm(prompt)