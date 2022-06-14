# Load secret environment variables using [dotenv](https://www.npmjs.com/package/dotenv)

I usually keep secret environment variables in a `.env.local` file (not checked into version control) and use [dotenv](https://www.npmjs.com/package/dotenv) to load the variables into `process.env`. To make these secrets available in a GitHub action, the variables need to be [stored as an encrypted secret on GitHub](https://docs.github.com/en/actions/security-guides/encrypted-secrets). If stored as `MY_SECRET`, the secret is available in an action as `secrets.MY_SECRET`. To be able to load this variable using [dotenv](https://www.npmjs.com/package/dotenv), the variable needs to be written to the `.env.local` file. The following step implements this:

```yaml
steps:
  - name: Create .env.local file
    run: |
      touch .env.local
      echo MY_SECRET=$MY_SECRET >> .env.local
    env:
      MY_SECRET: ${{ secrets.MY_SECRET }}
```
