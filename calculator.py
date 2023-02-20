def math(result):
    X_ = round(((sum(result)) / len(result)), 2)
    delta_x = [round((result[i] - X_), 2) for i in range(len(result))]
    delta_x2 = [round((result[i] - X_) ** 2, 3) for i in range(len(result))]
    sigma = round((sum(delta_x2) / 49) ** 0.5, 2)

    n = 0
    for i in range(len(result)):
        if (X_ - sigma) <= result[i] <= (X_ + sigma):
            n+=1
    procent = (n / len(result) * 100)  # процент результатов измерений  (Б.4)

    sigma_x = round((sigma / (len(result)) ** 0.5),3)           # вычислить σx ̄ (Б.5)
    dov_int = round((2 * sigma_x), 3)                            # полуширина доверительного интервала ∆x ̄
    E = round((dov_int / X_) * 100, 3)               # относительная погрешность

    d_x = 2 * sigma                                  # ∆x = kσ

    return X_, sigma, procent, sigma_x, dov_int, E, d_x
def math_2(result):
    X_ = round(((sum(result)) / len(result)), 2)
    delta_x = [round((result[i] - X_), 2) for i in range(len(result))]
    delta_x2 = [round((result[i] - X_) ** 2, 3) for i in range(len(result))]
    sigma = round((sum(delta_x2) / 49) ** 0.5, 2)
    sigma_x = round((sigma / (len(result)) ** 0.5), 3)
    dov_int = round((2 * sigma_x), 3)
    return X_, dov_int

def math_3(result):
    X_ = round(((sum(result)) / len(result)), 2)
    delta_x2 = [round((result[i] - X_) ** 2, 3) for i in range(len(result))]
    dov_int = round((5.84 * ((sum(delta_x2)/12) ** 0.5)), 3)
    return dov_int

def math_4(result):
    X_ = round(((sum(result)) / len(result)), 2)
    delta_x2 = [round((result[i] - X_) ** 2, 3) for i in range(len(result))]
    dov_int1 = round((2 * ((sum(delta_x2)/(12 * 11)) ** 0.5)), 3)
    dov_int2 = round((1 * ((sum(delta_x2)/(12 * 11)) ** 0.5)), 3)
    return X_, dov_int1, dov_int2
