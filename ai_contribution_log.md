# AI Contribution Log

## SLE-2: Empirical Performance Analysis


## 1. AI Tool Used :

**AI Tool:** Gemini

Gemini was used as a supporting tool during the development, profiling, and documentation of the SLE-2 experiment.

---

## 2. Purpose of AI Assistance :

AI assistance was used to support the preparation of the BFS and DFS profiling implementation, defining the sequential graph structure, setting up execution-time profiling across multiple boundaries, and organizing the experimental results and report.

---

## 3. Contribution of AI :

### Code Preparation

Gemini assisted with preparing the Python code for:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Graph creation (750 Nodes with sequential adjacency structure where each node connects to the next 4 available nodes)
- Node counting logic
- Execution-time measurement using Python's `timeit` module
- Multiple experimental runs (3 runs)
- Automated calculation of Best Case (Min), Worst Case (Max), and Average Case (Mean) execution times

### Graph Structure Documentation

Gemini assisted in documenting and formatting the exact structural connectivity of the graph environment:

0    →  1, 2, 3, 4
1    →  2, 3, 4, 5
2    →  3, 4, 5, 6
3    →  4, 5, 6, 7
...
745  →  746, 747, 748, 749
746  →  747, 748, 749
747  →  748, 749
748  →  749
749  →  No next node (Goal State)

### Profiling Setup :

Gemini assisted in setting up Python's `timeit` module (`timeit.repeat()`) for measuring precise algorithm execution time in milliseconds.

Manual node counting was also integrated into both BFS and DFS implementations to log the exact number of expanded nodes.

---

### Result Organization

Gemini helped organize the output into a comprehensive comparison table containing:

- Best Case execution time (Min ms)
- Worst Case execution time (Max ms)
- Average Case execution time (Mean ms)
- Run 1, Run 2, and Run 3 execution times
- Average nodes expanded
- Goal-found status

---

### Report Preparation

Gemini assisted in organizing the SLE-2 report into the required sections:

1. Algorithms / Versions Profiled
2. Profiling Method
3. Results
4. Justification & Analysis
5. AI Contribution Note
6. Conclusion

---

## 4. Student's Own Contribution :

The student:

- Understood the BFS and DFS search algorithms and their theoretical mechanics.
- Reviewed and executed the Python profiling code locally in VS Code.
- Executed benchmark runs for both algorithms on the 750-node graph.
- Collected actual measured timing and node expansion data across multiple runs.
- Checked and verified that both algorithms reached Goal Node 749 (`True`).
- Compared the measured execution times across Best, Worst, and Average cases.
- Used the actual results for the final analysis.
- Prepared and finalized all submission files.

---

## 5. Actual Experimental Results :

| Metric | BFS | DFS | Better ? |
|---|---:|---:|:---:|
| Best Case Time (Min ms) | 40.36780 | 36.97880 | DFS |
| Worst Case Time (Max ms) | 65.95430 | 45.30480 | DFS |
| Average Case Time (Mean ms) | 45.40981 | 39.30800 | DFS |
| Run 1 Time (ms) | 43.75460 | 36.97880 | DFS |
| Run 2 Time (ms) | 44.35240 | 39.24040 | DFS |
| Run 3 Time (ms) | 43.28450 | 37.27550 | DFS |
| Average Nodes Expanded | 173.00 | 750.00 | BFS |
| Goal Found | True | True | Both |

---

## 6. Result Interpretation :

For the 750-node sequential graph setup, DFS achieved lower execution times across Best Case (~36.97 ms), Worst Case (~45.30 ms), and Average Case (~39.30 ms) compared to BFS (~45.41 ms average).

However, BFS expanded significantly fewer nodes (173.00 nodes) compared to DFS (750.00 nodes) to reach Goal Node 749.

Both algorithms successfully found the goal node (`Goal Found = True`).

Therefore, BFS demonstrated superior search space efficiency in terms of node expansion, while DFS exhibited slightly faster raw execution times due to lower overhead in stack operations.

---

## 7. AI Usage Statement :

AI was used as an assistance tool for code preparation, profiling setup, graph connectivity documentation, explanation, and report organization.

The actual program execution and collection of performance results were performed by the student.

The final comparison and analysis were based on the actual measured experimental results.

---

## 8. Declaration :

> I have used AI assistance transparently for the tasks mentioned above and have verified the experimental results obtained from my program.