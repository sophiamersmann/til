# Rendering Bing tiles with MapLibre

[MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js) is an open-source JavaScript library that uses [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to render maps on the web. It's usually used to render vector tiles but it is possible to render raster tiles, including raster tiles from [Bing](https://www.bing.com/maps/).

Tile sources are specified in a [stylesheet](https://maplibre.org/maplibre-gl-js-docs/style-spec/). A minimal stylesheet to render raster tiles could look like this:

```json
{
  // version number, must be 8
  "version": 8,
  // arbitrary, human-readable name
  "name": "my-map",
  // tile sources
  "sources": {
    // arbitrary name
    "bing": {
      // tile type
      "type": "raster",
      // list of tile source URLs
      // (example url for now, but should be a list of Bing URLs!)
      "tiles": [
        "http://a.example.com/wms?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&width=256&height=256&layers=example"
      ],
      // minimum visual size to display tiles (in px), default: 512
      "tileSize": 512,
      // minimum zoom level for which tiles are available, default: 0
      "minzoom": 0,
      // maximum zoom level for which tiles are available, default: 22
      "maxzoom": 22
    }
  },
  // list of layers
  "layers": [
    {
      // raster layer that uses the "bing" layer defined above
      "id": "bing-layer",
      "type": "raster",
      "source": "bing"
    }
  ]
}
```

In brief, a raster source is specified that is then used in a layer. When rendering Bing maps, the tricky bit is finding the correct tile URL since [tile URLs for Bing maps actually change regularly](https://learn.microsoft.com/en-us/bingmaps/rest-services/directly-accessing-the-bing-maps-tiles). We will thus need to request the current tile URL at the time of rendering. To do so, fetch data from

```
https://dev.virtualearth.net/REST/V1/Imagery/Metadata/RoadOnDemand?uriScheme=https&output=json&include=ImageryProviders&key=BING_API_KEY
```

A couple of notes on this API call:

- `RoadOnDemand` specified the type of imagery, all available options are listed [on this documentation page](https://learn.microsoft.com/en-us/bingmaps/rest-services/imagery/get-imagery-metadata) but I find that only a subset of these work in this setting (including `Aerial`, `AerialWithLabelsOnDemand`, `CanvasDark`, `CanvasLight`, `CanvasGray`, `RoadOnDemand`) – `RoadOnDemand` gives you the [default Bing map look](https://www.bing.com/maps/)
- `uriScheme=https` is important to give you HTTPS tile URLs which is important if you plan to serve maps from a HTTPS site (since most browsers refuse to load HTTP content from HTTPS sites)
- `key=BING_API_KEY`: private Bing key

The data is returned as JSON (since `output=json` is set). The relevant field of the returned data is `resourceSets[0].resources` and looks like:

```json
[
  {
    "__type": "ImageryMetadata:http://schemas.microsoft.com/search/local/ws/rest/v1",
    "imageHeight": 256,
    "imageUrl": "https://{subdomain}.ssl.ak.dynamic.tiles.virtualearth.net/comp/ch/{quadkey}?mkt=en-US&it=G,L&shading=hill&og=2097&n=z",
    "imageUrlSubdomains": ["t0", "t1", "t2", "t3"],
    "imageWidth": 256,
    "vintageEnd": null,
    "vintageStart": null,
    "zoomMax": 21,
    "zoomMin": 1
  }
]
```

The field `imageUrl` holds the tile URL we are looking for. The `{subdomain}` placeholder is to be replaced with values from `imageUrlSubdomains`. Using a different subdomain for each tile request helps to get around browser URL request limits.

These tile URLs (with various subdomains) can then be written to the stylesheet which is then used to initialize a MapLibre map. We'll also grab some more information about Bing maps, like the image size and min and max zoom levels.

```js
// import map style
import mapStyle from "./my-map-styles.json";

fetch(
  "https://dev.virtualearth.net/REST/V1/Imagery/Metadata/RoadOnDemand?uriScheme=https&output=json&include=ImageryProviders&key=BING_API_KEY"
)
  .then((res) => res.json())
  .then((data) => {
    // get resource
    const resource = data.resourceSets[0].resources[0];

    // fill in tile URLs (one tile URL for each subdomain)
    mapStyle.sources.bing.tiles = resource.imageUrlSubdomains.map((subdomain) =>
      resource.imageUrl.replace(/{subdomain}/g, subdomain)
    );

    // additionally read the tile size and min/max zoom levels
    mapStyle.sources.bing.tileSize = resource.imageWidth;
    mapStyle.sources.bing.minzoom = resource.zoomMin;
    mapStyle.sources.bing.maxzoom = resource.zoomMax;

    // initialize map
    const map = new maplibregl.Map({
      container: "some-container-id",
      style: mapStyle,
      // initial zoom level and position
      zoom: 8,
      center: [13.42475, 52.5072],
    });
  });
```
