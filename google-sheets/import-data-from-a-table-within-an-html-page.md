# Import data from a table within an HTML page

`IMPORTHTML` allows to quickly pull a table or list from a website into a Google Sheet. Type `=IMPORTHTML(url, 'table' | 'list', index)` where index starts at 1 and marks the position of the table (or list) within the website.

For example,

```
=IMPORTHTML("http://en.wikipedia.org/wiki/Demographics_of_India", "table", 4)
```

pulls in the fourth table from "http://en.wikipedia.org/wiki/Demographics_of_India".
