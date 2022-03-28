# Run Python script in GitHub actions

Use [`actions/setup-python`](https://github.com/marketplace/actions/setup-python) to setup Python. You might also want to specify a Python version. The script to run, `my_script.py` below, lives in the repo's root.

```yml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repo
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: 3.8
      - name: Run Python script
        run: |-
          python my_script.py
```
