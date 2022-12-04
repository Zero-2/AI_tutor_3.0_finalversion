with open("../prepossessing/tagging_data.txt","r") as f:
    text = f.readlines()
    size = len(text)
with open("../bilstm_crf/data1/training_data.txt", "w+") as f1, open("../prepossessing/tagging_data.txt", "r") as f:
    for i in range(0, int(size*0.7)):
        row = f.readline()
        print(row)
        f1.write(row)
with open("../bilstm_crf/data1/testing_data.txt", "w+") as f1, open("../prepossessing/tagging_data.txt", "r") as f:
        for i in range(int(size * 0.7)+1, int(size * 0.9)):
            row = f.readline()
            print(row)
            f1.write(row)
with open("../bilstm_crf/data1/dev_data.txt", "w+") as f1, open("../prepossessing/tagging_data.txt", "r") as f:
    for i in range(int(size * 0.9) + 1, int(size)):
        row = f.readline()
        print(row)
        f1.write(row)