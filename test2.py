'''
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial
เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว

'''


def n_zeros_trailing_factorial(n):
    if n == 0:
        return 0

    n_factor_5 = 0
    n_factor_2 = 0
    for i in range(n, 1, -1):
        x = i
        while x % 5 == 0:
            x /= 5
            n_factor_5 += 1
        while x % 2 == 0:
            x /= 2
            n_factor_2 += 1

    return min(n_factor_2, n_factor_5)
