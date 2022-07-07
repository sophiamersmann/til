# Generate a random secret

This is a useful recipe to create a random secret such as a API token:

```bash
python -c 'import secrets; print(secrets.token_hex(32))'
```
