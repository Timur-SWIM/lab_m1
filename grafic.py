from matplotlib import pyplot as plt
def hist(result, max_val, min_val, X_, sigma):

    max_val = round(max_val - max_val % 0.05 + 0.05, 2)  # округленные диапазоны
    min_val = round(min_val - min_val % 0.05 - 0.05, 2)

    range_val = []              # колличество бинов
    i = min_val
    while i != (max_val + 0.05):
        range_val.append(i)
        i = round(i + 0.05,2)

    x, y = range_val, result

    fig, ax = plt.subplots(figsize=(10, 7), tight_layout=True)
    ax.hist(y, bins = x, label="Наибольшее значение:" + str(max_val) + "\nНаименьшее значение:" + str(min_val))
    plt.axvline(X_ - sigma, ymin=0, color='red', label="X\u00AF=" + str(X_ - sigma))
    plt.axvline(X_, ymin=0, color='b', label="X\u00AF=" + str(X_))
    plt.axvline(X_ + sigma, ymin=0, color='red', label="X\u00AF=" + str(X_ + sigma))
    plt.grid(True, color='grey',
             linestyle='-', linewidth=1,
             alpha=0.8)
    plt.xlabel('Xi')
    plt.ylabel('N')
    plt.title('Маятник 1')
    ax.text(1.9, 8, r'$ \sigma=$' + str(sigma), fontsize=16)
    plt.legend()

    plt.show()
