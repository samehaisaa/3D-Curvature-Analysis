import numpy as np
import trimesh

class CourbureGauss:
    @staticmethod
    def calculer(mesh):
        # Initialize the Gauss curvature array
        gauss_curvature = np.zeros(len(mesh.vertices))
        
        # Loop through each vertex and compute Gauss curvature
        for i, vertex in enumerate(mesh.vertices):
            # Get the neighboring faces of the current vertex
            vertex_faces = mesh.vertex_faces[i]
            if len(vertex_faces) < 2:
                # Skip if not enough neighbors to calculate curvature
                continue
            
            # Calculate the vertex normal
            vertex_normal = mesh.vertex_normals[i]
            
            # Compute the area of the surrounding faces
            face_areas = [mesh.area_faces[face] for face in vertex_faces]
            
            # Calculate Gauss curvature based on angle defects between neighboring faces
            angle_sum = 0
            for face in vertex_faces:
                # Get the three vertices of the face
                face_vertices = mesh.vertices[mesh.faces[face]]
                # Compute the angle defect (this is a simplified approach)
                normal1 = mesh.face_normals[face]
                for other_face in vertex_faces:
                    if face != other_face:
                        normal2 = mesh.face_normals[other_face]
                        # Calculate angle between normals
                        angle = np.arccos(np.clip(np.dot(normal1, normal2), -1.0, 1.0))
                        angle_sum += angle
            
            # Compute the Gauss curvature by dividing the angle defect by the area of the Voronoi cell
            # (area around the vertex)
            gauss_curvature[i] = angle_sum / np.sum(face_areas)
        
        return gauss_curvature
