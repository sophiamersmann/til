# Checkout full history of repo

By default [actions/checkout](https://github.com/actions/checkout) only fetches the last commit. Sometimes, you might want to fetch the full history of a repo. Do so by specifying `fetch-depth` appropriately.

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
