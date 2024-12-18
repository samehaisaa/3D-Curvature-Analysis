import numpy as np
import trimesh
from trimesh.curvature import discrete_gaussian_curvature_measure
from tqdm import tqdm

def gauss_curvature(mesh, points=None, radius=1.0):
    """
    Calculate the Gaussian curvature using the discrete Gaussian curvature measure
    from trimesh.

    Parameters:
    - mesh: The mesh object.
    - points: The points where the curvature is to be evaluated (optional).
    - radius: The radius around each point to consider for curvature calculation.

    Returns:
    - gauss_curv: The calculated Gaussian curvature at each point in the mesh.
    """
    # If points are not specified, use the mesh vertices
    if points is None:
        points = mesh.vertices

    # Use the trimesh function for Gaussian curvature calculation
    gauss_curv = discrete_gaussian_curvature_measure(mesh, points, radius)
    
    return gauss_curv
