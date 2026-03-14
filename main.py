from tools.file_loader import load_contract
from tools.slither_runner import run_slither
from agents.audit_agent import AuditAgent
from agents.exploit_generator_agent import ExploitGenerator
from agents.report_agent import ReportAgent


def main():

    contract_path = "contracts/vulnerable.sol"

    print("Loading contract...")
    contract_code = load_contract(contract_path)

    print("Running static analysis...")
    vulnerabilities = run_slither(contract_path)

    print("Auditing contract...")
    audit_agent = AuditAgent()
    audit_results = audit_agent.analyze(contract_code, vulnerabilities)

    print("Generating exploit...")
    exploit_agent = ExploitGenerator()

    exploits = []

    for vuln in vulnerabilities:
        exploit = exploit_agent.generate_exploit(contract_code, vuln["description"])
        # print(exploit)
        exploits.append(exploit)

    print("Generating report...")
    report_agent = ReportAgent()

    report = report_agent.generate_report(vulnerabilities)

    print(report)


if __name__ == "__main__":
    main()
