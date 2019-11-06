import json
import sys
import argparse

from collections import OrderedDict

def parse():
    parser = argparse.ArgumentParser(description='To merge multiple json files')
    parser.add_argument('-f', '--folder_path', help='Folder path for json files')
    parser.add_argument('-i', '--input_prefix', help='Folder path for json files')
    parser.add_argument('-o', '--output_prefix', help='Folder path for json files')
    parser.add_argument('-m', '--max_file_size', help='Folder path for json files')
    return parser


def size(file1,file2):
    return sys.getsizeof(file1)+sys.getsizeof(file2)

def Read(s):
    with open(s) as f:
         data = json.load(f, object_pairs_hook=OrderedDict)
    return data

def Write(s,d):
    with open(s, 'w') as f:
         json.dump(d, f)
         
def merge_json(folder,Input,Output,max_size):
    input_index=1
    temp_list=[]
    output_index=1
    while(1):
        s=folder+Input+str(input_index)+'.json' 
        input_index=input_index+1
        try:
          data=Read(s)
          key=data.keys()
          if(size(temp_list,data[key[0]])<max_size):
             temp_list.extend(data[key[0]])
          else:
             s=folder+Output+str(output_index)+'.json' 
             output_index=output_index+1
             d={}
             d[key[0]]=temp_list
             Write(s,d)
             temp_list=[]
             temp_list.extend(data[key[0]])
        except IOError:
              s=folder+Input+str(1)+'.json' 
              data = Read(s)
              key=data.keys() 
              s=folder+Output+str(output_index)+'.json' 
              d={}
              d[key[0]]=temp_list                  
              Write(s,d) 
              return


"""folder=str(input('Enter the file path or folder directory :'))
Input=str(input('Enter the Input Prefix'))
Output=str(input('Enter the '))
max_size=200
fun(folder,Input,Output,max_size)"""
parser = parse()
args = parser.parse_args()
folder=args.folder_path
Input=args.input_prefix
output=args.output_prefix
max_size=args.max_file_size
merge_json(folder,Input,output,int(max_size))    