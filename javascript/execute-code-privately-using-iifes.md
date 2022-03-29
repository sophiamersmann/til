# Execute code privately using IIFEs

Immediately Invoked Function Expressions (IIFEs) create a private context that is useful to avoid polluting the global namespace. One can also choose to make specific variables or functions defined within an IIFE public by deliberately exposing them to the global namespace.

An IIFE runs as soon as it is defined:

```js
// this function is immediately invoked
(function () {
  // private variables and functions
})();
```

Variables and functions defined within an IIFE will be discarded after the IIFE is executed.

If you want to expose a function or variable to the global namespace, return it from the IIFE:

```js
var exposed = (function () {
  var privateVariable;

  function privateFunction() {
    // some code
  }

  function publicFunction() {
    // some code, potentially calling privateFunction()
  }

  return { publicFunction };
})();
```

After the IIFE has been executed, you can call the exposed function: `exposed.publicFunction()`.
