# Checkout the full history of a repository

By default [actions/checkout](https://github.com/actions/checkout) only fetches the last commit to a repository. Sometimes, you might want to fetch the full history of a repository instead. Do so by setting `fetch-depth` to `0` (default: `1`).

```yml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repo
        uses: actions/checkout@v2
         with:
          # fetch full history of repo
          fetch-depth: 0
```
