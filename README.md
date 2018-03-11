# Sequence-squares
A repository dedicated to hobbyist tinkering of the problem of "Can you arrange the sequence of strictly positive integers to N in a way such that any adjacent numbers sum to a perfect square"


Inspired by this numberphile video: 
<center>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=G1m7goLCJDY
" target="_blank"><img src="http://img.youtube.com/vi/G1m7goLCJDY/0.jpg" 
alt="The Square-Sum Problem: Numberphile " border="10" /></a>
</center>

## The Problem

The problem most simply can be stated:

Given the numbers from 1 to 15, arrange them in an order such that any two numbers that are consecutive in the resulting sequence add to a square number.

So if you were given the numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] a valid ordering of these nubmers would be [8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9]. In fact it's the only ordering of the numbers 1-15 that fit this criteria.

This problem can be reduced to the hamiltonian path problem: Given a graph G, can you find a path P such that every node in G is found in P exactly once. The Hamiltonian Path (and it's near relative the Hamiltonian Cycle problem) is NP-Complete, making solving the originally stated problem more difficult than it may appear to be.

The complexity of solving the problem is worse than exponential. So the larger the input size, the greater and greater the time it will take in expectation to find a solution.


## Initial Solution

I have started with a simple python script that will brute force solutions to an endpoint. It utilizes a recursive Hamiltonian Path finder and a randomization option that will yield more variance in the resulting paths.

Usage:
```
python3 calculate_sequence.py 40 1
```

The first command line parameter, 40, is the last size of the sequence to find.
The second command line parameter, 1, denotes that the program should randomize the list of numbers before attempting to solve the hamiltonian path.

The resulting output is as follows:

```
1 [1]
1: 0.00 Seconds
15 [8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9]
15: 0.00 Seconds
16 [8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9, 16]
16: 0.00 Seconds
17 [17, 8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9, 16]
17: 0.00 Seconds
23 [2, 23, 13, 12, 4, 21, 15, 10, 6, 19, 17, 8, 1, 3, 22, 14, 11, 5, 20, 16, 9, 7, 18]
23: 0.00 Seconds
25 [9, 16, 20, 5, 4, 21, 15, 10, 6, 19, 17, 8, 1, 3, 22, 14, 11, 25, 24, 12, 13, 23, 2, 7, 18]
25: 0.10 Seconds
26 [4, 21, 15, 1, 8, 17, 19, 6, 10, 26, 23, 2, 14, 22, 3, 13, 12, 24, 25, 11, 5, 20, 16, 9, 7, 18]
26: 0.05 Seconds
27 [25, 24, 12, 4, 21, 15, 1, 8, 17, 19, 6, 10, 26, 23, 13, 3, 22, 27, 9, 16, 20, 5, 11, 14, 2, 7, 18]
27: 0.03 Seconds
28 [24, 25, 11, 14, 22, 27, 9, 16, 20, 5, 4, 12, 13, 3, 1, 15, 21, 28, 8, 17, 19, 6, 10, 26, 23, 2, 7, 18]
28: 0.68 Seconds
29 [3, 13, 12, 4, 5, 11, 25, 24, 1, 15, 21, 28, 8, 17, 19, 6, 10, 26, 23, 2, 14, 22, 27, 9, 16, 20, 29, 7, 18]
29: 1.72 Seconds
30 [25, 11, 5, 4, 21, 28, 8, 17, 19, 30, 6, 3, 13, 12, 24, 1, 15, 10, 26, 23, 2, 14, 22, 27, 9, 16, 20, 29, 7, 18]
30: 4.05 Seconds
31 [12, 13, 3, 22, 27, 9, 16, 20, 29, 7, 18, 31, 5, 4, 21, 28, 8, 17, 19, 30, 6, 10, 15, 1, 24, 25, 11, 14, 2, 23, 26]
31: 0.58 Seconds
32 [21, 28, 8, 1, 15, 10, 6, 30, 19, 17, 32, 4, 5, 31, 18, 7, 29, 20, 16, 9, 27, 22, 3, 13, 12, 24, 25, 11, 14, 2, 23, 26]
32: 1.43 Seconds
33 [24, 25, 11, 5, 20, 29, 7, 18, 31, 33, 16, 9, 27, 22, 14, 2, 23, 13, 12, 4, 32, 17, 19, 30, 6, 3, 1, 8, 28, 21, 15, 10, 26]
33: 2.81 Seconds
34 [18, 7, 9, 27, 22, 14, 2, 34, 15, 21, 28, 8, 1, 3, 13, 23, 26, 10, 6, 30, 19, 17, 32, 4, 12, 24, 25, 11, 5, 31, 33, 16, 20, 29]
34: 3.74 Seconds
35 [26, 23, 2, 7, 18, 31, 33, 16, 9, 27, 22, 14, 35, 29, 20, 5, 11, 25, 24, 12, 13, 3, 6, 10, 15, 1, 8, 28, 21, 4, 32, 17, 19, 30, 34]
35: 3.33 Seconds
36 [2, 23, 26, 10, 6, 3, 22, 27, 9, 16, 33, 31, 18, 7, 29, 20, 5, 4, 32, 17, 8, 1, 35, 14, 11, 25, 24, 12, 13, 36, 28, 21, 15, 34, 30, 19]
36: 17.22 Seconds
37 [17, 8, 1, 15, 34, 30, 19, 6, 10, 26, 23, 2, 7, 18, 31, 33, 16, 9, 27, 37, 12, 24, 25, 11, 5, 20, 29, 35, 14, 22, 3, 13, 36, 28, 21, 4, 32]
37: 7.81 Seconds
38 [11, 38, 26, 10, 6, 19, 30, 34, 15, 1, 8, 17, 32, 4, 21, 28, 36, 13, 23, 2, 7, 18, 31, 5, 20, 29, 35, 14, 22, 3, 33, 16, 9, 27, 37, 12, 24, 25]
38: 8.84 Seconds
39 [29, 35, 14, 22, 27, 9, 7, 18, 31, 33, 16, 20, 5, 11, 38, 26, 23, 2, 34, 30, 19, 6, 3, 13, 36, 28, 21, 4, 32, 17, 8, 1, 15, 10, 39, 25, 24, 12, 37]
39: 4.20 Seconds
40 [23, 13, 12, 37, 27, 9, 40, 24, 25, 39, 10, 26, 38, 11, 5, 4, 32, 17, 8, 1, 35, 29, 20, 16, 33, 31, 18, 7, 2, 14, 22, 3, 6, 19, 30, 34, 15, 21, 28, 36]
40: 93.42 Seconds
1: Yes
2: No
3: No
4: No
5: No
6: No
7: No
8: No
9: No
10: No
11: No
12: No
13: No
14: No
15: Yes
16: Yes
17: Yes
18: No
19: No
20: No
21: No
22: No
23: Yes
24: No
25: Yes
26: Yes
27: Yes
28: Yes
29: Yes
30: Yes
31: Yes
32: Yes
33: Yes
34: Yes
35: Yes
36: Yes
37: Yes
38: Yes
39: Yes
40: Yes
```


## Future Work
My actual research relies heavily on parallel programming. A brute force approach can easily be parallelized and clever use of MPI can lead to speedup even in dynamic programming approaches. I hope to rewrite this program in C utilizing MPI for coordination of workers and yield faster and larger solutions. 
