"""Maintains stuff

Files:
- places.csv: source of truth
- db.csv: places in the city, populated with Google Maps info, used for slides

Workflow:
    - read places.csv
    - extend db.csv entries
    - update db.csv info
    - compile slides
    - compile trip info
"""

import polars as pl
import pathlib


def compile_slides():
    """
    - use places.csv to update target list
    - update place data if cache older than one day
    - use data to compile slides
    """
    pass


def sort_places(file_name):
    """Sort the list of places
    """
    assert pathlib.Path(file_name).is_file()

    query = (
        pl.scan_csv(file_name)  #
        .sort(["been", "name", "award"])  #
    )
    df = query.collect()
    assert df["name"].is_unique().all(), "{key: name} is not unique"
    df.write_csv(file_name)


def fix_typos(dir_name):
    """Fix those typos we made updating beli list/scores in ./preference
    """
    # NOTE: have a canonical list somewhere
    assert (pref_dir := pathlib.Path(dir_name)).is_dir()
    for p in pref_dir.glob("*.csv"):
        if p.stem == "template":
            continue
        with p.open() as pref:
            pass
            # do fuzzy search?
            # find, and then ask if we want to fix: (1) keep (2) replace (3) manual


if __name__ == "__main__":
    sort_places("places.csv")
