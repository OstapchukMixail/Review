import random
import argparse
import os
import sys
import pickle
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('--model', dest='model_file', help='This is the address of model')
parser.add_argument('--seed', default='***', dest='First_Word', type=str, help='The First Word')
parser.add_argument('--output', default=sys.stdout, dest='output_file', help='this is the address of out')
parser.add_argument('--length', dest='Length', type=int, help='this is the length of text')


def dd():
    return defaultdict(int)


def model_in(args):

    # с помощью модели воссоздаю словарь словарей
    dic2 = {}
    with open(args.model_file, 'rb') as file:
        dic2 = pickle.load(file)
    return dic2


def In_Generation_Out(args, dic2):

    # считываю длину текста и первое слово
    Count = args.Length
    words = args.First_Word
    if args.First_Word == '***':
        List = []
        for symbol in dic2:
            List.append(symbol)
        words = random.choice(List)
    file = open(args.output_file, 'w')

    # генерирую текст
    file.write(words)
    file.write(' ')
    while Count > 0 and words in dic2:
        Sum = sum(int(i) for i in dic2[words].values())
        Listk = [
            int(i) / Sum
            for i in dic2[words].values()
        ]
        tmp = np.random.choice(list(dic2[words].keys()), p=Listk)
        file.write(tmp)
        file.write(' ')
        Count -= 1
        words = tmp
    file.write('\n')
    file.close()


args = parser.parse_args()
In_Generation_Out(args, model_in(args))
