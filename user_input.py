import json

dict ={}
dict["phase"]= 1
dict["question"]= input("enter a question")
dict["sql"]= {
      "conds":[
         [
            0,
            0,
            "1998"
         ]
      ],
      "sel":1,
      "agg":0
   }
dict["table_id"]= input("enter a table_id")
with open('User_Input.jsonl', 'w') as file:
     file.write(json.dumps(dict)) 