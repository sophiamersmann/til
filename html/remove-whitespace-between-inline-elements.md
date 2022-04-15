# Remove whitespace between inline elements

Browsers render whitespaces between inline elements by default. For example, the following buttons are rendered with a narrow space between them (since they're separated by a new line character in the markup):

```html
<div class="wrapper">
  <button>B1</button>
  <button>B2</button>
</div>
```

The pragmatic solution is to simply remove the whitespace from the markup:

```html
<!-- prettier-ignore -->
<div class="wrapper">
  <button>B1</button><button>B2</button>
</div>
```

However, this can make the markup more difficult to read and maintain. Alternatively, you might want to separate the buttons by a comment:

```html
<!-- prettier-ignore -->
<div class="wrapper">
  <button>B1</button><!-- 
--><button>B2</button>
</div>
```

but that can interfere with automatic code formatters like prettier (though possibly there is a setting that accounts for this but I am not aware). If you want to keep the markup intact, you can also reach for a pure CSS solution and use a technique people refer to as the [font-size trick](https://stackoverflow.com/questions/5078239/how-to-remove-the-space-between-inline-inline-block-elements).

```html
<div class="wrapper">
  <button>B1</button>
  <button>B2</button>
</div>
```

```css
.wrapper {
  font-size: 0;
}

.wrapper button {
  font-size: 1rem;
}
```

Setting `font-size` to `0` on the parent element will essentially render a zero-size whitespace between the buttons (hence, nothing at all is rendered). The font size can then be restored on the buttons itself.
