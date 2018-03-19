import random
import argparse
import os
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--model', dest='model_file', help='This is the address of model')
parser.add_argument('--seed', default='***', dest='First_Word', type=str, help='The First Word')
parser.add_argument('--output', default=sys.stdout, dest='output_file', help='this is the address of out')
parser.add_argument('--length', dest='Length', type=int, help='this is the length of text')

args = parser.parse_args()

# с помощью модели воссоздаю словарь словарей
file = open(args.model_file, 'r')
dic2 = {}
for line in file:
    tmp = list(line.split(' : '))
    tmp2 = list(tmp[1].split())
    dic2[tmp[0]] = {}
    for symb in tmp2:
        tmp3 = list(symb.split('*'))
        dic2[tmp[0]][tmp3[0]] = int(tmp3[1])
file.close()
# print(dic2)

# считываю длину текста и первое слово
Count = args.Length
str = args.First_Word
if args.First_Word == '***':
    List = []
    for symbol in dic2:
        List.append(symbol)
    str = random.choice(List)

file = open(args.output_file, 'w')

# генерирую текст
file.write(str)
file.write(' ')
while Count > 0 and str in dic2:
    List = []
    for keys, items in dic2[str].items():
        for i in range(items):
            List.append(keys)
    tmp = random.choice(List)
    file.write(tmp)
    file.write(' ')
    Count -= 1
    str = tmp
file.write('\n')
file.close()
