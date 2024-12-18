import pyvista as pv

def visualize_curvature(mesh, curvature_values, title="Curvature Visualization"):
    # Create a PyVista PolyData object
    pv_mesh = pv.PolyData(mesh.vertices, mesh.faces)
    
    # Add the curvature values to the mesh as a point scalar
    pv_mesh.point_arrays["GaussCurvature"] = curvature_values
    
    # Plot the curvature with the color map
    plotter = pv.Plotter()
    plotter.add_mesh(pv_mesh, scalars="GaussCurvature", cmap="coolwarm", show_edges=True)
    plotter.add_title(title)
    plotter.show()
