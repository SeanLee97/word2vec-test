# !/usr/bin/env python
# -*- coding: utf-8 -*-

import word2vec

import os, codecs
import numpy as np

class WordVector(object):
    def __init__(self):
        self.model = None
        self.model_path = None

    def set_model_path(self, model_path):
        self.model_path = model_path

    def train(self, train_path, model_path):
        global word2vec
        self.model_path = model_path
        word2vec.word2vec(train_path, model_path, verbose=True)

    def load(self):
        if self.model != None:
            return self.model

        if self.model_path == None:
            raise ValueError('Please set word2vec model file')
        if not os.path.exists(self.model_path):
            raise ValueError('Can`t find trained word2vec model file')

        global word2vec
        self.model = word2vec.load(self.model_path)
        return self.model

    def word_embedding(self, word):
        # load model
        self.load()
        
        if word in self.model.vocab:
            return self.model[word]
        else:
            return []

    def sentence_embedding(self, vocabs, unknown_avg=False):
        # load model
        self.load()

        word2vec_numpy = list()
        for word in vocabs:
            if word in self.model.vocab:
                word2vec_numpy.append(self.model[word].tolist())
        embed_size = len(word2vec_numpy[0])

        if unknown_avg is True:
            col = []
            for i in range(embed_size):
                count = 0.0
                for j in range(int(len(word2vec_numpy))):
                    count += word2vec_numpy[j][i]
                    count = round(count, 6)
                col.append(count)
            zero = []
            for m in range(embed_size):
                avg = col[m] / (len(word2vec_numpy))
                avg = round(avg, 6)
                zero.append(float(avg))

        list_word2vec = []
        oov = 0
        iov = 0
        for word in vocabs:
            if word not in self.model.vocab:
                oov += 1
                if unknown_avg is True:
                    wv = zero
                else:
                    wv = np.random.uniform(-0.25, 0.25, embed_size).round(6).tolist()
            else:
                iov += 1
                wv = self.model[word].tolist()
            list_word2vec.append(wv)
        return list_word2vec, embed_size
