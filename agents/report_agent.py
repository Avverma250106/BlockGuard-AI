from agents.scoring_agent import RiskScorer
from tools.swc_mapper import map_to_swc


class ReportAgent:

    def __init__(self):
        self.scorer = RiskScorer()

    def generate_report(self, vulnerabilities):

        vuln_list = [v["description"] for v in vulnerabilities]

        score, counts = self.scorer.compute_score(vuln_list)

        report = "\n====== SECURITY REPORT ======\n\n"

        report += f"Security Score: {score}/100\n\n"

        report += "Severity Distribution:\n"

        for k, v in counts.items():
            report += f"{k.upper()}: {v}\n"

        report += "\nDetected Vulnerabilities:\n"

        unique = {}

        # collect unique issues
        for vuln in vulnerabilities:
            swc = map_to_swc(vuln["description"])

            if swc not in unique:
                unique[swc] = vuln

        # print only unique ones
        for swc, vuln in unique.items():

            report += f"""
---------------------------------
Issue: {self.simplify_issue(vuln["description"])}
Line: {vuln["line"]}
SWC: {swc}
---------------------------------
"""

        return report
    
    def simplify_issue(self, description):
        if "reentrancy" in description.lower():
            return "Reentrancy vulnerability"
        if "low level call" in description.lower():
            return "Unsafe low level call"
        if "version constraint" in description.lower():
            return "Compiler version risk"

        return description.split("\n")[0]

