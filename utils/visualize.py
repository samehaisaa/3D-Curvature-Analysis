import pyvista as pv

def visualize(mesh, curvature, title="Curvature Visualization"):
    """
    Visualize the given curvature values on the 3D mesh using PyVista.

    Parameters:
    - mesh: Trimesh object
    - curvature: Array of curvature values
    - title: Title for the visualization window (default: "Curvature Visualization")
    """
    # Convert Trimesh mesh to PyVista mesh
    mesh_pv = pv.PolyData(mesh.vertices, mesh.faces)
    
    # Add curvature data as a scalar field to the PyVista mesh
    mesh_pv["curvature"] = curvature
    
    # Plot with PyVista
    p = pv.Plotter()
    p.add_mesh(mesh_pv, scalars="curvature", cmap="coolwarm", show_edges=False)
    p.add_scalar_bar(title="Curvature", vertical=True)
    p.show(title=title)
