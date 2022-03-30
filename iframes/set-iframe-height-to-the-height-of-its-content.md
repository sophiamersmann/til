# Set a cross-domain iframe's height to the height of its content

Passing the height of the content of an iframe to the page hosting the iframe is non-trivial if iframe and page are hosted on different domains as the same-origin policy restricts communication between resources of different origin.

Cross-origin communication can be safely established, however, via the [post-message API](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage). Two steps are required to resize an iframe's height based on its content:

- **on the page that will be embedded into another page as an iframe:** notify a parent context of the height of the content
- **on the page hosting the iframe:** listen to messages from the embedded iframe and set the iframe's height appropriately

## Minimal implementation

First, an explanation of the essential steps.

### Notify a parent context of the height of the content

On the page that will be embedded into another page as an iframe, post a message to the parent context that communicates the height of the content.

```js
var message = { height: document.body.clientHeight };
window.parent.postMessage(message, "*");
```

Here, `window.parent` will receive the message sent via `postMessage`; it references the parent window from within the embedded iframe. The second argument to `postMessage` controls what the origin of the receiving window must be - `"*"` specifies no preference.

### Listen to messages from the embedded iframe

On the page hosting the iframe, register an event on the window that listens to the `message` event. This event receives messages sent to its context (from anywhere). Make sure to check that the message received has actually been dispatched from within the embedded iframe. The message itself can then be accessed via `e.data`.

```js
var iframe = document.querySelector("#my-iframe");

function updateIframeHeight(e) {
  // security check
  if (iframe.src.indexOf(e.origin) !== 0) return;

  // set iframe height
  if (!e.data["height"]) return;
  iframe.style.height = e.data["height"] + "px";
}

window.addEventListener("message", updateIframeHeight, false);
```

## Production-ready implementation

Often, one would also want to notify the parent window when the size of the embedded iframe changes.

**On the page that will be embedded into another page as an iframe:**

```js
(function () {
  // throttle posting messages to the parent
  var throttledPostMessage = throttle((message) => {
    window.parent.postMessage(message, "*");
  }, 100);

  var resizeObserver = new ResizeObserver((entries) => {
    if (!Array.isArray(entries)) return;
    if (!entries.length) return;

    var entry = entries[0];
    var message = {
      href: window.location.href,
      height: entry.contentRect.height,
    };

    throttledPostMessage(message);
  });

  // use a resize observer to keep track of the body's height
  resizeObserver.observe(document.body);
})();
```

Posting messages is throttled for better performance using [a method from lodash](https://www.npmjs.com/package/lodash.throttle).

**On the page hosting the iframe:**

```js
window.addEventListener(
  "message",
  function (e) {
    // security checks
    var href = e.data["href"];
    if (iframe.src.indexOf(e.origin) !== 0) return;
    if (iframe.src.indexOf(href) !== 0) return;

    if (!e.data["height"]) return;

    iframe.style.height = e.data["height"] + "px";
  },
  false
);
```
