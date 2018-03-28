import re
import argparse
import os
import sys
import pickle
import collections


parser = argparse.ArgumentParser()
parser.add_argument('--model', dest='output_file', help='This is the address of model')
parser.add_argument('--input-dir', nargs='?', default=sys.stdin, dest='input_path', type=str, help='this is the address of input')
parser.add_argument('--lc', nargs='?', default=True, help='Low the text')


def creation(args):
    dic = collections.defaultdict(dict)
    List = os.listdir(path=args.input_path)
    for files in List:
        with open(os.path.join(args.input_path, files), 'r') as file:    # соединяю путь к файлу и путь к его директории
            last_word = 'something_that_isnot_important'
            flag_lw = False
            for line in file:
                List = re.compile(u'[а-яa-zA-ZА-Я0-9-]+|[.,:;?!]+').findall(line)
                for word in List:
                    if not args.lc:
                        word = word.lower()
                    if flag_lw:
                        if word not in dic[last_word]:
                            dic[last_word][word] = 1
                        else:
                            dic[last_word][word] += 1
                    else:
                        flag_lw = True
                    last_word = word
    return dic


def model_out(args, dic):
    with open(args.output_file, 'wb') as file:
        pickle.dump(dic, file)


args = parser.parse_args()
model_out(args, creation(args))
