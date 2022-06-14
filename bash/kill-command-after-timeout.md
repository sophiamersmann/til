# Kill command after a timeout

I suspect these requirements to be rather niche but I found myself today wanting to start up a development server for a short amount of time. To do so in bash, one can run:

```bash
( npm run dev ) & sleep 30 ; kill $!
```

This runs the command within the parenthesis (here, `npm run dev`) in a subshell for thirty seconds and then kills it. The `$!` variable is a Bash builtin that contains the process ID of the most recently started subshell.
