def commma(data):
    data.insert(len(data)-1,"and")
    for i in data:
        print(i + " ",end ="")
spam = ["apples","bananas","tofu","cats"]
commma(spam)
