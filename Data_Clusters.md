###Data clustering

Data clustering is a way for a program to group similar data on a graph
Consider this image 
![cluster](/temp/cluster.png)

Here our brain tells us that there are four clusters, or three groups, and its safe to assume that the members of these groups have something in common. Therefore if the clusters in a dataset are identified and named by a program,and when new data is given, the program can figure out in which cluster it belongs to and approximate its properties based on the properties of that cluster


##Heirarchial clustering
This is a type of unsupervised learning, where we write an algorithm for the program to identify clusters. The program doesnt know how many clusters are there, and will classify the given data into a respective cluster
#Basic Algorithm
1)Consider each element as a cluster
2)Find two clusters which are the closest
3)Merge the clusters found in step 2
4)Repeat Step 2 and 3 until there is only one cluster left

Note: There are three ways to find the distance between two clusters:
      1]Single linkage: Distance between the closet elements in both the clusters
      2]Complete linkage: Distance between the farthest elements in both the clusters
      3]Average linkage: Average distance of all the points in the two clusters
      4]Centroid linkage: Distance between the centroid of the two clusters


