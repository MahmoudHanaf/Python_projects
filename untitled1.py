# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:17:36 2022

@author: Mahmoud
"""

class node :
    def __init__(self,freq,sympol,left=None, right =None):
        self.freq =freq
        self.sympol =sympol
        self.left =left
        self.right =right
        self.huff =''
        

def printNodes(node,val =''):
    newVal =val +str(node.huff)
    
    if(node.left):
        printNodes(node.left,newVal)
    
    if(node.right):
        printNodes(node.right,newVal)
    
    if(not node.right and not node.left):
        print(F'{node.sympol} ---> {newVal}')
        
chars=['a','b','c','d','e']
freq=[0.22,0.28,0.15,0.30,0.05]	

nodes =[]

for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes)>1:
    nodes =sorted(nodes ,key=lambda x:x.freq)
    
    left =nodes[0]
    right=nodes[1]
    
    left.huff=0
    right.huff =1
    
    newNode=node(left.freq+right.freq ,left.sympol+right.sympol ,left ,right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
printNodes(nodes[0])
    
##--------------------------------------------------------------------------
def encode(message):
    encode_message =''
    i=0
    
    while i<= len(message)-1:
        counter =1
        j=i
        ch =message[i]
        
        while j <len(message)-1:
            
            if(message[j]== message[j+1]):
                counter +=1
                j +=1
            else:
                break
        encode_message =encode_message +str(counter)+ch
        i =j+1
    return encode_message
print(encode("AAAVVVVVVRGRRRNNNN"))

### ----------------------------------------------------------------------
# decode 

#--------------------------------------------------------------------------
        

def encode(message):
    encode_message=""
    i=0
    
    while i<= len(message)-1:
        counter =1
        ch =message [i]
        j=i
        
        while j < len(message)-1:
            if(message[j]== message[j+1]):
                counter +=1
                j += 1
            else:
                break
        i =j+1
        encode_message= encode_message +str(counter)+ch
    return  encode_message
print(encode("SSSSFFRRRRRGGG"))           
        
def decode(our_message):
    decode_message =""
    i=0
    while i<= len(our_message)-1:
        run_count = int(our_message[i])
        run_word =our_message[i+1]
        
        for j in range(run_count):
            decode_message=decode_message +run_word
        i =i+2
        
    return decode_message

print(decode("5B8V3G"))
            
    
    
    
        

        




        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
        
        