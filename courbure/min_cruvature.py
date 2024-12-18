import numpy as np

class CourbureMin:
    @staticmethod
    def calculer(courbure_moyenne, courbure_gauss):
        kmin = courbure_moyenne - np.sqrt(np.maximum(0, courbure_moyenne**2 - courbure_gauss))
        return kmin
