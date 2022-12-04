# AI_tutor
## Here you can know how to start the program
## 1.Go to the "bert_intent_recognition" directory and run the data_helper.py
* The file will generate the extra data for model to training and store them in the "./Data"
## 2.Go to the "prepossessing" directory and run all three files to get an tagging_data.txt 
* The raw data set is in xlsx format and store in the "Data" directory.
* You need to change the directory for reading the raw data set according to you own computer absolute address(AutoTagging.py and extraction.py).
* tagging_data.txt will contain the all the tokenized question sentences with an BIO tags.
* The split.py will use the tagging_data.txt to produce three data set for Bilstm_crf model to train and test which are stored in directory: "../bilistm_crf/data1/" 
## 3.Go to the "bert_intent_recognition" directory and run the train.py so that you can start to train the model.
## 4.Go to the "bilstm_crf" directory and run the train.py so that you can also start to train the model.
## 5. After finishing training two models then you can run the GUI.py file under the directory "Al_tutor/"
## Hints: if you want to test the single model performance you cna just run the app.py in each model directory.