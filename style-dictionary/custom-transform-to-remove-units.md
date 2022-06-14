# Custom transform that removes units

Style dictionary builds design tokens for various platforms including, for example, CSS and JavaScript. While CSS variables need units, I usually want some of the js values in number format. To remove units from tokens when building, one needs to register a custom transform. Consider the following code:

```js
// build.cjs

const StyleDictionary = require("style-dictionary");

// register custom transform that removes units
StyleDictionary.registerTransform({
  name: "size/unitless",
  type: "value",
  matcher: (token) => token.attributes.category === "some-category",
  transformer: (token) => +token.value.replace(/[a-z]/gim, ""),
});

// apply the configuration
const StyleDictionaryExtended = StyleDictionary.extend(
  __dirname + "/config.json"
);

// build tokens
StyleDictionaryExtended.buildAllPlatforms();
```

This assumes `config.json` lives in the same directory; within the configuration, we can then reference the custom transform as follows:

```json
{
  ...,
  "platforms": {
    "js": {
      "transformGroup": "js",
      "transforms": [
        "attribute/cti",
        "name/cti/camel",
        "size/unitless",
        "color/hex"
      ],
      "buildPath": "path/to/build/directory",
      "files": [
        {
          "destination": "tokens.js",
          "format": "javascript/es6"
        }
      ]
    }
  }
}
```

To build style dictionary, run `node /build.cjs`.
