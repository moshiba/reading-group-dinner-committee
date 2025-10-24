"""Sorts and formats config/data"""

import polars as pl

query = (
    pl.scan_csv(file_name := "places.csv")  #
    .sort(["been", "name", "award"])  #
)
df = query.collect()
assert df["name"].is_unique().all(), "{key: name} is not unique"
df.write_csv(file_name)
