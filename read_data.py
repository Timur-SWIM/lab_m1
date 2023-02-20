def reading_data():
    with open('rezult1.txt', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()  # прочтение файла с результами измерений
        result = [float(item) for item in lines]
        max_val = max(result)  # Наибольшее значение
        min_val = min(result)  # Наименьшее значение

    return result, max_val, min_val

def reading_data_3():
    with open('rezult3.txt', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
        result = [float(item) for item in lines]
    return result

def reading_data_4():
    with open('rezult4.txt', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
        result = [float(item) for item in lines]
    return result
