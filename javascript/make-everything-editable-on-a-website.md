# Make everything editable on a website

There is a neat trick to render an entire HTML document editable. Simply type this into the console to turn `designMode` on:

```js
document.designMode = "on";
```

The content of every text element in the document will then be editable (as if you set `contenteditable="true"` on each of them).
