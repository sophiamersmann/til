# Play and pause animations on hover

For my website, I had used CSS background patterns from [here](https://www.magicpattern.design/tools/css-backgrounds) to highlight some of my work. I thought it'd be nice to animate those pattern when a link is hovered over.

Let's say we have a pattern of diagonal lines like this one:

```css
a .pattern {
  background-color: aliceblue;
  opacity: 0.8;
  background-size: 10px 10px;
  background-image: repeating-linear-gradient(
    45deg,
    steelblue 0,
    steelblue 1px,
    aliceblue 0,
    aliceblue 50%
  );
}
```

Making the lines "move" from left to right, requires animating the `background-position` property:

```css
@keyframes move {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: 1000px 0;
  }
}

a:hover .pattern {
  animation: move 60s linear infinite alternate;
}
```

The x position is thus animated from `0px` to `1000px`. When the sequence is complete, the animation is played backwards (from `1000px` to `0px`), then forwards again, and so on. Note that a rather large duration (60 seconds) and distance (1000px) are used. These values are chosen to ensure that the backwards animation only kicks in when hovering over a link for a really long time, because I prefer having the lines to be animated from left to right (in the forwards direction).

The problem here is that, when the user stops hovering over the link, the animation jumps back to its initial position. Instead, I would like the animation to be _paused_ and then _resumed_ when the user hovers over the link again.

To achieve this, the `animate` property is applied to the pattern in its default (not-hovered) state and then _immediately_ paused, like this:

```css
a .pattern {
  background-color: aliceblue;
  opacity: 0.8;
  background-size: 10px 10px;
  background-image: repeating-linear-gradient(
    45deg,
    steelblue 0,
    steelblue 1px,
    aliceblue 0,
    aliceblue 50%
  );

  /* define the animation here but immediately pause it */
  animation: move 60s linear infinite alternate;
  animation-play-state: paused;
}
```

When the user hovers over the link, the animation is simply unpaused:

```css
a:hover .pattern {
  animation-play-state: running;
}
```

And that's it! The animation is now paused when the user stops hovering, and resumed when the user hovers over the link again.
