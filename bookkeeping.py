"""Sorts and formats config/data"""

import polars as pl


def sort_places(file_name):
    """Sort the list of places
    """

    query = (
        pl.scan_csv(file_name)  #
        .sort(["been", "name", "award"])  #
    )
    df = query.collect()
    assert df["name"].is_unique().all(), "{key: name} is not unique"
    df.write_csv(file_name)


if __name__ == "__main__":
    sort_places("places.csv")
