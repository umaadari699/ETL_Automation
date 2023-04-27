class prgm:

    def printlist(self,matrix):
      list1 =[]
      print(len(matrix))  # length is 2 but as per o/p it should need 4 iterations
      for i in range(len(matrix[0])): # here i is 0 and length taking based on index
         list2 =[]
         for x in matrix: # x means [1,2,3,4]
             list2.append(x[i])
         list1.append(list2)
      print(list1)
 # convert this list as below output
 #[[1, 4], [2, 5], [3, 6], [4, 8]]

matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
p=prgm()
p.printlist(matrix)

