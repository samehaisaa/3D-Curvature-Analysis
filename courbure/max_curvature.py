import numpy as np

class CourbureMax:
    @staticmethod
    def calculer(courbure_moyenne, courbure_gauss):
        kmax = courbure_moyenne + np.sqrt(np.maximum(0, courbure_moyenne**2 - courbure_gauss))
        return kmax
