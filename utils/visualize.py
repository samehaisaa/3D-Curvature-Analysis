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

void visualize_curvature(vtkSmartPointer<vtkPolyData> mesh, std::vector<float> curvature_values, const std::string &title = "Courbure") {
    if (curvature_values.size() != mesh->GetNumberOfPoints()) {
        std::cerr << "Error: Number of curvature values does not match the number of mesh vertices!" << std::endl;
        return;
    }

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

    vtkSmartPointer<vtkActor> actor = vtkSmartPointer<vtkActor>::New();
    actor->SetMapper(mapper);

    vtkSmartPointer<vtkRenderer> renderer = vtkSmartPointer<vtkRenderer>::New();
    vtkSmartPointer<vtkRenderWindow> renderWindow = vtkSmartPointer<vtkRenderWindow>::New();
    renderWindow->AddRenderer(renderer);

    vtkSmartPointer<vtkRenderWindowInteractor> renderWindowInteractor = vtkSmartPointer<vtkRenderWindowInteractor>::New();
    renderWindowInteractor->SetRenderWindow(renderWindow);

    renderer->AddActor(actor);
    renderer->SetBackground(0.1, 0.1, 0.1);

    renderWindow->Render();
    renderWindowInteractor->Start();
}
