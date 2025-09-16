from typing import List, Dict

def get_soc2_evidence(logs: List[dict]) -> Dict[str, str]:
    return {
        "CC6.1": "Access control enforced via RBAC → see logs",
        "CC6.2": "Authentication via SSO → see SSO logs",
        "CC6.3": "Authorization via Policy Engine → see policy logs",
        "CC7.2": "Monitoring via audit-trail → see WORM-log",
        "A1.2": "Data encryption at rest → see KMS usage",
    }
