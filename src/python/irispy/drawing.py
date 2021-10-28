from __future__ import print_function

import matplotlib.pyplot as plt
import scipy.spatial
import numpy as np
from matplotlib.colors import colorConverter
import mpl_toolkits.mplot3d as a3
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial.qhull import QhullError


def draw(self, ax=None, **kwargs):
    if self.getDimension() == 2:
        return self.draw2d(ax=ax, **kwargs)
    elif self.getDimension() == 3:
        return self.draw3d(ax=ax, **kwargs)
    else:
        raise NotImplementedError("drawing for objects of dimension <2 or >3 not implemented yet")


def draw2d(self, ax=None, **kwargs):
    if ax is None:
        ax = plt.gca()
    points = self.getDrawingVertices()
    kwargs.setdefault("edgecolor", self.default_color)
    return draw_2d_convhull(points, ax, **kwargs)


def draw3d(self, ax=None, **kwargs):
    if ax is None:
        ax = a3.Axes3D(plt.gcf())
    points = self.getDrawingVertices()
    kwargs.setdefault("facecolor", self.default_color)
    return draw_3d_convhull(points, ax, **kwargs)


def draw_convhull(points, ax, **kwargs):
    dim = points.shape[1]
    if dim == 2:
        return draw_2d_convhull(points, ax, **kwargs)
    elif dim == 3:
        return draw_3d_convhull(points, ax, **kwargs)
    else:
        raise NotImplementedError("not implemented for dimension < 2 or > 3")


def draw_2d_convhull(points, ax, **kwargs):
    hull = scipy.spatial.ConvexHull(points)
    kwargs.setdefault("facecolor", "none")
    return [ax.add_patch(plt.Polygon(xy=points[hull.vertices], **kwargs))]


def draw_3d_convhull(points, ax, **kwargs):
    kwargs.setdefault("edgecolor", "k")
    kwargs.setdefault("facecolor", "r")
    kwargs.setdefault("alpha", 0.5)
    kwargs["facecolor"] = colorConverter.to_rgba(kwargs["facecolor"], kwargs["alpha"])

    artists = []
    try:
        hull = scipy.spatial.ConvexHull(points)
        for simplex in hull.simplices:
            poly = Poly3DCollection([points[simplex]], **kwargs)
            if "alpha" in kwargs:
                poly.set_alpha(kwargs["alpha"])
            ax.add_collection3d(poly)
            artists.append(poly)
    except QhullError as e:
        if len(points) >= 3:
            # TODO: fix plotting color
            try:
                col = ax.plot_trisurf(points[:, 0], points[:, 1], points[:, 2], **kwargs)
            except ValueError:
                # happens when the surface is vertical
                p3dc = Poly3DCollection(points, **kwargs)
                col = ax.add_collection3d(p3dc)
        else:
            col = ax.plot(points[:, 0], points[:, 1], points[:, 2], "ko-")
        # p3dc = Poly3DCollection(points, **kwargs)
        # ax.add_collection3d(p3dc)
        if isinstance(col, list):
            artists.extend(col)
        else:
            artists.append(col)

    return artists
