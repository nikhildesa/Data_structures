# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:24:13 2021

@author: nikhi        Linkedlist
"""

class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        new_node = node(data)
        cur = self.head
        
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        
        while(cur.next!=None):
            cur = cur.next
            total+=1
        return total
    
    def display(self):
        elem = []
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            elem.append(cur.data)
        print(elem)
        
        
    def get(self,index):
        if index >=self.length():
            print('error')
            return 0
        else:
            cur = self.head
            cur_index = 0
            
            while cur.next!=None:
                cur = cur.next
                
                if cur_index == index:
                    return cur.data
                else:
                    cur_index+=1
                    
    def erase(self,index):
        if index >=self.length():
            print('error')
            return 0
        else:
            cur_index = 0
            cur = self.head
            #last_node = self.head
            while True:
                last_node = cur
                cur = cur.next
                
                if index == cur_index:
                    last_node.next = cur.next
                    return 
                else:
                    cur_index+=1
        
        
my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.get(2)
my_list.erase(2)
my_list.display()













