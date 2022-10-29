import csv
import openpyxl
# import keras.backend as K
from bert4keras.backend import keras,set_gelu
# from tensorflow.keras import backend as K

def deal_data(path, sheet_name):

    workbook = openpyxl.load_workbook(path)
    workbook_sheet = workbook[sheet_name]
    print(workbook_sheet)

    label_list = [line.strip() for line in open('label1', 'r', encoding='utf8')]
    id_label = {label: index for index, label in enumerate(label_list)}
    print(id_label)

    with open("train.csv", "w+", encoding="utf-8-sig") as f:
        write = csv.writer(f)
        print(write)
        data = []
        label = [f"text", "label_class", "label"]
        write.writerow(["text","label_class","label"])

        for row in range(2, workbook_sheet.max_row):
            row_stack = []
            text = workbook_sheet.cell(row, 5).value
            label_class = workbook_sheet.cell(row, 7).value
            label = id_label.get(label_class)

            row_stack.append(text)
            row_stack.append(label_class)
            row_stack.append(label)
            data.append(row_stack)
        write.writerows(data)


if __name__ == '__main__':
    path = "./AI Book Concepts 2022 (ChX - Your Name) v3(1).xlsx"
    sheet_name = "Q&A"
    deal_data(path,sheet_name)