def spam():
    global eggs
    eggs = "spam" #グローバル変数

def bacon():
    eggs = "bacon" #ローカル変数

def ham():
    print(eggs) #グローバル変数

eggs = 42 #グローバル変数
spam()
print(eggs)
