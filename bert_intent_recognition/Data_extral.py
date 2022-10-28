import csv
import openpyxl

def deal_data(path, sheet_name):

    workbook = openpyxl.load_workbook(path)
    workbook_sheet = workbook[sheet_name]
    print(workbook_sheet)
    with open("train.csv", "w+", encoding="utf-8-sig") as f:
        write = csv.writer(f)
        print(write)
        data = []
        write.writerows("text,label_class,label")
        for i in range(1, workbook_sheet.max_row + 1):
            row_stack = []
            for j in range(1, workbook_sheet.max_column + 1):
                row_stack.append(workbook_sheet.cell(row=i, column=j).value)
            data.append(row_stack)
        write.writerows(data)


if __name__ == '__main__':
    path = "./AI Book Concepts 2022 (ChX - Your Name) v3(1).xlsx"
    sheet_name = "Q&A"
    deal_data(path,sheet_name)