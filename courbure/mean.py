import numpy as np

from trimesh import curvature

def calculate_mean_curvature(mesh, radius=0.1):
    """
    Calculate the mean curvature of the mesh using the method from the `trimesh` repository.
    
    Parameters:
    - mesh: Trimesh object containing the 3D mesh.
    - radius: The radius around each point for calculating curvature (default is 0.1).
    
    Returns:
    - mean_curvature: A numpy array of mean curvature values for each vertex in the mesh.
    """
    # Get the points (vertices) of the mesh
    points = mesh.vertices
    
    # Calculate the mean curvature using the method provided in the trimesh repo
    mean_curvature = curvature.discrete_mean_curvature_measure(mesh, points, radius)
    
    return mean_curvature
