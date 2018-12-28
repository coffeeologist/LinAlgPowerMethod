# LinAlgPowerMethod

This project aims to implement the Power Method to approximate the singular value decomposition (SVD) on matrix A of m x n by taking it to a reasonably high kth power. 

## Getting Started
The power_method.py is the code for the power method. One can run with 
```
python power_method.py
```
The write up details the history, stakes, and mathematical concepts behind the power method incorporated into SVD.
The images svd1.png and pm1.png are output screenshots used for the write up. 


## Running the tests

Any matrix represented as a list of list will work for testing. The user can compare the result of the power_method with the results returned by numpy.linalg.svd (template is set up in the main method)

## Built With
Python and numpy

## Authors

* **Jiachen (Amy) Liu**
* **Allen Liu**

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE

## Acknowledgments

* Avrim Blum, John Hopcroft, and Ravindran Kannan, Foundations of Data Science, Cornell CS, Ithaca,
January 4, 2018.
* Edo Liberty, Lecture 7: Singular Value Decomposition, Yale University: 0368-3248-01-Algorithms in Data
Mining, Fall 2013.
* Rasmus Bro, Evrim Acar, and Tamara Kolda, Resolving the Sign Ambiguity in the Singular Value Decomposition, Technical Report SAND2007-6422, Sandia National Laboratories and United States Department
of Energy, New Mexico and California, October 2007.
* Carl Eckart and Gale Young, The Approximation of One Matrix By Another of Lower Rank, Psychometrika vol.1 (September 1936), no. 3, 211–218.
* Ron Larson, Bruce H. Edwards, and David C. Falvo, Elemantary Linear Algebra, 6th ed., Houghhton
Mifflin, Boston, January 1, 2008.
* The Scipy community, NumPy v1.15 Manual (August 23, 2018), https://docs.scipy.org/doc/
numpy-1.15.1/index.html. Accessed December 14, 2018. Specifically, the numpy.array, numpy.linalg
sections.
* Mary Radcliffe, Math 241: Final Project Options: Power Method, November 19, 2018. Cited for its claim
that SVD has a complexity of O(n^3).
