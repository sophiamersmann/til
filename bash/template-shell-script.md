# Template shell script

Dumping here the template script I usually use for shell scripts. It roughly follows the suggestions outlined in [this blog post](https://sharats.me/posts/shell-script-best-practices/).

```bash
#!/usr/bin/env bash

usage() {
  echo -e "Usage: ./$(basename $0) [-o|--option]

Does something

  --option \t example option
"
  exit
}

# show help
if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
  usage
fi

set -o errexit  # exit script when a command fails
set -o nounset  # fail when accessing an unset variable
set -o pipefail  # treats pipeline command as failed when one command in the pipeline fails
set -o xtrace  # prints every command before execution

# make sure to run from the script's directory
cd $(dirname $0)


do_something() {
  echo 'doing something'
}

main() {
  # check for the option
  if [[ "${1-}" =~ ^-*o(ption)?$ ]]; then
    echo '--option flag is set'
  fi

  do_something
}

main "$@"
```
