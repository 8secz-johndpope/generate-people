import json


def generate_feature(person):
    return {
        "type": "Feature",
        "properties": {"title": person.name},
        "geometry": {"coordinates": person.location, "type": "Point"},
    }


def generate_geojson(people):
    features = [generate_feature(person) for person in people]
    geojson = {"features": features, "type": "FeatureCollection"}
    with open("dist/people.geojson", "w") as outfile:
        json.dump(geojson, outfile)
