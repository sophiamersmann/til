# Assign default values when destructuring an object or array

When dealing with objects as function parameters where some properties have default values, I used to define a default parameters object outside of the function scope and then merge it with the object passed as a parameter. For example:

```js
const defaultOptions = { x: 0, y: 0 };
function add(options = defaultOptions) {
  const { x, y } = { ...defaultOptions, ...options };
  return x + y;
}
```

This works as expected in all cases,

```js
add(); // 0
add({}); // 0
add({ x: 1 }); // 1
add({ x: 1, y: 2 }); // 3
```

but is a bit cumbersome to write and difficult to read. Turns out javascript offers syntax that makes this much easier.

```js
function add({ x = 0, y = 0 } = {}) {
  return x + y;
}
```

Note that the destructuring expression is followed by a default value assignment. This ensures that `x` and `y` are pre-filled when `add` is called without any parameters.

This also works for arrays:

```js
function add([x = 1, y = 2] = []) {
  return x + y;
}
```

Optional value parameters in destructuring expressions also work outside of function parameter definitions.

```js
const { selected = "" } = { selected: "foo" }; // selected is "foo"
const { selected = "" } = { somethingElse: "bar" }; // selected is ""
const { selected = "" } = {}; // selected is ""
```

In this specific case, this is essentially a short-hand for:

```js
const selected = query.selected || "";
```

where `query` is `{ selected: "foo" }`. This can be especially useful if you want to extract many properties with optional default values. Extracting parameters from an object like

```js
const query = {
  firstParameter: "foo",
  secondParameter: "bar",
  thirdParameter: "baz",
};
```

is then as simple as

```js
const {
  firstParameter = "",
  secondParameter = "",
  thirdParameter = "",
} = query;
```

instead of writing separate statements for each parameter.

```js
const firstParameter = query.firstParameter || "";
const secondParameter = query.secondParameter || "";
const thirdParameter = query.thirdParameter || "";
```
