import pandas as pd
data = {'id':  ['1', '2','3','4','5'],
        'level':[ ['a','ab'],['a','b', 'c' ,'cd'], ['a','b', 'c' ,'cd'],['a'],['x','y']],
         'text':['hello world','good morning','new york', 'programming', 'computer']
        }

df = pd.DataFrame(data) #olumns = ['First Column Name','Second Column Name',...])

def intersection(lst1, lst2): 
    l= list(set(lst1) & set(lst2))
    if len(l) > 0:
       return True
    else:
       return False
    
print (df)