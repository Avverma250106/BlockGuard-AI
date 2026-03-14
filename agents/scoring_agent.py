class RiskScorer:
    def __init__(self):
        self.weights = {
            "critical": 40,
            "high": 25,
            "medium": 10,
            "low": 5,
            "info": 1
        }

    def classify_severity(self, vulnerability):
        vuln = vulnerability.lower()

        if "reentrancy" in vuln:
            return "critical"
        elif "access control" in vuln:
            return "high"
        elif "overflow" in vuln:
            return "high"
        elif "gas" in vuln:
            return "low"
        else:
            return "medium"

    def compute_score(self, vulnerabilities):

        severity_count = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0
        }

        for vuln in vulnerabilities:
            severity = self.classify_severity(vuln)
            severity_count[severity] += 1

        score = 100

        for sev, count in severity_count.items():
            score -= self.weights[sev] * count

        score = max(score, 0)

        return score, severity_count
