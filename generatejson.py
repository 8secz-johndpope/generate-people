import json
from cleanfolder import clean_folder


def generate_geojson(people):
    clean_folder("dist/json")

    for person in people:
        name = person["name"]
        with open(f"dist/json/{name}.json", "w") as outfile:
            json.dump(person, outfile)
