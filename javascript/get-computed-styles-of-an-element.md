# Get computed styles of an element on the page

I was in need to find the fill color of a SVG `<rect />` element but I had no way of knowing how the fill color was set. It could have been set as an attribute, as part of the style attribute, via CSS or via JS:

```html
<rect width="50" height="50" fill="steelblue"></rect>
<rect width="50" height="50" style="fill: steelblue"></rect>
<rect id="my-rect" width="50" height="50"></rect>
```

```css
#my-rect {
  fill: steelblue;
}
```

I thought to get the current color of the rectangle, I would need to read both, `myRect.getAttribute('fill')` and `myRect.style.fill` and figure out which one is currently in use. Turns out that doesn't work since the `style` property only contains styles assigned in a style attribute or set by scripting (CSS styles would thus be missed!). Aside, I needed the _computed_ color, reading a custom property for example would have been no use to me. That is when I learned about [`window.getComputedStyle()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle), a method that returns all style properties of an element _after_ applying stylesheets and performing basic computations (which means that a named color like `blue` gets resolved to `rgb(0, 0, 255)`, for example, and custom properties get resolved too). To get the currently displayed fill color of a rectangle on screen, you would thus use:

```js
const myRect = document.getElementById("my-rect");
window.getComputedStyle(myRect).fill;
```
