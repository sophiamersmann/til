# Custom transform that removes units

Style dictionary builds design tokens for various platforms including, for example, CSS and JavaScript. While CSS variables usually need units, I often want js values to be in number format. To remove units from tokens when building, register a custom transform:

```js
// build.cjs

const StyleDictionary = require("style-dictionary");

// register custom transform that removes units
StyleDictionary.registerTransform({
  name: "size/unitless",
  type: "value",
  // filter for specific categories
  matcher: (token) => token.attributes.category === "some-category",
  // remove all characters
  transformer: (token) => +token.value.replace(/[a-z]/gim, ""),
});

// apply the configuration
const StyleDictionaryExtended = StyleDictionary.extend(
  __dirname + "/config.json"
);

// build tokens
StyleDictionaryExtended.buildAllPlatforms();
```

This assumes `config.json` lives in the same directory; the custom transformation can then be referenced like:

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
