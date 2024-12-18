import pyvista as pv
import numpy as np

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
