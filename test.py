# !/usr/bin/env python
# -*- coding: utf-8 -*-

from libs import GensimWordVector, WordVector

word = '中国'
sentence = '我 生活 在 中国'

# 1. gensim
wv = GensimWordVector()
wv.set_model_path('./model/w2v.gensim.bin')
# 1.1 获取词向量
print(word, 'embedding:')
print(wv.word_embedding(word))
# 1.2 获取句子向量
print(sentence, 'embedding:')
embed, embed_size = wv.sentence_embedding(sentence.split())
print(embed)


# 2. word2vec
wv = WordVector()
wv.set_model_path('./model/w2v.bin')
# 2.1 获取词向量
print(word, 'embedding:')
print(wv.word_embedding(word))
# 2.2 获取句子向量
print(sentence, 'embedding:')
embed, embed_size = wv.sentence_embedding(sentence.split())
print(embed)
