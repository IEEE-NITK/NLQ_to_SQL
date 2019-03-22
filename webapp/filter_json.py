
import json
import os
import codecs

anno = 'test.jsonl'


def read_anno_json(anno_path):
    with codecs.open(anno_path, "r", "utf-8") as corpus_file:
        js_list = [json.loads(line) for line in corpus_file]
    return js_list

js_list = read_anno_json(anno)


def filter_json(question, table_id):

    print(type(js_list))
    # print((js_list[0]["question"]))
    # print((js_list[0]))

    for i in range(0, len(js_list)):
        a = js_list[i]["question"]["words"]

        a = ''.join(a)

        print(" searching test json: {}".format(a))
        b = question.replace(" ", "")
        # "".join(question.split())

        print(" given question: {}".format(question))
        
        
        if(b in a):
            print('found the string')
            # with open('/home/palak/coarse2fine/c2f/data_model/wikisql/data/User_Input.jsonl', 'w') as file:
            #     file.write(json.dumps(dict))

            with open('/home/chenna/Desktop/NLQ_to_SQL/webapp/User_Input.jsonl', 'w') as file:
                file.write(json.dumps(js_list[i]))
            break

# ques3 = "how many different college"
# ques2 = ""
# filter_json(ques3, 1)


