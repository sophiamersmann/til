# Masonry layout with a clean bottom edge

Masonry layouts arrange items of uneven height across a number of columns. Masonry layouts usually align on top and flow down but I found myself in need for a masonry layout that flows in the other direction, that is, from bottom to top. A tad unnatural for the web to think bottom-up, though there apparently is spec work on grid to make this work in the future (see [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Masonry_Layout)).

To get started, I found a blog post on (traditional) masonry layouts on [CSS-Tricks](https://css-tricks.com/piecing-together-approaches-for-a-css-masonry-layout/) that suggests using flexbox like so:

```scss
.masonry {
  max-height: 1000px;

  // use flexbox to achieve a top-aligned masonry layout
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;

  div {
    // items within the layout share width
    width: 150px;

    // presentation
    background: #ec985a;
    color: white;
    margin: 0 1rem 1rem 0;
    text-align: center;
    font-family: system-ui;
    font-weight: 900;
    font-size: 2rem;
  }

  // each child gets a random height
  @for $i from 1 through 36 {
    div:nth-child(#{$i}) {
      $h: (random(400) + 100) + px;
      height: $h;
      line-height: $h;
    }
  }
}
```

A devious trick to achieve a bottom-aligned masonry layout is to simply rotate the parent container by 180 degree. To correct for the content being upside down, each child gets rotated by 180 degree as well. Note that the rotations put the first child element in the bottom right corner. (This might not be what you want but it works for me.)

```scss
.masonry {
  max-height: 1000px;

  display: flex;
  flex-direction: column;
  flex-wrap: wrap;

  // rotate container
  transform: rotate(180deg);

  div {
    width: 150px;

    // rotate child
    transform: rotate(180deg);

    background: #ec985a;
    color: white;
    margin: 0 1rem 1rem 0;
    text-align: center;
    font-family: system-ui;
    font-weight: 900;
    font-size: 2rem;
  }

  @for $i from 1 through 36 {
    div:nth-child(#{$i}) {
      $h: (random(400) + 100) + px;
      height: $h;
      line-height: $h;
    }
  }
}
```
