def write_data_b(result, X_, sigma, procent, sigma_x, dov_int, E):
    delta_x = [round((result[i] - X_), 3) for i in range(len(result))]
    delta_x2 = [round((result[i] - X_) ** 2, 5) for i in range(len(result))]

    with open('/Users/mac/Desktop/Project/Python_code/physics/b2.1.txt', 'w', encoding='utf-8') as outfile:
        for i in range(len(delta_x)):
            outfile.write(str(delta_x[i]) + "\n")

    with open('b2.2.txt', 'w', encoding='utf-8') as outfile:
        for i in range(len(delta_x2)):
            outfile.write(str(delta_x2[i]) + "\n")

    with open('b.txt', 'w', encoding='utf-8') as outfile:
        outfile.write('σ =' + str(sigma) + '\n')
        outfile.write("процент результатов измерений, попавший в заштрихованную часть:"
                      + str(procent) + '%' + '\n')
        outfile.write('σx ̄ = ' + str(sigma_x) + '\n')
        outfile.write('полуширина доверительного интервала ∆x ̄=' + str(dov_int) + '\n')
        outfile.write('относительная погрешность:' + str(E) + '%')

def write_data_v(d_x, X_, dov_int):
    with open('v.txt', 'w', encoding='utf-8') as outfile:
        outfile.write('вычислить полуширину доверительного '
                      'интервала \nслучайной погрешности '
                      'единичного измерения ∆x = kσ =' + str(d_x))
        outfile.write('x ̄ для n = 4' + str(X_) + '\n')
        outfile.write('По формуле (13) определить \n'
                      'полуширину доверительного '
                      'интервала для P = 0.95.' + str(dov_int) + '\n')

def write_data_3(result):
    X_ = round(((sum(result)) / len(result)), 2)
    delta_x = [round((result[i] - X_), 3) for i in range(len(result))]
    delta_x2 = [round((result[i] - X_) ** 2, 5) for i in range(len(result))]

    with open('/Users/mac/Desktop/Project/Python_code/physics/m3.1.txt', 'w', encoding='utf-8') as outfile:
        for i in range(len(delta_x)):
            outfile.write(str(delta_x[i]) + "\n")

    with open('m3.2.txt', 'w', encoding='utf-8') as outfile:
        for i in range(len(delta_x2)):
            outfile.write(str(delta_x2[i]) + "\n")


def write_data_4(result):
    X_ = round(((sum(result)) / len(result)), 2)
    delta_x = [round((result[i] - X_), 3) for i in range(len(result))]
    delta_x2 = [round((result[i] - X_) ** 2, 5) for i in range(len(result))]

    with open('/Users/mac/Desktop/Project/Python_code/physics/m4.1.txt', 'w', encoding='utf-8') as outfile:
        for i in range(len(delta_x)):
            outfile.write(str(delta_x[i]) + "\n")

    with open('m4.2.txt', 'w', encoding='utf-8') as outfile:
        for i in range(len(delta_x2)):
            outfile.write(str(delta_x2[i]) + "\n")

