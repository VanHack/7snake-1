
# 7Snake Problem
###### Ascent Software Challenge - Vanhackaton 4.0
---

The problem consists of finding two 7 cells long snakes in a grid, such as the sum of each snake's cells are equal. The full problem description can be read [here](https://docs.google.com/document/d/e/2PACX-1vRXHKuyB96RPcOuCHwVs_sBHYty3gMpjcwgi7hD7Lh1bJ4BbtAq3odvCxKCXHMw-8XiiXeHKSEn9ihq/pub)


My solution is constructed in the following steps:
* Load the grid from a csv file into a Numpy matrix
* Use recursion to generate all possible snake shapes respecting the problem restrictions
* Translate the shapes through the grid
* Store each snake found in a dictionary, for which the key is the value of the sum, and the value is a list of snakes (represented by its cells' coordinates) with that same sum
* For each snake found, test if there is already one snake with the same sum, not sharing any cell
* Stop the execution when a valid result is found, and store the result in a file called output.txt


To run the algorithm you will need:
(versions I used in development)
* Python 3.6.1
* Numpy 1.12.1


Type the command:


`python 7snake.py input_file delimiter`


Exemple:


`python 7snake.py example.csv ";"`


```python

```
