# SOC-2 Evidence — AI Control Tower

## CC6.1 — Logical Access
- **Evidence**: RBAC logs in `audit.log`
- **Sample**: `{“user”: “ivanov”, “action”: “policy_apply”, “result”: “denied”}`

## CC6.2 — Authentication
- **Evidence**: SSO logs in `sso.log`
- **Sample**: `{“user”: “petrov”, “sso_provider”: “AzureAD”, “offboarded”: true}`

## CC7.2 — Monitoring
- **Evidence**: WORM-log with SHA-256 hash
- **Sample**: `{“log”: “...”, “hash”: “abc123...”}`

## A1.2 — Encryption
- **Evidence**: KMS usage in `kms.log`
- **Sample**: `{“key_id”: “kms-eu-west-1”, “action”: “encrypt”}`
