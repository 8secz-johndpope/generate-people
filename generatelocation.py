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
    outmulti = []
    for pol in multipoly1:
        for pol2 in multipoly2:
            if pol.intersects(pol2) == True:
                # If they intersect, create a new polygon that is
                # essentially pol minus the intersection
                nonoverlap = (pol.symmetric_difference(pol2)).difference(pol2)
                outmulti.append(nonoverlap)

            else:
                # Otherwise, just keep the initial polygon as it is.
                outmulti.append(pol)

    return sgeom.MultiPolygon(outmulti)


land_geom = unary_union(list(shpreader.Reader(land_shp_fname).geometries()))
lake_geom = unary_union(list(shpreader.Reader(lake_shp_fname).geometries()))
actual_land_geom = cut_out(land_geom, lake_geom)
land = prep(actual_land_geom)


def is_land(x, y):
    return land.contains(sgeom.Point(x, y))


def get_coord():
    coord = []
    while True:
        coord = [(random() * 2 - 1) * 180, (acos(2 * random() - 1) / pi) * 180 - 90]
        if is_land(*coord):
            break
    return coord
