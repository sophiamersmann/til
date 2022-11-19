# Sync compressed files to Google Cloud Storage

When _copying_ local files to the cloud, `gsutil cp` provides the `-z` option that applies gzip content-encoding to any uploaded file that matches the given extension(s). For example, to upload web content a command could look like:

```bash
gsutil -m cp -r -z html,css,js my-local-dir/ gs://my-bucket/my-path
```

Files are copied recursively (`-r`) from `my-local-dir` to the cloud location, and HTML, CSS and JavaScript files are compressed on upload (`-z html,css,js`).

Unfortunately, such an option does not exist for the `gsutil sync` utility that _syncs_ files to the cloud. To achieve syncing of compressed files, we will need to compress the files ourselves and then adjust the files' content types and encodings appropriately.

First, compress text files in place:

```bash
# find all files to be compressed (here, *.html, *.css and *.js files)
text_files=$(find my-local-dir -name '*.html' -o -name '*.css' -o -name '*.js')
# compress each file using gzip (in-place)
for f in $text_files; do gzip $f && mv $f.gz $f; done
```

Then, sync the directory:

```bash
gsutil rsync -d -r -c  my-local-dir/ gs://my-bucket/my-path
```

Finally, configure content types and encodings:

```bash
gsutil setmeta \
  -h 'Content-Encoding:gzip' \
  -h 'Content-Type:text/html' gs://my-bucket/my-path/**/*.html
gsutil setmeta \
  -h 'Content-Encoding:gzip' \
  -h 'Content-Type:text/css' gs://my-bucket/my-path/**/*.css
gsutil setmeta \
  -h 'Content-Encoding:gzip' \
  -h 'Content-Type:text/javascript' gs://my-bucket/my-path/**/*.js
```
