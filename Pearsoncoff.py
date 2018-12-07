#Basic Machine learning
#Pearson correlation factor
#LawJarp

import math
import random

#Consider a dictionary of few people with friuts and how much they like it(scale of 1 to 10)
dict={'Anna':{"Apples":8,"Bannanas":9,"Oranges":7,"Grapes":7,"Tomato":6,"Watermelon":10},
      'Raj':{"Apples":8,"Bannanas":9,"Oranges":4,"Grapes":6,"Tomato":7,"Watermelon":8},
      'Bhuvan':{"Apples":3,"Bannanas":5,"Oranges":8,"Grapes":4,"Tomato":7,"Watermelon":6},
      'Aditya':{"Apples":4,"Bannanas":9,"Oranges":7,"Grapes":7,"Tomato":8,"Watermelon":2},
      'Gaurav':{"Apples":2,"Bannanas":7,"Oranges":6,"Grapes":9,"Tomato":7,"Watermelon":4},
      'Ishan':{"Apples":3,"Bannanas":4,"Oranges":4,"Grapes":8,"Tomato":8,"Watermelon":7},
      'Harsha':{"Apples":4,"Bannanas":8,"Oranges":5,"Grapes":8,"Tomato":2,"Watermelon":10},
      'Nikhil':{"Apples":5,"Bannanas":2,"Oranges":2,"Grapes":3,"Tomato":2,"Watermelon":5},
      'Somedude':{"Apples":1,"Bannanas":8,"Oranges":6,"Grapes":7,"Tomato":8,"Watermelon":6}
      }

#And this is the test set
test={"X":{"Apples":8,"Bannanas":10,"Oranges":8,"Grapes":6,"Tomato":6,"Watermelon":9}}


#Aim: To find the person similar to 'X' using Pearson co-relation factor

#Takes in the preferences of two people and outputs a number between -1 and 1, closer the number is to 1, more the similar the person is
#formula to calculate pearson corelation coefficent : (a1*b1+a2*b2+...)-((a1+a2+a3+..)*(b1+b2+b3) / n)  /   (sqrt(((a1^2+a2^2)-(a1+a2+..)^2)) / n) * ((b1^2+b2^2+b3^2)-(b1+b2+..)^2) /n ))
def pearsonCoff(a,b):

    sum1=sum(x for x in a.values())
    sum2=sum(x for x in b.values())

    sum1sq=sum(pow(x,2) for x in a.values())
    sum2sq=sum(pow(x,2) for x in b.values())

    psum=0
    alist=list(a.values())
    blist=list(b.values())
    for i in range(len(alist)):
        psum+=alist[i]*blist[i]

    n=len(alist)
    nu=psum-(sum1*sum2/n)
    d=math.sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if d==0:return 0
    return nu/d

#Finds and prints the similarity coefficient between all the people in dict and 'X'
for i in dict.keys():
    print(i+": "+str(pearsonCoff(dict[i],test["X"])))

    
