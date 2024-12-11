from random import randint

x = randint(1, 100)
print(x)
user_num = 0
attempt = 0
while True:
    print("я загадал число от 1 до 100, попробуй угадать")
    user_num = int(input("ваше число:  "))
    attempt += 1
    if user_num == x:
        print("Угадал! \nКоличество попыток:"+ str(attempt))
        break
    elif user_num > x:
        print("Загаданое число меньше этого")
    elif user_num < x:
        print("Загаданое число больше этого")