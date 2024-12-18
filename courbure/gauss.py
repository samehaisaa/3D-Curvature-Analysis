import numpy as np

class CourbureGauss:
    @staticmethod
    def calculer(mesh):
        angles = mesh.vertex_defects  # Défaut angulaire par sommet
        aire_voronoi = mesh.vertex_areas  # Aire de Voronoi pour chaque sommet
        courbure_gauss = angles / aire_voronoi
        return courbure_gauss
