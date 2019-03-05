def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print("好きな番号を入力してください")
try:
    select_number = int(input())
    while select_number != 1:
        select_number =collatz(select_number)
        print(select_number)
except ValueError:
    print("整数を入力してください")
