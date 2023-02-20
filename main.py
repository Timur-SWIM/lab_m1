from grafic import hist
from read_data import reading_data, reading_data_3, reading_data_4
from writing_data import write_data_b, write_data_v, write_data_3, write_data_4, write_data_g
from calculator import math, math_2, math_3, math_4

def main():

    result, max_val, min_val = reading_data()
    X_, sigma, procent, sigma_x, dov_int, E, d_x = math(result)

    hist(result, max_val, min_val, X_, sigma)
    write_data_b(result, X_, sigma, procent, sigma_x, dov_int, E)

    X_, dov_int = math_2(reading_data_3())
    write_data_v(d_x, X_, dov_int)

    write_data_3(reading_data_3())
    write_data_4(reading_data_4())

    dov_int_3 = math_3(reading_data_3())
    X_, dov_int_4_1, dov_int_4_2 = math_4(reading_data_4())
    write_data_g(dov_int_3, X_, dov_int_4_1, dov_int_4_2)

if __name__ == '__main__':
    main()
