# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
import sys
if sys.version[0] < 3:
    print('python version isn`t avaliable, only support python3+')
    exit()
'''

from libs import GensimWordVector, WordVector

import logging

logger = logging.getLogger('/ word2vec trainer / ')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

import argparse
parser = argparse.ArgumentParser('word2vec')
parser.add_argument('--gensim', action='store_true', help='use gensim to train')
parser.add_argument('--corpus', type=str, help='path of corpus to train')
parser.add_argument('--model', type=str, help='path of model to save')
args = parser.parse_args()

def main():
    if args.gensim:
        logger.info('use gensim.word2vec to train')
        wv = GensimWordVector()
    else:
        logger.info('use default word2vec to train')
        wv = WordVector()

    logger.info('start to train / corpus path :' + args.corpus)
    wv.train(args.corpus, args.model)
    logger.info('finish! / save model in :' + args.model)

if __name__ == '__main__':
    main()