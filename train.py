import re
import argparse
import os
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--model', dest='output_file', help='This is the address of model')
parser.add_argument('--input-dir', nargs='?', default=sys.stdin, dest='input_file', type=str, help='this is the address of input')
parser.add_argument('-ls', nargs='?', default=True, help='Low the text')


args = parser.parse_args()

# создаю словарь словарей из полученного текста

file = open(args.input_file, 'r')
dic = {}
last_word = '0'
for line in file:
    List = re.compile(u'[а-яa-zA-ZА-Я0-9-]+|[.,:;?!]+').findall(line)
    for word in List:
        if not args.ls:
            word = word.lower()
        if last_word == '0':
            dic[word] = {}
            # print("1 ", dic)
        else:
            if word not in dic[last_word]:
                dic[last_word][word] = 1
                # print("2 ", dic)
            else:
                dic[last_word][word] += 1
                # print("3 ", dic)
        if word not in dic:
            dic[word] = {}
        last_word = word
# print(dic)
file.close()

# создаю модель и записываю её в файл
file = open(args.output_file, 'w')
for symb in dic:
    file.write(symb)
    file.write(' : ')
    for subsymb in dic[symb]:
        file.write(subsymb)
        file.write('*')
        file.write(str(dic[symb][subsymb]))
        file.write(' ')
    file.write('\n')
file.close()





