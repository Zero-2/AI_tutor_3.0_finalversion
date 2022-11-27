# -*- coding:utf-8 -*-
import json
# import flask
import pickle
import ahocorasick
import numpy as np
from gevent import pywsgi
import tensorflow as tf 
import keras
from keras.backend.tensorflow_backend import set_session
from keras.preprocessing.sequence import pad_sequences

import sys
sys.path.append("..")
import bilstm_crf.crf_layer as crf_layer
# from crf_layer import CRF
sys.path.append("..")
import bilstm_crf.bilstm_crf_model
# from bilstm_crf import bilstm_crf_model as BiLstmCrfModel

# 修改：8099 -》15
max_len = 15
# 修改2410 -> 500 ->300
vocab_size = 400
embedding_dim = 200
lstm_units = 128
tag_type = 4

class NerBaseDict(object):
    def __init__(self, dict_path):
        super(NerBaseDict, self).__init__()
        self.dict_path = dict_path
        self.region_words = self.load_dict(self.dict_path)
        self.region_tree = self.build_actree(self.region_words)

    def load_dict(self,path):
        with open(path,'r',encoding='utf8') as f:
            return json.load(f)

    def build_actree(self, wordlist):

        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            # print(word)
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    def recognize(self, text):
        item = {"string": text, "entities": []}

        region_wds = []

        for i in self.region_tree.iter(text):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        item["entities"] = [{"word":i,"type":"eneity","recog_label":"dict"} for i in final_wds]
        return item


class MedicalNerModel(object):
    """基于bilstm-crf的用于医疗领域的命名实体识别模型"""
    def __init__(self):
        super(MedicalNerModel, self).__init__()
        self.word2id,_,self.id2tag = pickle.load(
                open("F:/AI_tutor/bilstm_crf/checkpoint1/word_tag_id.pkl", "rb")
            )
        self.model = bilstm_crf.bilstm_crf_model.BiLstmCrfModel(max_len,vocab_size,embedding_dim,lstm_units,tag_type).build()
        self.model.load_weights('F:/AI_tutor/bilstm_crf/checkpoint1/best_bilstm_crf_model.h5')

        self.nbd = NerBaseDict('F:/AI_tutor/bert_intent_recognition/data/eneities.json')

    def tag_parser(self,string,tags):
        item = {"string": string, "entities": [],"recog_label":"model"}

        string = string.split()
        entity_name = ""
        flag=[]
        visit=False
        for char, tag in zip(string, tags):
            if tag[0] == "B":
                if entity_name!="":
                    x=dict((a,flag.count(a)) for a in flag)
                    y=[k for k,v in x.items() if max(x.values())==v]
                    item["entities"].append({"word": entity_name,"type": y[0]})
                    flag.clear()
                    entity_name=""
                entity_name += char + " "
                flag.append(tag[2:])
            elif tag[0]=="I":
                entity_name += char + " "
                flag.append(tag[2:])
            else:
                if entity_name!="":
                    x=dict((a,flag.count(a)) for a in flag)
                    y=[k for k,v in x.items() if max(x.values())==v]
                    item["entities"].append({"word": entity_name,"type": y[0]})
                    flag.clear()
                flag.clear()
                entity_name=""
         
        if entity_name!="":
            x=dict((a,flag.count(a)) for a in flag)
            y=[k for k,v in x.items() if max(x.values())==v]
            item["entities"].append({"word": entity_name,"type": y[0]})

        return item

    def predict(self,texts):
        """
        texts 为一维列表，元素为字符串
        texts = ["淋球菌性尿道炎的症状","上消化道出血的常见病与鉴别"]
        """
        texts = texts[0].split()
        # for x in texts:
        #     print("x: ")
        #     print(type(x))
        #     print(list(x))
        #     for word in list(x):
        #         print(word)

        # X = [[self.word2id.get(word, 1) for word in x] for x in X]
        print(texts)
        X = [[self.word2id.get(word, 1) for word in texts]]
        # X = [[self.word2id.get(word, 1) for word in texts]]
        X = pad_sequences(X,maxlen=15,value=0)
        pred_id = self.model.predict(X)
        res = []
        texts = " ".join(texts)
        texts = [texts]
        for text,pred in zip(texts,pred_id):
            tags = np.argmax(pred,axis=1)
            print(tags)
            tags = [self.id2tag[i] for i in tags if i!=0]
            print(tags)
            ents = self.tag_parser(text,tags)
            if ents["entities"]:
                res.append(ents)

        for text in texts:
            ents = self.nbd.recognize(text)
            if ents["entities"]:
                res.append(ents)

        return res


global graph,model,sess 

config = tf.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)
graph = tf.get_default_graph()
set_session(sess)

model = MedicalNerModel()


if __name__ == '__main__':
    # app = flask.Flask(__name__)
    #
    # @app.route("/service/api/medical_ner",methods=["GET","POST"])
    # def medical_ner():
    #     data = {"sucess":0}
    #     result = []
    #     text_list = flask.request.get_json()["text_list"]
    #     with graph.as_default():
    #         set_session(sess)
    #         result = model.predict(text_list)
    #
    #     data["data"] = result
    #     data["sucess"] = 1
    #
    #     return flask.jsonify(data)



    # r = model.predict(["淋球菌性尿道炎的症状"])
    r = model.predict(["can you tell me what is cognitive science"])
    print(type(r))
    print(r)

