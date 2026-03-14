SWC_REGISTRY = {
    "reentrancy": "SWC-107",
    "integer overflow": "SWC-101",
    "integer underflow": "SWC-101",
    "access control": "SWC-105",
    "unchecked call": "SWC-104",
    "timestamp dependence": "SWC-116",
    "tx.origin": "SWC-115",
}


def map_to_swc(vulnerability):

    vuln = vulnerability.lower()

    for key, value in SWC_REGISTRY.items():
        if key in vuln:
            return value

    return "SWC-UNKNOWN"
