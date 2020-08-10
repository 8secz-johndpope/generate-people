import names
from random import random
from math import pi, acos
import cartopy.io.shapereader as shpreader
import shapely.geometry as sgeom
from shapely.ops import unary_union
from shapely.prepared import prep
import json
from numpy.random import choice

distribution = (0.5, 0.5)

land_shp_fname = shpreader.natural_earth(
    resolution="50m", category="physical", name="land"
)

land_geom = unary_union(list(shpreader.Reader(land_shp_fname).geometries()))
land = prep(land_geom)


def is_land(x, y):
    return land.contains(sgeom.Point(x, y))


def get_coord():
    coord = []
    while True:
        coord = [(random() * 2 - 1) * 180, (acos(2 * random() - 1) / pi) * 180 - 90]
        if is_land(*coord):
            break
    return coord


def get_random_point():
    return {
        "type": "Feature",
        "properties": {
            "title": names.get_full_name(
                gender=choice(("male", "female"), p=distribution)
            )
        },
        "geometry": {"coordinates": get_coord(), "type": "Point"},
    }


def get_geojson():
    features = []
    for i in range(2000):
        features.append(get_random_point())
    return {"features": features, "type": "FeatureCollection"}


if __name__ == "__main__":
    with open("people.geojson", "w") as outfile:
        json.dump(get_geojson(), outfile)
