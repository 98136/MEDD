import re

# Load the text file
with open("xianyu/test.txt", "r",encoding="utf-8") as f:
    lines = f.readlines()


    tags = set()
    for text in lines:
     try:
        tag = text.strip().split(" ")
        tags.add(tag[1])
     except:
        continue
tag_dict = {"O": 0, "[SEP]": 1, "[CLS]": 2}

for tag in tags:
    if tag not in tag_dict:
        tag_dict[tag] = len(tag_dict)

import json
f2=open("xianyu/bert_tag.json","w",encoding="utf-8")
json_data = json.dumps(tag_dict)
f2.write(json_data)