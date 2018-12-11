Euclidean distance score is a simple way of finding how similar two objects are by depicting the objects as points on a graph and checking how close they are using simple distance function, the euclidean distance or the well known pythagorean distance
So, if we have a set of points and we have to find if a given point is similar to any, just find the distance between the points and keep track of the least distance achieved, the closer the points are, more the similar
Its a very simple and intuitive implement and works well for small dataset with about 95-97 percent accuracy
The main disadvantage observed was that  we have to iterate through the whole dataset finding the minimum distance
Therefore its not practical for large dataset as it offers a time complexity 'n', 'n' being the size of the dataset
NOTE: This method can only be used for specific types of learning and programs and not all
