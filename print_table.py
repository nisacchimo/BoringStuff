#! python3
# -*- coding: utf-8 -*-

# 演習プロジェクト 6.7.1

def print_table(table_data):
    col_n = len(table_data) #col_n=3
    row_n = len(table_data[0]) #row_n=4

    col_width = [0] * col_n #[0,0,0]
    for c in range(col_n): #3回繰り返すループ
        for row in table_data[c]: #データの*列目
            col_width[c] = max(col_width[c], len(row)) #*列目の値の最大の長さを調べる(col_width[c]と len(row)どっちが大きいかを調べて大きい方をcol_width[c]へ代入)

    #print(col_width) [8,5,5]

    for r in range(row_n): #4回繰り返すループ
        for c in range(col_n): #3回繰り返すループ
            print(table_data[c][r].rjust(col_width[c]), end=' ') #applesを8文字右づめ、Aliceを5文字右づめ、dogsを5文字右づめ、改行なし
        print() #改行



table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)
