# subtask 4
def max_num():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))

    if a > b:
        res = a
    else:
        res = b

    if res < c:
        res = c

    print("max_num: %s" % res)


# subtask 9
def elephant():
    a0 = int(input("a0="))
    a1 = int(input("a1="))
    b0 = int(input("b0="))
    b1 = int(input("b1="))

    if (a0 == b0):
        return print("NO")
    k = (b1 - a1) // (b0 - a0)
    if (k == 1 or k == -1):
        print("YES")
    else:
        print("NO")


# subtask 10
def is_equal():
    a0 = int(input("a0="))
    a1 = int(input("a1="))
    b0 = int(input("b0="))
    b1 = int(input("b1="))

    if (a0 % 2 == a1 % 2) and (b0 % 2 == b1 % 2):
        print("YES")
    else:
        print("NO")


# subtask 11
def equation():
    a = int(input("a="))
    b = int(input("b="))

    if (a == 0 or b % a != 0):
        print("NO")
    elif (a == 0 and b == 0):
        print("INF")
    else:
        print(-b // a)


# subtask 12
def metro():
    tickets_q = [1, 5, 10, 20, 60]
    tickets_p = {1: 15, 5: 70, 10: 125, 20: 230, 60: 440}
    n = int(input("n="))
    # n: int = 156
    remainder: int = n
    min_price: int = 0

    tmp_str = ""
    item = len(tickets_q) - 1
    while remainder != 0:
        if n >= tickets_q[item]:
            tmp_val = remainder // tickets_q[item]
            if tmp_val > 0:
                min_price += tmp_val * tickets_p[tickets_q[item]]
                tmp_str += f"{remainder // tickets_q[item]}x{tickets_q[item]}={tmp_val * tickets_p[tickets_q[item]]}rub, "
            remainder = (lambda x, y: x % y)(n, tickets_q[item])
        item -= 1

    for i in reversed(range(len(tickets_q))):
        if n < tickets_q[i]:
            tmp_price = tickets_p[tickets_q[i]]
            if tmp_price < min_price:
                min_price = tmp_price
                tmp_str = f"1x{tickets_p[tickets_q[i]]}={min_price}, "

    print(f"{tmp_str}total of: {min_price}rub")


# subtask 13
def steaks():
    k = int(input("k="))
    m = int(input("m=")) * 2
    n = int(input("n="))

    if (n % k != 0):
        res = (n // k + 1) * m
    else:
        res = n // k * m
    print("minimum: %s min" % res)


# subtask 16
def natural_odd():
    n = int(input("n="))
    res = 1
    for i in range(n):
        res *= 10

    for i in range(res):
        tmp_num = res - i
        if (i % 2 == 0):
            continue
        elif (tmp_num < res//10):
            break
        print(tmp_num)


# subtask 17
def squares_summ():
    n = int(input("n=")) + 1
    res = 0

    for i in range(n):
        res += i ** 2

    print("summ=%s" % res)


# max_num()
# elephant()
# is_equal()
# equation()
metro()
# steaks()
# squares_summ()
# natural_odd()
