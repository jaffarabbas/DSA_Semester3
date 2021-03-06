# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:47:38 2018

@author: Dell
"""
class Vector:
    def __init__ (self,d):
        self._coord=[0]*d
    def __len__(self):
        return(len (self._coord))
    def __getitem__(self,j):
        return self._coord[j]
    def __setitem__(self,j,val):
        self._coord[j]=val
    def __add__(self,other):
        if len(self)!=len(other):
            raise ValueError("the dimensions must match")
        result=Vector(len(self))
        for j in range(len(self)):
            result=self[j]+other[j]
        return result
    def __sub__(self,other):
        if len(self)!=len(other):
            raise ValueError("the dimensions must match")
        result=Vector(len(self))
        for j in range(len(self)):
            result=self[j]-other[j]
        return result
    def __eq__(self,other):
        return self._coord==other._coord
    def __ne__(self,other):
        return not self==other
    def __str__(self):
        return '<' + str(self._coord)[1:-1] + '> '
    def __neg__(self):
        result=Vector(len(self))
        for j in range(len(self)):
            result[j]=-self[j]
        return result    
    def __mul__(self,factor):
        result=Vector(len(self))
        for j in range(len(self)):
            result[j]=factor*self[j]
        return result    
    def __rmul__(self,factor):
        result=Vector(len(self))
        for j in range(len(self)):
            result[j]=self[j]*factor
        return result   
    
    
if __name__=='__main__':
    v=Vector(5)
    w=Vector(5)
    v[1]=23
    v[3]=67
    w[1]=8
    w[3]=34
    u=[]
    for i in range(len(v)):
        u.append(v[i]-w[i])
    print (u)   
    print(-w)
    print(v*3)
    print(3*v)
   
    

       
    
    