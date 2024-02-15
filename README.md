# Foundations of Artificial Intelligence and Machine Learning

## Second week's homework

### BFS algorithm

An algorithm that finds the path to the end goal (that's unknown), creates a (backwards) path from start to end.

Time to find the solution: 
    **300x300:** 0.2692899703979492 sec;
    **600x600:** 1.2800841331481934 sec;
    **900x900:** 2.726066827774048 sec;

number of iterations to find the solution: 
    **300x300:** 47 233;
    **600x600:** 197 804;
    **900x900:** 450 414;

length of the solution in steps: 
    **300x300:** 300; 
    **600x600:** 600;
    **900x900:** 900;

### Greedy algorithm

An algorithm that finds the path to the end goal (that's known previously) using prioritizing. 

Time to find the solution: 
    **300x300:** 0.02541804313659668 sec;
    **600x600:** 0.05270791053771973 sec;
    **900x900:** 0.22244882583618164 sec;

number of iterations to find the solution: 
    **300x300:** 3 358;
    **600x600:** 6 293;
    **900x900:** 29 496;

length of the solution in steps: 
    **300x300:** 300;
    **600x600:** 600;
    **900x900:** 900;

### A* algorithm

An algorithm that finds the path to the end goal (that's known previously) prioritizing a path that seem to be leading closer to a goal. 

Time to find the solution: 
    **300x300:** 0.07017397880554199 sec
    **600x600:** 0.5386078357696533 sec
    **900x900:** 0.8762140274047852 sec

number of iterations to find the solution: 
    **300x300:** 8 202
    **600x600:** 60 472
    **900x900:** 93 999

length of the solution in steps: 
    **300x300:** 300
    **600x600:** 600
    **900x900:** 900

These results show that comparing execution time, the most effective algorithm, in this comparison, is Greedy algorithm. 
While Greedy is fastest, it may not always find the shortest path in all scenarios.
Path finding with BFS algorithm has the lowest score in every criterion. Although this algorithm has its benefits due to its simplicity.  
A* algorithm has an optimal balance: finds efficient paths relatively quickly.

This homework was done by Hanna Kätlin Ardel, using every bit of help that was available to get.
