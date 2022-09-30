# Store data in local storage

Storing local data for the document's origin can either be done via `window.localStorage` or `window.sessionStorage`. Unlike session storage, that gets cleared when a session ends, data stored in local storage has no expiration date.

`window.localStorage` might not be supported or throw a `SecurityError` if the origin is not valid or the user has configured the browser to not persist data (e.g. the user blocked cookies).

Code Example:

```js
try {
  if (window.localStorage) {
    // write to local storage
    window.localStorage.setItem("my-local-storage-data", JSON.stringify(data));

    // read from local storage
    let data = window.localStorage.getItem("my-local-storage-data");
    if (data) {
      data = JSON.parse(data);
    }
  }
} catch (e) {
  console.log("could not access local storage", e.message);
}
```
