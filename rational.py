from math import gcd


def get_rational(expr_temp):
    list_dig =[]
    list_operator = []
    list_one_num = []
    znak = 1

    if expr_temp[0]=='-':
        znak = -1
        expr = expr_temp[1:]
    else:expr = expr_temp

    dict_op = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               ':': lambda x, y: x * y,
               }

    for oper in dict_op:
        expr = expr.replace(oper, f'#{oper}#')

    temp = expr.split('#')


    for i in range(len(temp)):
        list_one_num.append(temp[i]) if not i%2 else list_operator.append(temp[i])

    for i in list_one_num:
        list_temp = list(map(int,i.split("/")))
        list_dig.append([(list_temp[0]*list_temp[2]+list_temp[1]),list_temp[2]])

    list_dig[0][0]*=znak

    temprory = 0
    while '*' in list_operator or ':' in list_operator:
        for i in range(len(list_operator)):
            if list_operator[i]=='*' or list_operator[i]==':':
                if list_operator[i]==':': temprory =1
                new_chis = (dict_op[list_operator[i]])(list_dig[i][0], list_dig[i+1][0+temprory])
                new_znam = (dict_op[list_operator[i]])(list_dig[i][1], list_dig[i+1][1-temprory])
                temp_res = [new_chis,new_znam]
                list_dig.pop(i)
                list_dig.pop(i)
                list_dig.insert(i, temp_res)
                list_operator.pop(i)
                break

    while len(list_operator)!=0:

        znam_first = list_dig[0][1]
        znam_second = list_dig[1][1]

        list_dig[0][0]*= znam_second
        list_dig[0][1]*= znam_second

        list_dig[1][0]*= znam_first
        list_dig[1][1]*= znam_first

        new_chis = (dict_op[list_operator[0]])(list_dig[0][0],list_dig[1][0])
        temp_res = [new_chis,list_dig[0][1]]

        list_operator.pop(0)
        list_dig.pop(0)
        list_dig.pop(0)
        list_dig.insert(0, temp_res)

    nod = gcd(list_dig[0][0], list_dig[0][1])

    res_chis = int(list_dig[0][0]/nod)
    res_znam = int(list_dig[0][1]/nod)

    print(f'Ответ: {res_chis}/{res_znam}') if res_chis<res_znam else \
        print(f'Ответ: {res_chis}/{res_znam} или {res_chis//res_znam} целых и {res_chis-(res_chis//res_znam)*res_znam}/{res_znam}')

get_rational('1/2/3+2/1/2')


