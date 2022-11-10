# Write temporary files from Cloud Functions

Cloud Functions run in a serverless environment managed by Google. Though Cloud Functions are commonly stateless, it is possible to write to the temporary directory `/tmp`. For example, in Python:

```python
# path to a file in the temporary directory
filename = "/tmp/my-file.txt"
# make sure the directory exists
os.makedirs(os.path.dirname(filename), exist_ok=True)
# write to file
with open(filename, "w") as f:
  f.write('Content')
```

[It is advised to always delete temporary files](https://cloud.google.com/functions/docs/bestpractices/tips#always_delete_temporary_files) since written files consume memory available to the function and sometimes persist between invocations.

If you don't want to write to `/tmp` in a local setup, use an environment variable to differentiate between development and production. For example,

```python
# in development, write to the working directory
if "FUNCTION_ENV" in os.environ and os.environ["FUNCTION_ENV"] == "development":
  root = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(root, "my-file.txt")
# in production, write to /tmp
else:
  filename = "/tmp/my-file.txt"
```
