# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 10:50:57 2015

@author: Administrator
"""
import csv
import numpy as np
import operator
def loadTrainData():
    train_x=[]
    train_y=[]
    with open("D:\\Kaggle\\train.csv") as TrainFile:
        lines=csv.reader(TrainFile)
        for line in lines:
            train_y.append(line[0])
            train_x.append(line[1:])
            
        train_x.remove(train_x[0])
        train_y.remove(train_y[0])
    return toInt(train_x),toInt(train_y)
def loadTestData():
    test_x=[]
    with open("D:\\Kaggle\\test.csv") as TestFile:
        lines=csv.reader(TestFile)
        for line in lines:
            test_x.append(line)
        test_x.remove(test_x[0])
    return toInt(toInt(test_x))
def toInt(data):
    data=np.mat(data)
    #print type(data)
    row,col=np.shape(data)
    #print row,col
    int_data=np.zeros((row,col),int)
    for i in range(0,row):
        for j in range(0,col):
            int_data[i,j]=int(data[i,j])
    return int_data

##############KNN算法,K近邻，一般K值定位3-20之间
def knn(test_x_single,train_x,train_y,k):
    num_count={}    
    #行数
    row=np.shape(train_x)[0]
    print row    
    mat_test=np.tile(test_x_single,(row,1))
    diff_mat=mat_test-train_x
    #求和，然后开平方根
    distances=np.sum(diff_mat**2,axis=1)**0.5
    #得到离他最近的K个索引
    index=distances.argsort()[0:k+1]
    #取得这K个label
    for i in index:
        if num_count.has_key(train_y[0][i])==0:
            num_count[train_y[0][i]]=1
        else:
            num_count[train_y[0][i]]=num_count[train_y[0][i]]+1
        
    sorted_label=sorted(num_count.iteritems(),key=operator.itemgetter(1),reverse=True)
    
    return sorted_label[0][0]
    
            
        
        

#得到训练集中的X，和标签Y   
train_x,train_y=loadTrainData()
#得到测试集
test_x=loadTestData()

count=0
res=[]
csv_file=open('D:\\Kaggle\\res.csv','wb')
for single in test_x:    
    t=knn(single,train_x,train_y,5)
    tmp=[]
    count=count+1
    tmp.append(count)
    tmp.append(t)
    writer=csv.writer(csv_file)
    writer.writerow(tmp)    

csv_file.close()