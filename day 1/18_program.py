"""  Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
{"merry":"god", "cbristmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

and use it to translate your Christmas wishes from English into Swedish

That is, write a python function translate() that accepts the bilingual dictionary
and a list of English words (your Christmas wish) and returns a list of equivalent Swedish word. """

def translate (dic1,list2):
    list2=[]
    for i in list1:
        list2.append(dic1[i])
    return list2
        

dic1= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
list1=["merry","christmas"]
print (translate(dic1,list1))
