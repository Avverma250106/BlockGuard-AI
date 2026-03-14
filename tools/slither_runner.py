import subprocess
import json


def run_slither(contract_path):

    command = [
        "slither",
        contract_path,
        "--json",
        "slither_output.json"
    ]

    subprocess.run(command, capture_output=True)

    with open("slither_output.json") as f:
        data = json.load(f)

    findings = []

    for issue in data["results"]["detectors"]:

        description = issue["description"]

        for element in issue["elements"]:
            if "source_mapping" in element:

                line = element["source_mapping"]["lines"][0]

                findings.append({
                    "description": description,
                    "line": line
                })

    return findings
