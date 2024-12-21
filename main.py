from courbure.gauss import gauss_curvature
from courbure.mean import calculate_mean_curvature
from courbure.max_curvature import CourbureMax
from courbure.min_cruvature import CourbureMin
from utils.visualize import visualize_curvature, visualize_mean_curvature
import trimesh

def main():
    # Load the 3D mesh
    mesh_path = "meshes/cow.obj"
    print(f"Loading mesh from: {mesh_path}")
    mesh = trimesh.load(mesh_path)
    points = mesh.vertices

    # Menu system
    while True:
        print("\n=== Choix des calculs de courbure ===")
        print("\n=== TP2_2024_Sameh_Aissa>python main.py ===")

        
        print("1. Calculer la courbure de Gauss")
        print("2. Calculer la courbure Moyenne")
        print("3. Calculer la courbure Maximale")
        print("4. Calculer la courbure Minimale")
        print("5. Quitter")
        choix = input("Entrez votre choix (1-5): ")

        if choix == "1":
            print("Calculating Gauss Curvature...")
            gauss_curv = gauss_curvature(mesh, points)

            # Visualize the results
            print("Visualizing Gauss Curvature...")
            visualize_curvature(mesh, gauss_curv, title="Courbure de Gauss")
        elif choix == "2":
            mean_curvature = calculate_mean_curvature(mesh)
            print("Courbure Moyenne calculée.")
            visualize_mean_curvature(mesh, mean_curvature)
        elif choix == "3":
            courbure_gauss = gauss_curvature(mesh, points)
            courbure_moyenne = calculate_mean_curvature(mesh)
            courbure_max = CourbureMax.calculer(courbure_moyenne, courbure_gauss)
            print("Courbure Maximale calculée.")
            visualize_curvature(mesh, courbure_max, title="Courbure Maximale")
        elif choix == "4":
            courbure_gauss = gauss_curvature(mesh, points)
            courbure_moyenne = calculate_mean_curvature(mesh)
            courbure_min = CourbureMin.calculer(courbure_moyenne, courbure_gauss)
            print("Courbure Maximale calculée.")
            visualize_curvature(mesh, courbure_min, title="Courbure Minimale")
        elif choix == "5":
            print("Quitter le programme. À bientôt!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
