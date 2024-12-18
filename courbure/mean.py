import numpy as np

class CourbureMoyenne:
    @staticmethod
    def calculer(mesh):
        # Get the vertex normals (approximated surface normals)
        vertex_normals = mesh.vertex_normals

        # Get the face areas
        face_areas = mesh.area_faces
        
        # Initialize vertex area sums and mean curvature values
        vertex_areas = np.zeros(len(mesh.vertices))
        mean_curvatures = np.zeros(len(mesh.vertices))

        # Distribute face areas to vertices (Weighted average)
        for i, face in enumerate(mesh.faces):
            for vertex in face:
                vertex_areas[vertex] += face_areas[i] / 3.0

        # Calculate mean curvature by the change in normals
        for i, face in enumerate(mesh.faces):
            vertices = mesh.vertices[mesh.faces[i]]
            for vertex in face:
                # The mean curvature for each vertex can be approximated
                # by the difference of normals of neighboring faces
                normal_diff = np.linalg.norm(vertex_normals[face[0]] - vertex_normals[face[1]])  # Example diff, modify for neighbors
                mean_curvatures[vertex] += normal_diff / vertex_areas[vertex]  # Weight by area
        
        return mean_curvatures
