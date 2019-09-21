#Libraries
from textwrap import wrap
import numpy as np

m=5 #No. of Rows
n=5 #No. of Columns

#Functioning of Plain text
plain_text=input("\n Enter the Plain Text ")
length=len(plain_text)
plain_text=plain_text.lower()
if "j" in plain_text:
    plain_text=plain_text.replace("j","i")
if (length%2) is not 0:
    plain_text=plain_text+"x"
plain_text=wrap(plain_text,2)

#Functioning of Key
length_key=int(input("\n Enter the length of the Key:"))
enc=""
mat=[]
for i in range(0,n):
    mat.append([])
for i in range(0,m):
    for j in range(0,n):
        mat[i].append(j)
        mat[i][j]=""
for i in range(0,length_key):
    for j in range(0,length_key):
        mat[i][j]= input()
print(mat)

"""for i in key:
    if i not in enc:
        if(i==74):
            i=i+1
            continue
        else:
            enc=enc + i
i=65
while(i<91):
    if(chr(i) not in key):
        if(i==74):
            i=i+1
            continue
        else:
            enc=enc+chr(i)
            i=i+1
    else:
        i=i+1
        continue
print(plain_text)
print(enc)"""
