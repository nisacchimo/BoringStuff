def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print("不正な値です")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
