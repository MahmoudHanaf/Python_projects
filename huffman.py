# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:13:45 2022

@author: Mahmoud
"""

class node:
	def __init__(self, freq, symbol, left=None, right=None):
		# frequency of symbol
		self.freq = freq

		# symbol name (character)
		self.symbol = symbol

		# node left of current node
		self.left = left

		# node right of current node
		self.right = right

		# tree direction (0/1)
		self.huff = ''
        
def printNodes (node,val =''):
    newVal =val +str(node.huff)
    
    if (node.left):
        printNodes(node.left,newVal)
    if(node.right):
        printNodes(node.right,newVal)
    
    if(not node.left and not node.right):
        print(f"{node.symbol} -->  {newVal}")

chars=['a','b','c','d','e']
# frequency of characters
#freq = [ 5, 9, 12, 13, 16, 45]
freq=[0.22,0.28,0.15,0.30,0.05]			

# list containing unused nodes
nodes = []

for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes) >1:
    nodes =sorted(nodes,key=lambda x:x.freq)
    
    left =nodes[0]
    right =nodes[1]
    
    left.huff =0
    right.huff =1
    
    newNode =node(left.freq +right.freq ,left.symbol + right.symbol ,left ,right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
printNodes(nodes[0])
##------------------------------------------------------------------------------





























    
   
    
        