# Copy to clipboard

Reading and writing to the clipboard requires the user's permission. When permission has been granted, use `navigator.clipboard.writeText` to write text to the clipboard. There is also `navigator.clipboard.write` for arbitrary data. These functions return a promise that resolves if writing to clipboard was successful and rejects in case of an error.

```js
navigator.permissions.query({ name: "clipboard-write" }).then((result) => {
  if (result.state === "granted" || result.state === "prompt") {
    navigator.clipboard.writeText('This bit will be written to the clipboard if all goes well').then(
      () => console.log("Success! Copied to clipboard!");,
      () => console.log("Copy to clipboard failed")
    );
  }
});
```
