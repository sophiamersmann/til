# Load environment variables from file

If you have a text file with key/value pairs like:

```
API=http://localhost:8080
USERNAME=my-username
```

and want to export them into the shell environment, you can do so with:

```bash
export $(cat .env | xargs)
```

The contents of `.env` are piped into `xargs` which constructs a single-line string where the key/value pairs are separated by a whitespace. `export` then exports these key/value pairs as variables into the shell environment.

This is usually good enough for me, but if you want to account for comments and other special cases, [here is a nice answer on StackOverflow](https://stackoverflow.com/questions/19331497/set-environment-variables-from-file-of-key-value-pairs).
