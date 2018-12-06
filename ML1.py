#Basic machine learning
import math
import random

def euclideanDist(pta,ptb):
    x,y=pta
    c,v=ptb
    return(math.sqrt((x-c)**2+(y-v)**2))

def sim(dt,x,fn=euclideanDist):
    mx=fn(x,(50,100))
    pos=(0,0)
    c=1
    for i in dt.keys():
        
        c=c+1
        k=fn(x,i)
        
        if k<mx:
            
            mx=k
            pos=i
            
    
    
    print(dt[pos],mx)


dict={}

for i in range(100):
    
    dict[(random.choice(range(50,101)),random.choice(range(1,76)))]="Type A"
for i in range(100):
    
    dict[(random.choice(range(120,201)),random.choice(range(80,101)))]="Type B"
for i in range(100):

    dict[(random.choice(range(250,301)),random.choice(range(120,181)))]="Type C"


sim(dict,(270,300))
