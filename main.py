from courbure.gauss import CourbureGauss
from courbure.mean import CourbureMoyenne
from courbure.max_curvature import CourbureMax
from courbure.min_cruvature import CourbureMin
from utils.visualize import visualize_curvature
import trimesh

def main():
    # Load the 3D mesh
    mesh_path = "meshes/cow.obj"
    print(f"Loading mesh from: {mesh_path}")
    mesh = trimesh.load(mesh_path)

    # Menu system
    while True:
        print("\n=== Choix des calculs de courbure ===")
        print("1. Calculer la courbure de Gauss")
        print("2. Calculer la courbure Moyenne")
        print("3. Calculer la courbure Maximale")
        print("4. Calculer la courbure Minimale")
        print("5. Quitter")
        choix = input("Entrez votre choix (1-5): ")

        if choix == "1":
            courbure_gauss = CourbureGauss.calculer(mesh)
            print("Courbure de Gauss calculée.",courbure_gauss)
            print("courbure gauss shape : ", courbure_gauss.shape)
            visualize_curvature(mesh, courbure_gauss, title="Courbure de Gauss")
        elif choix == "2":
            courbure_moyenne = CourbureMoyenne.calculer(mesh)
            print("Courbure Moyenne calculée.")
            visualize_curvature(mesh, courbure_moyenne, title="Courbure Moyenne")
        elif choix == "3":
            courbure_gauss = CourbureGauss.calculer(mesh)
            courbure_moyenne = CourbureMoyenne.calculer(mesh)
            courbure_max = CourbureMax.calculer(courbure_moyenne, courbure_gauss)
            print("Courbure Maximale calculée.")
            visualize_curvature(mesh, courbure_max, title="Courbure Maximale")
        elif choix == "4":
            courbure_gauss = CourbureGauss.calculer(mesh)
            courbure_moyenne = CourbureMoyenne.calculer(mesh)
            courbure_min = CourbureMin.calculer(courbure_moyenne, courbure_gauss)
            print("Courbure Minimale calculée.")
            visualize_curvature(mesh, courbure_min, title="Courbure Minimale")
        elif choix == "5":
            print("Quitter le programme. À bientôt!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
