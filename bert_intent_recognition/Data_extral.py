import csv
import openpyxl
import random
import pandas as pd
import json

def gen_sample_base_template(eneity):
    # definition
    definition_explain_qwds = ["what is ", "Could you tell me ", "Can i ask ", "Can you discribe ", "May i ask ",
                               "what can you tell me ", "How to describe "]
    definition_qwds = ["the meaning of ", "the difinition of ", "the discription of ", "the portrait of ",
                       "the picture of "]

    # developer
    developer_explain_qwds = ['Who ', 'which person ', 'which one']
    developer_qwds = ['is the funder of ', 'setup the ', 'is the designer ', 'is the inventor ', "is the developer",
                      "is the creator ", ]

    # different
    different_explain_qwds = ['What is ', 'How is ', 'Is there a ', 'Is there any', 'Is the ', 'Are there a ',
                              'Are there any', 'Are the ']
    different_qwds = ['the difference', 'the contrast ', 'the gap ', 'the seperation ']
    different_connectives_qwds = ['between ', 'compare ', 'from ']

    # drawback
    drawback_explain_qwds = ['What are ', 'What is ', "Could you tell me ", "Can i ask ", "Can you discribe ",
                             "May i ask ", "what can you tell me ", "How to describe ", 'Are there any']
    drawback_qwds = ['the drawbacks of ', ' the disadvantages of ', 'the downsides of ', 'the shortcomings of ',
                     'the cons of ', '']

    # example
    example_explain_qwds = ["Could you tell me ", "Can i ask ", "May i ask ", "Can you give me", 'Are there any',
                            "Can you provide ", " Can you show me ", "Can you offer me ", "Can you point out "]
    example_qwds = ["the example of ", "the illustrate of ", "the instance of ", "the smaple of ", "the case of "]

    # method
    method_explain_qwds = ["What do we need to ", "How to ", "what is the requirement to ",
                           "which method can we used to "]
    method_qwds = ["chieve the ", "use the ", "realize the ", "accomplish the ", "implement", "carry out", ]

    # reason
    reason_explain_qwds = ["what is the reason of ", "Can you explain the reason of",
                           "Could you tell me the reason of ", "Can you give me the reason about "]

    greet_qwds = ['hello ! ', 'excuse me ! ', 'Hi ! ', 'How are you ? ', 'How do you do ? ']

    label_list = [line.strip() for line in open('data/label', 'r', encoding='utf8')]
    label2id = {label: idx for idx, label in enumerate(label_list)}

    eneity_list = eneity
    n = len(eneity_list) - 1

    data = []

    # 问定义
    template = "{greet}{explain}{definition}{eneity}?"
    for i in range(150):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        explain = definition_explain_qwds[random.randint(0, len(definition_explain_qwds) - 1)]
        definition = definition_qwds[random.randint(0, len(definition_qwds) - 1)]
        eneity = eneity_list[random.randint(0, n)][0]
        text = template.format(greet=greet, explain=explain, definition=definition, eneity=eneity, )
        data.append([text, 'definition', label2id['definition']])

    # developer
    template = "{greet}{explain}{developer}{eneity}?"
    for i in range(300):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        explain = developer_explain_qwds[random.randint(0, len(developer_explain_qwds) - 1)]
        eneity = eneity_list[random.randint(0, n)][0]
        developer = developer_qwds[random.randint(0, len(developer_qwds) - 1)]
        text = template.format(greet=greet, explain=explain, developer=developer, eneity=eneity)
        data.append([text, 'developer', label2id['developer']])

    # different
    template = "{greet}{explain}{difference}{Connectives}{eneity1}and{eneity2}?"
    for i in range(300):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        eneity1 = eneity_list[random.randint(0, n)][0]
        eneity2 = eneity_list[random.randint(0, n)][0]
        explain = different_explain_qwds[random.randint(0, len(different_explain_qwds) - 1)]
        difference = different_qwds[random.randint(0, len(different_qwds) - 1)]
        Connectives = different_connectives_qwds[random.randint(0, len(different_connectives_qwds) - 1)]
        text = template.format(greet=greet, explain=explain, difference=difference, Connectives=Connectives,
                               eneity1=eneity1, eneity2=eneity2)
        data.append([text, 'different', label2id['different']])

    # drawback
    template = "{greet}{explain}{drawback}{eneity}?"
    for i in range(300):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        explain = drawback_explain_qwds[random.randint(0, len(drawback_explain_qwds) - 1)]
        eneity = eneity_list[random.randint(0, n)][0]
        drawback = drawback_qwds[random.randint(0, len(drawback_qwds) - 1)]
        text = template.format(greet=greet, explain=explain, drawback=drawback, eneity=eneity)
        data.append([text, 'drawback', label2id['drawback']])

    # example
    template = "{greet}{explain}{example}{eneity}?"
    for i in range(300):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        explain = example_explain_qwds[random.randint(0, len(example_explain_qwds) - 1)]
        eneity = eneity_list[random.randint(0, n)][0]
        example = example_qwds[random.randint(0, len(example_qwds) - 1)]
        text = template.format(greet=greet, explain=explain, example=example, eneity=eneity)
        data.append([text, 'example', label2id['example']])

    # has_part

    # method
    template = "{greet}{explain}{method}{eneity}?"
    for i in range(300):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        explain = method_explain_qwds[random.randint(0, len(method_explain_qwds) - 1)]
        eneity = eneity_list[random.randint(0, n)][0]
        method = method_qwds[random.randint(0, len(method_qwds) - 1)]
        text = template.format(greet=greet, explain=explain, method=method, eneity=eneity)
        data.append([text, 'method', label2id['method']])

    # reason
    template = "{greet}{explain}{reason}{eneity}?"
    for i in range(300):
        greet = greet_qwds[random.randint(0, len(greet_qwds) - 1)]
        explain = method_explain_qwds[random.randint(0, len(method_explain_qwds) - 1)]
        eneity = eneity_list[random.randint(0, n)][0]
        reason = method_qwds[random.randint(0, len(method_qwds) - 1)]
        text = template.format(greet=greet, explain=explain, reason=reason, eneity=eneity)
        data.append([text, 'reason', label2id['reason']])

    return data


def deal_data(path, sheet_name):

    label_list = [line.strip() for line in open('data/label', 'r', encoding='utf8')]
    id_label = {label: index for index, label in enumerate(label_list)}

    data = []
    Total_eneity_csv = []
    Total_eneity_json = []
    chapters = [1,2,3,4,5,8,9,10,11,12,13,14,15]

    for i in chapters:
        full_path = path + str(i)+'.xlsx'
        workbook = openpyxl.load_workbook(full_path)
        workbook_sheet = workbook[sheet_name]

        for row in range(2, workbook_sheet.max_row):
            row_stack = []
            text = workbook_sheet.cell(row, 5).value
            label_class = workbook_sheet.cell(row, 7).value
            label = id_label.get(label_class)
            eneity_csv = [workbook_sheet.cell(row, 6).value]
            eneity_json = workbook_sheet.cell(row, 6).value


            if text == None or label_class == None:
                continue

            if eneity_csv != None and eneity_csv not in Total_eneity_csv:
                Total_eneity_csv.append(eneity_csv)
                Total_eneity_json.append(eneity_json)


            row_stack.append(text)
            row_stack.append(label_class)
            row_stack.append(label)
            data.append(row_stack)

    return data, Total_eneity_csv,Total_eneity_json

def creat_dataset(data):

    with open("data/train.csv", "w+", encoding="utf-8-sig", newline='') as f:
        write = csv.writer(f)
        write.writerow(["text","label_class","label"])
        for item in range(0,int(len(data)*0.7)):
            write.writerow(data[item])

    with open("data/test.csv", "w+", encoding="utf-8-sig", newline='') as f:
        write = csv.writer(f)
        write.writerow(["text","label_class","label"])
        for item in range(int(len(data)*0.7)+1,len(data)-1):
            write.writerow(data[item])

def creat_eneityset(eneities_csv, eneities_json):

    with open("data/eneities.csv", "w+", encoding="utf-8-sig", newline='') as f:
        write = csv.writer(f)
        write.writerows(eneities_csv)

    with open("data/eneities.json", "w+") as f:
        json.dump(eneities_json, f)




if __name__ == '__main__':
    path = "../Concepts/"
    sheet_name = "Q&A"

    data1, eneity_csv, eneity_json = deal_data(path, sheet_name)
    creat_eneityset(eneity_csv,eneity_json)

    data2 = gen_sample_base_template(eneity_csv)
    data = data1 + data2
    creat_dataset(data)