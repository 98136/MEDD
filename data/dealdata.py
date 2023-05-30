
fil_path="xianyu/train.txt"
f2=open("xianyu/bert_data.json","w",encoding="utf-8")
dic={}
with open(fil_path,"r",encoding="utf-8") as f1:
    sentences=[]
    sentence=[]
    tags=[]
    tag=[]
    for line in f1.readlines():
            data=line.strip().split(" ")
            if len(data)>1:
                sentence.append(data[0])
                tag.append(data[1])
            else:
                sentences.append(sentence)
                tags.append(tag)
                sentence=[]
                tag=[]
print(len(sentences))
print(len(tags))
final_s=[]
final_t=[]
for sen in range (len(sentences)):
    if len(sentences[sen]) !=0:
        final_s.append(sentences[sen])
        final_t.append(tags[sen])
print(len(final_s))
print(len(final_t))

dic["train_x"]=final_s
dic["train_y"]=final_t
fil_path_dev="xianyu/dev.txt"
with open(fil_path_dev,"r",encoding="utf-8") as f1:
    sentencesdev=[]
    sentencedev=[]
    tagsdev=[]
    tagdev=[]
    for line in f1.readlines():

            data=line.strip().split(" ")
            if len(data)>1:
                sentencedev.append(data[0])
                tagdev.append(data[1])
            else:
                sentencesdev.append(sentencedev)
                tagsdev.append(tagdev)
                sentencedev=[]
                tagdev=[]
print(len(sentencesdev))
print(len(tagsdev))
final_ss=[]
final_tt=[]
for sen in range (len(sentencesdev)):
    if len(sentencesdev[sen]) !=0:
        final_ss.append(sentencesdev[sen])
        final_tt.append(tagsdev[sen])
print(len(final_ss))
print(len(final_tt))
dic["dev_x"]=final_ss
dic["dev_y"]=final_tt
fil_path_test="xianyu/test.txt"
with open(fil_path_test,"r",encoding="utf-8") as f1:
    sentencestest=[]
    sentencetest=[]
    tagstest=[]
    tagtest=[]
    for line in f1.readlines():

            data=line.strip().split(" ")
            if len(data)>1:
                sentencetest.append(data[0])
                tagtest.append(data[1])
            else:
                sentencestest.append(sentencetest)
                tagstest.append(tagtest)
                sentencetest=[]
                tagtest=[]
print(len(sentencestest))
print(len(tagstest))

final_sss=[]
final_ttt=[]
for sen in range (len(sentencestest)):
    if len(sentencestest[sen]) !=0:
        final_sss.append(sentencestest[sen])
        final_ttt.append(tagstest[sen])
print(len(final_sss))
print(len(final_ttt))

dic["test_x"]=final_sss
dic["test_y"]=final_ttt

import json
json_data = json.dumps(dic)
f2.write(json_data)