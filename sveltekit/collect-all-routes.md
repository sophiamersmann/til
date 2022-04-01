# Collect all routes in a SvelteKit application (development only)

Sometimes in development I find it useful to link to all routes in the application on the index page. Here is a hacky way to do that. It uses [Vite's glob import](https://vitejs.dev/guide/features.html#glob-import) that imports multiple modules from the file system via the special `import.meta.glob` function. (You probably don't want to do this in production though.)

```js
// load all routes
const modules = import.meta.glob("./**.svelte");

// extract filenames
const filenames = [];
for (let filename in modules) {
  filename = filename.slice(2).replace(".svelte", "");
  filenames.push(filename);
}
```

When run from the index file, the glob pattern (`'./**.svelte'`) will import all svelte files in the routes directory, including nested ones. Normally you would run this code before the component is created and send the results to the component as a prop.

```svelte
<script context="module">
	export async function load() {
		const modules = import.meta.glob('./**.svelte');

		const filenames = [];
		for (let filename in modules) {
			filename = filename.slice(2).replace('.svelte', '');
			filenames.push(filename);
		}

		return {
			props: {
				routes: filenames
			}
		};
	}
</script>

<script>
	export let routes;
</script>

<ul>
	{#each routes as route}
		<li><a href={route}>{route}</a></li>
	{/each}
</ul>
```
