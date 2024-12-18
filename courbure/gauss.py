import numpy as np
import trimesh
from tqdm import tqdm  # Progress bar

class CourbureGauss:
    @staticmethod
    def calculer(mesh):
        # Initialize the Gauss curvature array
        gauss_curvature = np.zeros(len(mesh.vertices))

        # Precompute vertex normals and face areas
        vertex_normals = mesh.vertex_normals
        face_areas = mesh.area_faces
        
        # Loop through the faces to compute curvature
        for i in tqdm(range(len(mesh.faces)), desc="Calculating Gauss Curvature", unit="face"):
            face = mesh.faces[i]
            # Get the three vertices of the face
            v0, v1, v2 = mesh.vertices[face]
            
            # Compute the area of the face using the cross product of two edges
            edge1 = v1 - v0
            edge2 = v2 - v0
            face_area = np.linalg.norm(np.cross(edge1, edge2)) / 2
            
            # Compute the normal of the face
            face_normal = np.cross(edge1, edge2)
            face_normal /= np.linalg.norm(face_normal)
            
            # Compute the angle defects for each vertex in the face
            for j in range(3):
                vertex = face[j]
                # Get the neighboring faces for the current vertex
                vertex_faces = mesh.vertex_faces[vertex]
                
                # Compute angle defect at the vertex (simplified method)
                angle_sum = 0
                for neighbor_face in vertex_faces:
                    if neighbor_face != i:  # Ignore the current face
                        neighbor_normal = mesh.face_normals[neighbor_face]
                        # Compute the angle between face normals
                        angle = np.arccos(np.clip(np.dot(face_normal, neighbor_normal), -1.0, 1.0))
                        angle_sum += angle
                
                # Store the Gauss curvature for the vertex
                gauss_curvature[vertex] += angle_sum / face_area

        return gauss_curvature

