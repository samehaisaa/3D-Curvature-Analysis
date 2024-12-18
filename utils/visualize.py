import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt  # Add this line if it's missing

def visualize_curvature(mesh, curvature_values, title="Courbure"):
    """
    Visualize curvature values on the 3D mesh using PyVista.
    :param mesh: Trimesh object
    :param curvature_values: Array of curvature values (one per vertex)
    :param title: Title of the visualization
    """
    # Convert Trimesh to PyVista format
    faces = mesh.faces

    # Ensure faces are triangular
    if faces.ndim == 1:
        n_faces = len(faces) // 3
        faces = faces.reshape((n_faces, 3))
    elif faces.shape[1] != 3:
        raise ValueError("Faces are not triangular. Please check the mesh.")

    # PyVista expects faces in a "vtk-style" format
    vtk_faces = []
    for face in faces:
        vtk_faces.append([3, *face])  # 3 indicates the number of vertices per face
    vtk_faces = np.array(vtk_faces).flatten()

    pv_mesh = pv.PolyData(mesh.vertices, vtk_faces)

    # Add curvature values as a scalar field
    pv_mesh.point_data[title] = curvature_values

    # Create a plotter
    plotter = pv.Plotter()
    plotter.add_mesh(pv_mesh, scalars=title, cmap="coolwarm", show_edges=True)
    plotter.add_title(title, font_size=16)
    plotter.show()



def visualize_mean_curvature(mesh, mean_curvature):
    """
    Visualize the mean curvature on the mesh by coloring the vertices.
    
    Parameters:
    - mesh: Trimesh object containing the 3D mesh.
    - mean_curvature: A numpy array of mean curvature values for each vertex.
    """
    # Normalize the curvature values for visualization
    normalized_curvature = mean_curvature 
    # Map the curvature values to a colormap (you can adjust this as needed)
    colormap = plt.cm.viridis(normalized_curvature)
    
    # Apply the colormap to the vertices
    mesh.visual.vertex_colors = (colormap[:, :3] * 255).astype(np.uint8)
    
    # Show the mesh with curvature visualization
    mesh.show()
