#! -*- coding: utf-8 -*-
import random
import numpy as np
import os
from bert4keras.backend import keras
from bert4keras.tokenizers import Tokenizer
from bert4keras.snippets import sequence_padding, DataGenerator
from sklearn.metrics import classification_report
from bert4keras.optimizers import Adam
import tensorflow as tf

from bert_model import build_bert_model
from data_helper import load_data

seed = 233
tf.set_random_seed(seed)
np.random.seed(seed)
random.seed(seed)
os.environ['PYTHONHASHSEED'] = str(seed)

#定义超参数和配置文件
class_nums = 11
maxlen = 120
batch_size = 16

config_path='../Bert_model/wwm_uncased_L-24_H-1024_A-16/bert_config.json'
checkpoint_path ='../Bert_model/wwm_uncased_L-24_H-1024_A-16/bert_model.ckpt'
dict_path ='../Bert_model/wwm_uncased_L-24_H-1024_A-16/vocab.txt'

tokenizer = Tokenizer(dict_path)
class data_generator(DataGenerator):
    """
    数据生成器
    """
    def __iter__(self, random=False):
        batch_token_ids, batch_segment_ids, batch_labels = [], [], []
        for is_end, (text, label) in self.sample(random):
            token_ids, segment_ids = tokenizer.encode(text, maxlen=maxlen)#[1,3,2,5,9,12,243,0,0,0]
            batch_token_ids.append(token_ids)
            batch_segment_ids.append(segment_ids)
            batch_labels.append([label])
            if len(batch_token_ids) == self.batch_size or is_end:
                # 应该是填充矩阵的大小
                batch_token_ids = sequence_padding(batch_token_ids)
                batch_segment_ids = sequence_padding(batch_segment_ids)
                # 问题：为什么label也需要填充
                batch_labels = sequence_padding(batch_labels)
                # yield表示迭代，相当于while吧
                yield [batch_token_ids, batch_segment_ids], batch_labels
                batch_token_ids, batch_segment_ids, batch_labels = [], [], []

if __name__ == '__main__':
    # 加载数据集
    train_data = load_data('./data/train.csv')
    test_data = load_data('./data/test.csv')

    # 转换数据集
    train_generator = data_generator(train_data, batch_size)
    test_generator = data_generator(test_data, batch_size)

    model = build_bert_model(config_path,checkpoint_path,class_nums)
    print(model.summary())

    model.compile(
        loss='sparse_categorical_crossentropy',
        optimizer=Adam(5e-6),
        metrics=['accuracy'],
    )

    earlystop = keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=4,
        verbose=2,
        mode='min'
        )

    bast_model_filepath = 'checkpoint1/best_model.weights'
    '''
        保存训练后的模型
        bast_model_filepath: 保存模型的路径
        monitor：被检测的数据 val_acc or val_loss
        verbose: 详细信息模式，0 或者1。0为不打印输出信息，1为打印
        如果save_best_only=True，将只保存在验证集上性能最好的模型mode: {auto, min, max} 的其中之一
    '''
    checkpoint = keras.callbacks.ModelCheckpoint(
        bast_model_filepath,
        monitor='val_loss',
        verbose=1,
        save_best_only=True,
        mode='min'
        )
    '''
        将数据导入，允许模型
        steps_per_epoch: 每一个epoch 运行的次数
        validation_data：验证集
    '''
    model.fit_generator(
        train_generator.forfit(),
        steps_per_epoch=len(train_generator),
        epochs=80,
        validation_data=test_generator.forfit(),
        validation_steps=len(test_generator),
        shuffle=True,
        callbacks=[earlystop,checkpoint]
    )
    # 把保存的权重加载进去
    model.load_weights(bast_model_filepath)
    test_pred = []
    test_true = []
    for x,y in test_generator:
        p = model.predict(x).argmax(axis=1)
        test_pred.extend(p)

    test_true = test_data[:,1].tolist()
    print(set(test_true))
    print(set(test_pred))

    target_names = [line.strip() for line in open('data/label', 'r', encoding='utf8')]
    print(classification_report(test_true, test_pred,target_names=target_names))