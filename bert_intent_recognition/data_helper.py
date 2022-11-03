#! -*- coding: utf-8 -*-
import json
import random
import pandas as pd 

def gen_training_data(raw_data_path):
    label_list = [line.strip() for line in open('label','r',encoding='utf8')]
    print(label_list)
    label2id = {label:idx for idx,label in enumerate(label_list)}

    data = []
    with open(raw_data_path,'r',encoding='utf8') as f:
        origin_data = f.read()
        origin_data = eval(origin_data)

    label_set = set()
    for item in origin_data:
        text = item["originalText"]
        label_36class = item["label_36class"][0].strip("'")
        if len(text) > 60 and label_36class not in ["所属科室","传染性","治愈率","治疗时间"]:
            continue
        label_class = item["label_4class"][0].strip("'")
        if label_class == "其他":
            data.append([text,label_class,label2id[label_class]])
            continue
        
        label_set.add(label_class)
        if label_36class in label_list:
            data.append([text,label_36class,label2id[label_36class]])
        label_set.add(label_36class)

    print(label_set)

    return data



def gen_sample_base_template():

    # definition
    definition_explain_qwds = ["what is ","Could you tell me ","Can i ask ","Can you discribe ","May i ask ","what can you tell me ","How to describe "]
    definition_qwds = ["the meaning of ","the difinition of ","the discription of ", "the portrait of ","the picture of "]

    # developer
    developer_explain_qwds =['Who ','which person ','which one']
    developer_qwds = ['is the funder of ', 'setup the ','is the designer ', 'is the inventor ', "is the developer", "is the creator ",]

    #different
    different_explain_qwds = ['What is ','How is ','Is there a ','Is there any','Is the ','Are there a ','Are there any','Are the ']
    different_qwds = ['the difference', 'the contrast ', 'the gap ', 'the seperation ' ]
    different_connectives_qwds = ['between ','compare ','from ']

    #drawback
    drawback_explain_qwds = ['What are ', 'What is ', "Could you tell me ","Can i ask ","Can you discribe ","May i ask ","what can you tell me ","How to describe ",'Are there any']
    drawback_qwds = ['the drawbacks of ', ' the disadvantages of ', 'the downsides of ', 'the shortcomings of ','the cons of ','']

    #example
    example_explain_qwds = ["Could you tell me ", "Can i ask ", "May i ask ", "Can you give me", 'Are there any',"Can you provide "," Can you show me ","Can you offer me ", "Can you point out "]
    example_qwds = ["the example of ","the illustrate of ","the instance of ","the smaple of ","the case of "]

    #method
    method_explain_qwds = ["What do we need to ","How to ","what is the requirement to ","which method can we used to "]
    method_qwds = ["chieve the ", "use the ","realize the ","accomplish the ","implement","carry out",]

    # reason
    reason_explain_qwds = ["what is ", ]
    reason_qwds = ["the reason ", "use the ", "realize the ", "accomplish the ", "implement", "carry out", ]
    reason_explain_qwds =["what is the reason of ","Can you explain the reason of","Could you tell me the reason of ","Can you give me the reason about "]


    greet_qwds = ['hello !','excuse me !','Hi !','How are you ?','How do you do ?']




    label_list = [line.strip() for line in open('label','r',encoding='utf8')]
    label2id = {label:idx for idx,label in enumerate(label_list)}

    eneity_list = ["AI","Data minning","NLP"]
    n = len(eneity_list)

    data = []

    #问定义
    template = "{greet}{explain}{definition}{eneity}"
    for i in range(150):
        greet = greet_qwds[random.randint(0,len(greet_qwds)-1)]
        explain = definition_explain_qwds[random.randint(0,len(definition_explain_qwds)-1)]
        definition = definition_qwds[random.randint(0, len(define_qwds) - 1)]
        eneity = eneity_list[random.randint(0,n)]
        text = template.format(greet=greet,explain=explain,eneity=eneity,difinition=definition)
        data.append([text,'definition',label2id['definition']])

    #developer
    template = "{greet}{explain}{developer}{eneity}"
    for i in range(300):
        greet = greet_qwds[random.randint(0,len(greet_qwds)-1)]
        explain = developer_explain_qwds[random.randint(0,len(developer_explain_qwds)-1)]
        eneity = eneity_list[random.randint(0, n)]
        developer = developer_qwds[random.randint(0,len(developer_qwds)-1)]
        text = template.format(greet=greet,explain=explain,developer=developer,eneity=eneity)
        data.append([text,'developer',label2id['developer']])

    #difference
    template = "{greet}{explain}{difference}{Connectives}{eneity1}and{eneity2}"
    for i in range(300):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        eneity1 = eneity_list[random.randint(0, n)]
        eneity2 = eneity_list[random.randint(0, n)]
        explain = different_explain_qwds[random.randint(0,len(different_explain_qwds)-1)]
        difference = different_qwds[random.randint(0,len(different_qwds)-1)]
        Connectives = different_connectives_qwds[random.randint(0,len(different_connectives_qwds)-1)]
        text = template.format(greet=greet,explain=explain,difference=difference,Connectives=Connectives,eneity1=eneity1,eneity2=eneity2)
        data.append([text,'difference',label2id['difference']])

    #drawback
    template = "{greet}{explain}{drawback}{eneity}"
    for i in range(300):
        greet = greet_qwds[random.randint(0,len(greet_qwds)-1)]
        explain = drawback_explain_qwds[random.randint(0,len(drawback_explain_qwds)-1)]
        eneity = eneity_list[random.randint(0, n)]
        drawback = drawback_qwds[random.randint(0,len(drawback_qwds)-1)]
        text = template.format(greet=greet,explain=explain,drawback=drawback,eneity=eneity)
        data.append([text,'drawback',label2id['drawback']])

    #example
    template = "{greet}{explain}{example}{eneity}"
    for i in range(300):
        greet = greet_qwds[random.randint(0,len(greet_qwds)-1)]
        explain = example_explain_qwds[random.randint(0,len(example_explain_qwds)-1)]
        eneity = eneity_list[random.randint(0, n)]
        example = example_qwds[random.randint(0,len(example_qwds)-1)]
        text = template.format(greet=greet,explain=explain,example=example,eneity=eneity)
        data.append([text,'example',label2id['example']])

    #has_part

    #method
    template = "{greet}{explain}{method}{eneity}"
    for i in range(300):
        greet = greet_qwds[random.randint(0,len(greet_qwds)-1)]
        explain = method_explain_qwds[random.randint(0,len(method_explain_qwds)-1)]
        eneity = eneity_list[random.randint(0, n)]
        method = method_qwds[random.randint(0,len(method_qwds)-1)]
        text = template.format(greet=greet,explain=explain,method=method,eneity=eneity)
        data.append([text,'method',label2id['method']])

    # reason
    template = "{greet}{explain}{method}{eneity}"
    for i in range(300):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        explain = method_explain_qwds[random.randint(0, len(method_explain_qwds) - 1)]
        eneity = eneity_list[random.randint(0, n)]
        reason = method_qwds[random.randint(0, len(method_qwds) - 1)]
        text = template.format(greet=greet, explain=explain, reason=reason, eneity=eneity)
        data.append([text, 'reason', label2id['reason']])

    return data
    

def load_data(filename):
    """加载数据
    单条格式：(文本, 标签id)
    """
    df = pd.read_csv(filename,header=0)
    return df[['text','label']].values

if __name__ == '__main__':
    data_path = "E:/工作空间/CMID/CMID.json"
    data1= gen_training_data(data_path)
    data2 = gen_sample_base_template()

    data = data1 + data2

    data = pd.DataFrame(data,columns=['text','label_class','label'])
    data = data.sample(frac=1.0)
    print(data['label_class'].value_counts())

    data['text_len'] = data['text'].map(lambda x: len(x))
    print(data['text_len'].describe())
    import matplotlib.pyplot as plt
    plt.hist(data['text_len'], bins=30, rwidth=0.9, density=True,)
    plt.show()

    del data['text_len']

    train_num = int(0.9*len(data))
    train,test = data[:train_num],data[train_num:]
    train.to_csv("./data/train.csv",index=False)
    test.to_csv("./data/test.csv",index=False)


    

