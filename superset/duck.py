import duckdb

con = duckdb.connect("superset/peets_uae.duckdb")

# get list of table names
tables = [row[0] for row in con.execute("SHOW TABLES").fetchall()]
print("Found tables:", tables)

# export each table to a CSV with same name
for t in tables:
    csv_name = f"{t}.csv"
    print(f"Exporting {t} -> {csv_name}")
    con.execute(f"COPY {t} TO '{csv_name}' (HEADER, DELIMITER ',');")

con.close()
