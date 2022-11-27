# -*- coding:utf-8 -*-
import json
# import flask
import pickle
import numpy as np
from gevent import pywsgi
import tensorflow as tf 
import keras
from keras.backend.tensorflow_backend import set_session
from bert4keras.backend import keras
from bert4keras.tokenizers import Tokenizer
from bert4keras.snippets import sequence_padding

import sys
sys.path.append("..")
import bert_intent_recognition.bert_model

global graph,model,sess 


config = tf.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)
graph = tf.get_default_graph()
set_session(sess)

class BertIntentModel(object):
    def __init__(self):
        super(BertIntentModel, self).__init__()
        self.config_path = 'F:/AI_tutor/bert_model/wwm_uncased_L-24_H-1024_A-16/bert_config.json'
        self.checkpoint_path = 'F:/AI_tutor/bert_model/wwm_uncased_L-24_H-1024_A-16/bert_model.ckpt'
        self.dict_path = 'F:/AI_tutor/bert_model/wwm_uncased_L-24_H-1024_A-16/vocab.txt'
        #把所有的label都读进去
        self.label_list = [line.strip() for line in open('F:/AI_tutor/bert_intent_recognition/data/label','r',encoding='utf8')]
        self.id2label = {idx:label for idx,label in enumerate(self.label_list)}

        self.tokenizer = Tokenizer(self.dict_path)
        self.model = bert_intent_recognition.bert_model.build_bert_model(self.config_path,self.checkpoint_path,11)
        self.model.load_weights('F:/AI_tutor/bert_intent_recognition/checkpoint1/best_model.weights')

    def predict(self,text):
        # tokenizer.encode 相当于把embedding
        token_ids, segment_ids = self.tokenizer.encode(text, maxlen=60)
        # predict 的结果是 每一个label的概率
        proba = self.model.predict([[token_ids], [segment_ids]])
        rst = {l:p for l,p in zip(self.label_list,proba[0])}
        # 对概率进行排序，选择概率最大的那一个
        rst = sorted(rst.items(), key = lambda kv:kv[1],reverse=True)
        name,confidence = rst[0]
        return {"name":name,"confidence":float(confidence)}


BIM = BertIntentModel()


if __name__ == '__main__':

    r = BIM.predict("who invent an application")
    print(r)