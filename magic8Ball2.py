import random

messages  = ["確かにそうだ",
             "間違いなくそうだ",
             "はい",
             "なんとも、もう一度やってみて",
             "あとでもう一度きいてみて",
             "集中してもう一度きいてみて",
             "私の答えはノーです",
             "見通しはそれほどよくない",
             "とても疑わしい"]

print(messages[random.randint(0,len(messages)-1)])
