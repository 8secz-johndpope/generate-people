from random import random
from math import pi, acos
import cartopy.io.shapereader as shpreader
import shapely.geometry as sgeom
from shapely.ops import unary_union
from shapely.prepared import prep

import matplotlib.pyplot as plt

land_shp_fname = shpreader.natural_earth(
    resolution="50m", category="physical", name="land"
)
lake_shp_fname = shpreader.natural_earth(
    resolution="50m", category="physical", name="lakes"
)


def cut_out(multipoly1, multipoly2):
    return (multipoly1.symmetric_difference(multipoly2)).difference(multipoly2)


land_geom = unary_union(list(shpreader.Reader(land_shp_fname).geometries()))
lake_geom = unary_union(list(shpreader.Reader(lake_shp_fname).geometries()))
actual_land_geom = cut_out(land_geom, lake_geom)
land = prep(actual_land_geom)


def is_land(x, y):
    return land.contains(sgeom.Point(x, y))


def repeat_until(set_function, check_function):
    value = set_function()
    while not check_function(value):
        value = set_function()
    return value


def get_coord():
    return repeat_until(
        lambda: [(random() * 2 - 1) * 180, (acos(2 * random() - 1) / pi) * 180 - 90],
        lambda coord: is_land(*coord) and coord[1] > -65,
    )
