import pandas

res=eval(open('common.txt', 'r', encoding='utf-8').read())
a={}
key_list=[]
value_list=[]
for i in res:
    for k,v in res[i].items():
        key_list.append(k)
        value_list.append(v)
a['key']=key_list
a['value']=value_list
df=pandas.DataFrame(a)
df.to_csv('common.csv')