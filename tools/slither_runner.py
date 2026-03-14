import subprocess

def run_slither(contract_path):

    try:
        result = subprocess.run(
            ["slither", contract_path],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return str(e)