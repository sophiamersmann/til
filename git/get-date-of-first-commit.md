# Find the creation date of a file in a repository

To retrieve a list of dates on which a file has been committed to git, use `git log` with a specific format that outputs the committer date only. For example, `%cs` outputs the committer date in short format (`YYYY-MM-DD`). See [pretty-formats](https://git-scm.com/docs/pretty-formats#Documentation/pretty-formats.txt-emcsem) for more options.

```bash
git log --pretty='format:%cs' <filename> | tail -1
```

`git log` outputs a list of committer dates, sorted from recent commits to less recent commits. Grab the creation date by using the `tail` command.
