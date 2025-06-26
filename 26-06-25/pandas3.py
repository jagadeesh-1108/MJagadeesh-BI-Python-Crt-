#DataFrames
import pandas as pd
Data={
    'Std1':{
    'Name':'Nani',
    'Branch':'BI',
    'ID':10001,
    'Skills':['Pyhton','DSA','SQL']
},
    'Std2':{
        'Name':'Jagadeesh',
        'Branch':'BI',
        'ID':1002,
        'Skills':['Pyhton','HTML']}
}
print(pd.DataFrame(Data))