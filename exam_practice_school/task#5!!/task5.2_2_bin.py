#строится восьмибитная запись числа н
# инвертируются все разряды двоичного числа
# полученное число переводится в дестичную систему счисления
# выводится результат разности исходног и нового

for n in range(1, 256):
    r=bin(n)[2:]
    #строится восьмибитная запись числа н
    r=(8-len(r)) * "0" + r

    #инвертируются все разряды двоичного числа
    s = ""
    for i in r:
        if i=="1":
            s+="0"
        else:
            s+="1"

    if int(s, 2) - n == 99:
        print(n)


