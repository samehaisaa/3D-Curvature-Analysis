import numpy as np

class CourbureMoyenne:
    @staticmethod
    def calculer(mesh):
        laplacien = mesh.vertex_normals @ mesh.vertex_normals.T
        aire_voronoi = mesh.vertex_areas
        courbure_moyenne = laplacien / (2 * aire_voronoi)
        return courbure_moyenne
