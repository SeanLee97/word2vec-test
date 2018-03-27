# word2vec-test
word2vec 的训练及使用

## 依赖库
```
word2vec
gensim
```
## 安装依赖库
```
pip3 install -r requirements.txt
```

## 如何训练
###  使用gensim包训练

```
python3 trainer.py --corpus /path/to/corpus --model /path/to/model --gensim
```

参数说明

1. corpus： 指定训练语料路径（确保语料分好词，且用空格分割）
2. model ： 指定模型保存目录
3. gensim： 使用gensim训练

### 使用word2vec包
```
python3 trainer.py --corpus /path/to/corpus --model /path/to/model
```

参数说明

1. corpus： 指定训练语料路径（确保语料分好词，且用空格分割）
2. model ： 指定模型保存目录

## 如何获取词向量、句向量

详情请参照 `test.py` 文件

## Refrence

1. [gensim word2vec用法文档](https://radimrehurek.com/gensim/models/word2vec.html)
2. [word2vec 用法文档](http://nbviewer.jupyter.org/github/danielfrg/word2vec/blob/master/examples/word2vec.ipynb)