# Type component parameters when spreading `$$restProps`

Say, you have a simple `<Button />` component that defines custom parameters but is also expected to accept any attribute that is allowed on an HTML `<button />` element. In that case you would probably spread the special `$$restProps` parameter into the `<button />` element like so:

```svelte
<!-- Button.svelte -->
<script lang="ts">
  export let variant: 'primary' | 'secondary' | 'tertiary' = 'primary';
</script>

<button
  type="button"
  {...$$restProps}
  data-variant={variant}
  on:click
>
  <slot>Label missing</slot>
</button>
```

The downside is: By spreading `$$restProps`, all type safety is lost. No type error will be thrown if you pass a parameter to `<Button />` that is neither a custom property of `<Button />` nor a valid attribute on `<button />`. To correct for this, we can extend the type interface of the component by overwriting the special `$$Props` interface:

```svelte
<!-- Button.svelte -->
<script lang="ts">
  type Variant = 'primary' | 'secondary' | 'tertiary';

  interface $$Props extends svelte.JSX.HTMLAttributes<HTMLButtonElement> {
    variant?: Variant;
  }

  export let variant: Variant = 'primary';
</script>
```

`$$Props` is the interface that types the component's parameters. It is usually inferred but can be overwritten. Here, it extends the interface for attributes of a `HTMLButtonElement` instance, and additionally specifies the types of all custom parameters (`variant`). Sadly, you will need to specify the types of the custom parameters twice: once on the `$$Props` interface, once when initializing the variable. If you omit the type definition from the initialization statement, then the parameter will be incorrectly typed throughout the component file (at least at the time of writing).
