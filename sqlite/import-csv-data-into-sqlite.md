# Import CSV data into SQLite

Data can be imported into SQLite from a CSV file with `.import`.

Open the database:

```bash
sqlite3 database.db
```

Then, import the CSV file:

```sql
-- ensures the imported file is treated as CSV
.mode csv
-- import csv data into a table
.import filename.csv table_name
```

`.mode csv` ensures the imported file is treated as CSV.
