# AI_tutor
## Here you can know how to start the program
## 1.started the Neo4j knowledge graph\
* Open the cmd and go to the directory "\Knowledge\neo4j-community-3.5.21-windows\neo4j-community-3.5.21\bin" (you just use the Windows file management system to copy the address and paste in the command line)
* When you enter the "...../bin" address you need to type the neo4j console to start the knowledge graph, and you will see a link for you to open in the browser.
* You can use the username: neo4j and password neo4j to login and you see the content of our knowledge graph. 
## 2.Go to the "bert_intent_recognition" directory and run the data_helper.py
* The file will generate the extra data for model to training and store them in the "./Data"
## 3.Go to the "prepossessing" directory and run all three files to get an tagging_data.txt 
* The raw data set is in xlsx format and store in the "Data" directory.
* You need to change the directory for reading the raw data set according to you own computer absolute address(AutoTagging.py and extraction.py).
* tagging_data.txt will contain the all the tokenized question sentences with an BIO tags.
* The split.py will use the tagging_data.txt to produce three data set for Bilstm_crf model to train and test which are stored in directory: "../bilistm_crf/data1/" 
## 4.Go to the "bert_intent_recognition" directory and run the train.py so that you can start to train the model.
## 5.Go to the "bilstm_crf" directory and run the train.py so that you can also start to train the model.
## 6. After finishing training two models then you can run the GUI.py file under the directory "Al_tutor/"
## Hints: if you want to test the single model performance you cna just run the app.py in each model directory.