#Basic machine learning
#Finding similarities using euclidean distance, more about it in the text file included
#Type of point: Consider x=(a,b) to be a point, 
#Type A: If a belongs to (50,100) and b belongs to (1,75)
#Type B: If a belongs to (120,200) and b belongs to (80,100)
#Type C: If a belongs to (250,300) and b belongs to (120,180)


import math
import random



#Finds distance between two points
def euclideanDist(pta,ptb):
    x,y=pta
    c,v=ptb
    return(math.sqrt((x-c)**2+(y-v)**2))



#finds the similarity between a a point(x) given as input and dataset(dt) as outputs the type of points x is
#Basically it finds the point which is closet to x and thus it assumes x is of the same type as it is closest to it
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

    
    
#Training dictionary code----------
#This code creates a random dictionary of Type A,Type B and Type C points to use for finding if another point is of any revelant type
dict={}
#Here input is (a,b)
#if a is btween 50 and 100 and b is between 1 and 75, its of type A and so on
for i in range(100):
    
    dict[(random.choice(range(50,101)),random.choice(range(1,76)))]="Type A"
for i in range(100):
    
    dict[(random.choice(range(120,201)),random.choice(range(80,101)))]="Type B"
for i in range(100):

    dict[(random.choice(range(250,301)),random.choice(range(120,181)))]="Type C"
#------Dictionary code ends---------



#Finds the type of point the given point in the parameter is
sim(dict,(270,300))



#Example of training dataset used
#'''{(88, 22): 'Type A', (57, 75): 'Type A', (88, 66): 'Type A', (85, 22): 'Type A', (83, 7): 'Type A', (91, 22): 'Type A', (60, 5): 'Type A', (73, 47): 'Type A', (70, 56): 'Type A', (85, 31): 'Type A', (72, 3): 'Type A', (78, 41): 'Type A', (83, 13): 'Type A', (79, 69): 'Type A', (60, 58): 'Type A', (66, 69): 'Type A', (62, 7): 'Type A', (92, 28): 'Type A', (60, 34): 'Type A', (52, 43): 'Type A', (65, 3): 'Type A', (52, 2): 'Type A', (95, 33): 'Type A', (65, 66): 'Type A', (81, 13): 'Type A', (77, 72): 'Type A', (74, 72): 'Type A', (71, 44): 'Type A', (100, 72): 'Type A', (100, 49): 'Type A', (51, 53): 'Type A', (61, 6): 'Type A', (87, 70): 'Type A', (67, 17): 'Type A', (74, 67): 'Type A', (63, 7): 'Type A', (97, 31): 'Type A', (78, 73): 'Type A', (97, 68): 'Type A', (79, 27): 'Type A', (65, 35): 'Type A', (79, 58): 'Type A', (90, 51): 'Type A', (63, 51): 'Type A', (83, 62): 'Type A', (61, 13): 'Type A', (73, 34): 'Type A', (57, 19): 'Type A', (52, 22): 'Type A', (84, 28): 'Type A', (69, 62): 'Type A', (67, 7): 'Type A', (54, 9): 'Type A', (97, 10): 'Type A', (92, 64): 'Type A', (74, 21): 'Type A', (71, 4): 'Type A', (88, 24): 'Type A', (99, 47): 'Type A', (90, 28): 'Type A', (98, 72): 'Type A', (55, 46): 'Type A', (74, 37): 'Type A', (52, 14): 'Type A', (67, 61): 'Type A', (58, 15): 'Type A', (71, 7): 'Type A', (59, 49): 'Type A', (97, 70): 'Type A', (87, 25): 'Type A', (56, 71): 'Type A', (92, 56): 'Type A', (87, 28): 'Type A', (71, 6): 'Type A', (54, 74): 'Type A', (57, 57): 'Type A', (92, 53): 'Type A', (65, 55): 'Type A', (83, 33): 'Type A', (96, 11): 'Type A', (70, 17): 'Type A', (78, 75): 'Type A', (59, 64): 'Type A', (76, 18): 'Type A', (77, 56): 'Type A', (91, 54): 'Type A', (93, 5): 'Type A', (98, 11): 'Type A', (93, 52): 'Type A', (65, 69): 'Type A', (75, 37): 'Type A', (57, 31): 'Type A', (71, 58): 'Type A', (66, 49): 'Type A', (63, 44): 'Type A', (77, 66): 'Type A', (82, 9): 'Type A', (71, 1): 'Type A', (98, 42): 'Type A', (120, 91): 'Type B', (141, 99): 'Type B', (198, 82): 'Type B', (168, 85): 'Type B', (188, 95): 'Type B', (155, 91): 'Type B', (173, 92): 'Type B', (139, 96): 'Type B', (133, 84): 'Type B', (146, 81): 'Type B', (136, 99): 'Type B', (165, 93): 'Type B', (152, 99): 'Type B', (184, 82): 'Type B', (148, 86): 'Type B', (176, 99): 'Type B', (123, 82): 'Type B', (125, 84): 'Type B', (151, 84): 'Type B', (127, 100): 'Type B', (142, 87): 'Type B', (161, 81): 'Type B', (200, 95): 'Type B', (133, 83): 'Type B', (141, 100): 'Type B', (153, 81): 'Type B', (147, 91): 'Type B', (179, 87): 'Type B', (132, 80): 'Type B', (164, 86): 'Type B', (192, 88): 'Type B', (193, 80): 'Type B', (192, 87): 'Type B', (186, 97): 'Type B', (131, 97): 'Type B', (121, 95): 'Type B', (138, 81): 'Type B', (174, 84): 'Type B', (152, 96): 'Type B', (158, 90): 'Type B', (124, 98): 'Type B', (193, 93): 'Type B', (132, 99): 'Type B', (124, 82): 'Type B', (132, 94): 'Type B', (120, 81): 'Type B', (169, 85): 'Type B', (142, 81): 'Type B', (183, 93): 'Type B', (183, 92): 'Type B', (126, 100): 'Type B', (194, 82): 'Type B', (123, 86): 'Type B', (144, 80): 'Type B', (188, 84): 'Type B', (143, 89): 'Type B', (148, 92): 'Type B', (159, 100): 'Type B', (175, 85): 'Type B', (146, 95): 'Type B', (171, 94): 'Type B', (167, 96): 'Type B', (197, 80): 'Type B', (172, 90): 'Type B', (158, 97): 'Type B', (153, 84): 'Type B', (125, 96): 'Type B', (137, 94): 'Type B', (178, 92): 'Type B', (132, 97): 'Type B', (154, 99): 'Type B', (179, 94): 'Type B', (137, 100): 'Type B', (194, 85): 'Type B', (158, 87): 'Type B', (175, 99): 'Type B', (161, 89): 'Type B', (176, 88): 'Type B', (143, 94): 'Type B', (147, 94): 'Type B', (174, 92): 'Type B', (159, 88): 'Type B', (173, 85): 'Type B', (126, 91): 'Type B', (138, 87): 'Type B', (122, 85): 'Type B', (195, 89): 'Type B', (125, 100): 'Type B', (157, 85): 'Type B', (140, 95): 'Type B', (150, 82): 'Type B', (130, 88): 'Type B', (179, 88): 'Type B', (176, 90): 'Type B', (292, 180): 'Type C', (261, 159): 'Type C', (265, 168): 'Type C', (283, 126): 'Type C', (272, 173): 'Type C', (273, 149): 'Type C', (290, 166): 'Type C', (267, 141): 'Type C', (287, 167): 'Type C', (279, 165): 'Type C', (252, 133): 'Type C', (268, 161): 'Type C', (282, 180): 'Type C', (264, 151): 'Type C', (276, 132): 'Type C', (276, 126): 'Type C', (300, 162): 'Type C', (271, 139): 'Type C', (265, 164): 'Type C', (271, 177): 'Type C', (254, 137): 'Type C', (289, 174): 'Type C', (284, 180): 'Type C', (262, 132): 'Type C', (270, 172): 'Type C', (268, 168): 'Type C', (261, 121): 'Type C', (295, 147): 'Type C', (254, 140): 'Type C', (274, 135): 'Type C', (294, 132): 'Type C', (275, 120): 'Type C', (292, 123): 'Type C', (250, 129): 'Type C', (295, 167): 'Type C', (262, 161): 'Type C', (265, 177): 'Type C', (263, 128): 'Type C', (257, 138): 'Type C', (264, 145): 'Type C', (267, 145): 'Type C', (268, 138): 'Type C', (258, 153): 'Type C', (287, 126): 'Type C', (272, 132): 'Type C', (288, 156): 'Type C', (287, 120): 'Type C', (291, 126): 'Type C', (293, 153): 'Type C', (287, 136): 'Type C', (285, 158): 'Type C', (281, 143): 'Type C', (258, 142): 'Type C', (295, 125): 'Type C', (269, 146): 'Type C', (267, 153): 'Type C', (291, 154): 'Type C', (267, 168): 'Type C', (280, 123): 'Type C', (299, 179): 'Type C', (255, 120): 'Type C', (296, 136): 'Type C', (298, 171): 'Type C', (257, 122): 'Type C', (292, 128): 'Type C', (260, 136): 'Type C', (290, 146): 'Type C', (269, 168): 'Type C', (275, 146): 'Type C', (260, 162): 'Type C', (277, 139): 'Type C', (296, 167): 'Type C', (251, 167): 'Type C', (277, 146): 'Type C', (268, 150): 'Type C', (261, 125): 'Type C', (291, 172): 'Type C', (254, 158): 'Type C', (275, 170): 'Type C', (298, 133): 'Type C', (279, 152): 'Type C', (295, 170): 'Type C', (275, 167): 'Type C', (299, 120): 'Type C', (259, 176): 'Type C', (282, 156): 'Type C', (256, 180): 'Type C', (292, 131): 'Type C', (269, 154): 'Type C', (295, 133): 'Type C', (273, 127): 'Type C', (285, 141): 'Type C', (268, 149): 'Type C', (286, 165): 'Type C', (291, 156): 'Type C', (287, 124): 'Type C', (279, 175): 'Type C', (270, 177): 'Type C', (265, 120): 'Type C'}'''
