"""Problem statement: The goal is to tokenize the following 5 sentences into words, excluding the stop words.
i/p:
 sentence and stopwords are given """

sentence=["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen laps,"
          "lit up simultaneously on the banks of the Sarayu river"]
stopwords=['was','for','a','of','the','and','to','in','on','with']
res=[]
for i in sentence:
     row_data=[]
     for k in i.split():
         # to split the sentence into words , not in letter
         if k not in stopwords:
             row_data.append(k)
     res.append(row_data)
print(res)
