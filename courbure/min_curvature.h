#ifndef COURBUREMAX_H
#define COURBUREMAX_H

#include <vector>
#include <cmath>

class CourbureMax {
public:
    static std::vector<double> calculer(const std::vector<double>& courbure_moyenne, const std::vector<double>& courbure_gauss) {
        std::vector<double> kmax(courbure_moyenne.size());

        for (size_t i = 0; i < courbure_moyenne.size(); ++i) {
            kmax[i] = courbure_moyenne[i] - std::sqrt(std::max(0.0, courbure_moyenne[i] * courbure_moyenne[i] - courbure_gauss[i]));
        }

        return kmax;
    }
};

#endif // COURBUREMAX_H
