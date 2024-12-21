#include <vtkSmartPointer.h>
#include <vtkPolyData.h>
#include <vtkCellArray.h>
#include <vtkPoints.h>
#include <vtkFloatArray.h>
#include <vtkPolyDataMapper.h>
#include <vtkActor.h>
#include <vtkRenderer.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkLookupTable.h>
#include <vtkXMLPolyDataReader.h>
#include <vtkNamedColors.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

<<<<<<< HEAD
void visualize_curvature(vtkSmartPointer<vtkPolyData> mesh, std::vector<float> curvature_values, const std::string &title = "Courbure") {
    if (curvature_values.size() != mesh->GetNumberOfPoints()) {
        std::cerr << "Error: Number of curvature values does not match the number of mesh vertices!" << std::endl;
        return;
    }
=======
def visualize_curvature(mesh, curvature_values, title):
    """
    Visualize curvature values on the 3D mesh using PyVista.
    :param mesh: Trimesh object
    :param curvature_values: Array of curvature values (one per vertex)
    :param title: Title of the visualization
    """
    # Convert Trimesh to PyVista format
    faces = mesh.faces
>>>>>>> cb7e9a441a7730e727d5366975c119544c57330a

    vtkSmartPointer<vtkFloatArray> curvatureArray = vtkSmartPointer<vtkFloatArray>::New();
    curvatureArray->SetName(title.c_str());
    for (size_t i = 0; i < curvature_values.size(); ++i) {
        curvatureArray->InsertNextValue(curvature_values[i]);
    }
    mesh->GetPointData()->AddArray(curvatureArray);

    vtkSmartPointer<vtkLookupTable> lookupTable = vtkSmartPointer<vtkLookupTable>::New();
    lookupTable->SetNumberOfTableValues(256);
    lookupTable->Build();

    for (int i = 0; i < 256; ++i) {
        lookupTable->SetTableValue(i, i / 255.0, 0.0, 1.0 - i / 255.0);
    }

    vtkSmartPointer<vtkPolyDataMapper> mapper = vtkSmartPointer<vtkPolyDataMapper>::New();
    mapper->SetInputData(mesh);
    mapper->SetLookupTable(lookupTable);
    mapper->SetScalarModeToUsePointData();
    mapper->SetScalarRange(*std::min_element(curvature_values.begin(), curvature_values.end()),
                           *std::max_element(curvature_values.begin(), curvature_values.end()));

<<<<<<< HEAD
    vtkSmartPointer<vtkActor> actor = vtkSmartPointer<vtkActor>::New();
    actor->SetMapper(mapper);
=======
    # Create a plotter
    plotter = pv.Plotter()
    plotter.add_mesh(pv_mesh, scalars=title, cmap="viridis", show_edges=True)
    plotter.add_title(title, font_size=16)
    plotter.show()
>>>>>>> cb7e9a441a7730e727d5366975c119544c57330a

    vtkSmartPointer<vtkRenderer> renderer = vtkSmartPointer<vtkRenderer>::New();
    vtkSmartPointer<vtkRenderWindow> renderWindow = vtkSmartPointer<vtkRenderWindow>::New();
    renderWindow->AddRenderer(renderer);

    vtkSmartPointer<vtkRenderWindowInteractor> renderWindowInteractor = vtkSmartPointer<vtkRenderWindowInteractor>::New();
    renderWindowInteractor->SetRenderWindow(renderWindow);

<<<<<<< HEAD
    renderer->AddActor(actor);
    renderer->SetBackground(0.1, 0.1, 0.1);

    renderWindow->Render();
    renderWindowInteractor->Start();
}
=======
def visualize_mean_curvature(mesh, mean_curvature):
    """
    Visualize the mean curvature on the mesh by coloring the vertices.
    
    Parameters:
    - mesh: Trimesh object containing the 3D mesh.
    - mean_curvature: A numpy array of mean curvature values for each vertex.
    """
    # Normalize the curvature values for visualization
    normalized_curvature = (mean_curvature - mean_curvature.min()) / (mean_curvature.max() - mean_curvature.min())
    
    # Map the curvature values to a colormap (you can adjust this as needed)
    colormap = plt.cm.plasma(normalized_curvature)
    
    # Apply the colormap to the vertices
    mesh.visual.vertex_colors = (colormap[:, :3] * 255).astype(np.uint8)
    # Show the mesh with curvature visualization
    mesh.show()
>>>>>>> cb7e9a441a7730e727d5366975c119544c57330a
