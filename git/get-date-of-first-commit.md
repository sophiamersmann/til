# Get date of first commit in git

To retrieve a list of days on which a file has been committed to git, use `git log` with a specific format that outputs the committer date only. For example, `%cs` outputs the committer date in short format (`YYYY-MM-DD`). See [pretty-formats](https://git-scm.com/docs/pretty-formats#Documentation/pretty-formats.txt-emcsem) for more options.

```bash
git log --pretty='format:%cs' <FILE> | tail -1
```

`git log` outputs a list of committer dates, sorted from more to less recent. Grab the date of first commit by using the `tail` command.
