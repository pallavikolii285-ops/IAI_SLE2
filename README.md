# SLE-2: Profiling Report
## Empirical Performance Analysis of BFS and DFS

### Course
02AML204 – Introduction to Artificial Intelligence

### Experiment
Empirical Performance Analysis

---

## 1. Aim

The aim of this experiment is to experimentally compare the performance of Breadth First Search (BFS) and Depth First Search (DFS) on the same graph.

The comparison is based on actual execution time and the number of nodes expanded by each algorithm.

Python's `timeit` module is used for execution-time measurement and `py-spy` is used for profiling and generating a flame graph.

---

## 2. Algorithms / Versions Profiled

### Algorithm A: Breadth First Search (BFS)

BFS explores the graph level by level. It uses a queue to store nodes that are waiting to be explored.

### Algorithm B: Depth First Search (DFS)

DFS explores one branch deeply before backtracking. It uses a stack to store nodes that are waiting to be explored.

Both algorithms were tested on the same graph with the same starting and goal nodes.

---

## 3. Problem Configuration

The experiment uses a small graph containing 20 nodes.

- Number of Nodes: 20
- Start Node: 0
- Goal Node: 19
- Number of Runs: 3
- Repetitions per Run: 1000
- Programming Language: Python

The same graph and same start and goal nodes were used for both BFS and DFS to make the experimental comparison fair.

---

## 4. Profiling Method

Python's `timeit` module was used to measure the execution time.

Each algorithm was executed for 3 runs. In every run, the search operation was repeated 1000 times so that the measured execution time was large enough for practical comparison.

The following measurements were collected:

1. Execution time in milliseconds.
2. Number of nodes expanded.
3. Average execution time over 3 runs.

The program was also profiled using `py-spy`. The profiling generated a flame graph named `profile.svg`.

---

## 5. Experimental Results

The following results were obtained from the actual execution of the Python program.

| Run | BFS Time (ms) | BFS Nodes | DFS Time (ms) | DFS Nodes |
|---|---:|---:|---:|---:|
| 1 | 8.63200 | 20 | 3.87470 | 6 |
| 2 | 12.28480 | 20 | 4.06690 | 6 |
| 3 | 7.43880 | 20 | 5.12350 | 6 |

### Average Results

| Metric | BFS | DFS |
|---|---:|---:|
| Average Execution Time (ms) | 9.45187 | 4.35503 |
| Average Nodes Expanded | 20.00 | 6.00 |
| Goal Found | True | True |

The measured execution time represents 1000 repeated searches in each run.

---

## 6. Observation

Both BFS and DFS successfully reached the goal node 19 from the starting node 0.

For the selected graph, BFS expanded an average of 20 nodes, whereas DFS expanded an average of 6 nodes.

The measured average execution time was 9.45187 ms for BFS and 4.35503 ms for DFS.

The results show that the practical execution time and number of nodes explored can differ depending on the graph structure and the position of the goal node.

---

## 7. Justification and Analysis

BFS explores nodes level by level using a queue. In the selected graph, the goal node was reached after exploring more nodes, resulting in 20 expanded nodes.

DFS explores a branch deeply before backtracking. For this particular graph and goal position, DFS reached the goal after expanding only 6 nodes.

The measured average execution time was also different for the two algorithms. BFS required 9.45187 ms for the 1000 repeated searches, while DFS required 4.35503 ms.

These results are specific to the selected graph, start node and goal node. A different graph structure or goal position can produce different results.

As the problem size increases, the number of explored nodes and execution time may also increase depending on the search strategy and graph structure.

---

## 8. Py-spy Profiling

The program was profiled using the `py-spy` tool.

The following command was used to generate the flame graph:

    py-spy record -o profile.svg -- python dfs_vs_bfs.py

The generated file is:

    profile.svg

The flame graph provides a visual representation of where the program spends its execution time.

The profiling completed successfully with 0 errors and generated the flame graph data.

---

## 9. AI Contribution

AI assistance was used during the development of this experiment.

AI helped with:

- Understanding the SLE-2 profiling requirements.
- Structuring the BFS and DFS experiment.
- Preparing the graph representation.
- Adding node expansion counting.
- Adding execution-time measurement using `timeit`.
- Organizing the experimental output.
- Preparing the README documentation.
- Understanding the use of `py-spy`.

The student performed the actual execution of the program, collected the terminal results, generated the `py-spy` flame graph and updated the GitHub repository.

---

## 10. Files in the Repository

### dfs_vs_bfs.py

Contains the Python implementation of BFS and DFS along with execution-time measurement and node counting.

### README.md

Contains the description of the experiment, methodology, results, observation and analysis.

### ai_contribution_log.md

Contains the record of AI assistance and the student's contribution.

### profile.svg

Contains the flame graph generated using `py-spy`.

---

## 11. Conclusion

BFS and DFS were successfully implemented and experimentally evaluated on the same 20-node graph.

The experiment measured execution time and the number of nodes expanded using actual program execution.

For the selected graph, both algorithms successfully reached the goal node. The experiment also demonstrated how profiling tools such as `timeit` and `py-spy` can be used to study the practical performance of search algorithms.

The results also show that theoretical complexity alone does not describe the complete practical behaviour of an algorithm; actual execution depends on the graph structure, search path and implementation.