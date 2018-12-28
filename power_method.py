'''
This python script has one primary function called power_method(A, k) which takes in two arguments. The first is a matrix (square or rectangular) represented as a numpy array and the second is a positive integer representing the number of iterations run to approximate the limit.
'''

import numpy as np
import math
import copy

'''
 Written by: Allen and Jiachen (Amy) Liu
 Date: December 13th, 2018
 21-241 Project: Power Method for Approximating SVD

 This function aims to implement the Power Method to approximate the SVD
 decomposition on matrix A of m x n by taking it to a reasonably high kth
 power. This algorithm will not take inverses or limits that are highly
 expensive. Instead, the code will conduct matrix-vector multiplication
 (A^T)Ax (for a random vector x) for k iterations to approximate its limit
 that yields the eigen value and eigen vector for a rank 1 approximation.
 The rank 1 approximation is substracted from A and the algorithm repeats 
 to find all rank approximation until A becomes rank 0 (which occurs when
 trying to find a best rank approximation higher than the rank of the mat-
 rix). The algorithm will return an array of length m containing 3-tuple 
 of (singular value, right singular vector, left singular vector) in desc-
 ending order of singular values.
'''
def power_method(A, k):

  # create an array to be returned. It has the shape of A's number of rows
  # and contains 3-tuples of singular value (float), right singular
  # vector (object), left singular vector (object).
  res = np.empty(A.shape[0], dtype=('float ,object, object'))
  m = A.shape[0]

  for i in range(m): #calculating the ith singular value and left right vectors
    
    #constructing ATA
    Acopy = copy.deepcopy(A) #constructs a copy of input matrix as it is
                           #necessary to preserve it for future computations
    ATA = np.transpose(Acopy).dot(Acopy) #computes ATA
    # end of ATA construction

    # We choose a random vector so that the chances of it being orthogonal
    # to the eigenvectors of the matrix are slim
    v = np.random.rand(ATA.shape[1])
    for _ in range(k): #approximates the limit with k iterations
        temp = np.dot(ATA, v) #matrix-vector multiplication between (ATA)v
        v = temp / np.linalg.norm(temp) #normalizes the vector at each iteration
    # After a sufficient amount of iterations, the changes to v will become
    # increasingly less significant, which causes v to approach the limit
    # which is the eigenvector


    # Eigen value can be calculated through a simple process. First, we
    # calculate the dot product of ATA・v. We then calculate the dot 
    # product of (ATA・v)・v. By dividing by the ||v||^2 which can be 
    # attained by the dot product of v・v, we get the eigenvalue. This
    # is known as Reileigh's Quotient. Since we that the eigenvalue is
    # the singular value squared, we will take the square root.
    sval = math.sqrt(np.dot(ATA, v).dot(v) / np.dot(v,v))
    
    # The left singular vector is obtained by \frac{1}{σ}*A・v
    u = (1/sval)*A.dot(v)

    # Creates a 3-tuple with the order required by the project writeup
    res[i] = np.asarray((sval, np.ndarray.tolist(v), np.ndarray.tolist(u)),
                        dtype=('float ,object, object'))
    
    # Subtracts the best rank i approximation from A and goes onto calculate
    # the (i+1)th singular value and its left and right singular vectors
    A = A - sval*(np.dot(u.reshape(5,1),(np.transpose(v).reshape(1,10))))
  
  return res #returns an 1D array (size m) of 3-tuples 


def main():
   A = [[ 0.041,  0.815,  0.245,  0.054,  0.249,  0.534,  0.753,  0.307,  0.877,  0.429],
   [ 0.918,  0.846,  0.249,  0.262,  0.133,  0.32,   0.446,  0.122,  0.164,  0.711],
   [ 0.139,  0.701,  0.726,  0.094,  0.036,  0.695,  0.325,  0.29,   0.373,  0.692],
   [ 0.644,  0.067,  0.032,  0.896,  0.047,  0.55,   0.062,  0.568,  0.204,  0.275],
   [ 0.631,  0.412,  0.232,  0.415,  0.335,  0.508,  0.393,  0.549,  0.076,  0.698]]
   #print(power_method(np.array(A), 10))

   #print("************************************************8")
   print(np.linalg.svd(np.array(A)))

if __name__ == "__main__":
    main()