import re
import pandas as pd
from collections import defaultdict 

def clean_str(string):
  """To replace weird word, like \x96, \x85..."""
  string=string.lower()
  string = re.sub(r"it\'s", "it is", string)
  string = re.sub(r"let\'s", "let us", string)
  string = re.sub(r"won\'t", "will not", string)
  string = re.sub(r"n\'t", " not", string)
  string = re.sub(r"\'re", " are", string)
  string = re.sub(r"\'d", " would", string)
  string = re.sub(r"\'ve", " have", string)
  string = re.sub(r"\'ll", " will", string)
  string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
  string = re.sub(r",", " ", string)
  string = re.sub('\"', "", string)
  string = re.sub('\'', "", string)
  string = re.sub('\!', "", string)
  string = re.sub('\.', "", string)
  string = re.sub(r"\s{2,}", " ", string) #replace space 
  return string.strip()

  
def df_to_list(df):
  """split column""" 
  list_text=[]
  list_label=[]
  for idx in range(0,len(df)):
    list_text.append(df.loc[idx].str.split("\t").tolist()[0][0])
    list_label.append(df.loc[idx].str.split("\t").tolist()[0][1])
    
  new_df = pd.DataFrame({'text':list_text,'label':list_label})
  return new_df


def get_duplicated_idx(data,col):
  """get the index of duplicate row"""
  IDX=[]
  count=defaultdict (int)
  for idx,line in enumerate(data.duplicated(col)):
    if line == True:
      IDX.append(idx)
        
  return IDX
 

def get_pos_neg_texts(data,i):
  """Get the index of text with positive/negtive label <can decide by second parameter>"""
  IDX=[]
  for idx,y in enumerate(data):
    if y == i:
      IDX.append(idx)    

  return IDX
  
  
def get_idx(list,list2):
  """Compare two list"""
  dict1=defaultdict(int)
  IDX=[]
  for i in list:
    dict1[i]+=1
  for i,j in enumerate(list2):
    if dict1[j] >= 1:
      IDX.append(i)
    
  return IDX
  
  
def cat_subset_by_index(List,index):
  """Get subset of feature"""
  features=[]
  for i in index:
    features.append(List[i])
  return features