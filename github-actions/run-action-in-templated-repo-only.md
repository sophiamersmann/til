# Run action in a templated repository only

Defining GitHub actions in template repositories that do not run in the template repo itself but in copies of the template repo only is possible by using an if statement that checks the `github.repository` variable.

```yaml
jobs:
  my-job:
    runs-on: ubuntu-latest

    # only run action in copies of this repo
    if: ${{ github.repository != 'sophiamersmann/my-template-repo' }}
```

Here, `sophiamersmann/my-template-repo` is the template repository. This runs the action only in repositories other than `sophiamersmann/my-template-repo`.
