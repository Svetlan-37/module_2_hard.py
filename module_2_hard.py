import random
box = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20]
number = random.choice(box)


def psw(number):
    result = ' '
    for i in range(1, 21):
        for j in range(1+i, 21):
            if i+j > number:
                break
            elif number % (i+j) == 0:
                result += str(i) + str(j)
    return result


print('Случайное число: ', number, ',', 'пароль: ', psw(number))
