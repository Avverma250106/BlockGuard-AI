from tools.file_loader import load_contract
from tools.slither_runner import run_slither

from agents.audit_agent import audit_contract
from agents.exploit_agent import generate_exploit
from agents.report_agent import generate_report


def main():

    contract_path = "contracts/vulnerable.sol"

    print("Loading contract...")
    contract_code = load_contract(contract_path)

    print("Running static analysis...")
    slither_output = run_slither(contract_path)

    print("Auditing contract...")
    vulnerabilities = audit_contract(contract_code, slither_output)

    print("Generating exploit idea...")
    exploit = generate_exploit(contract_code, vulnerabilities)

    print("Generating report...")
    report = generate_report(vulnerabilities, exploit)

    print("\n======= SECURITY REPORT =======\n")
    print(report)


if __name__ == "__main__":
    main()