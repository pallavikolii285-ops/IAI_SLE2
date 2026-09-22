# SLE-2: Empirical Performance Analysis

## 1. AIM :

To experimentally compare the performance of Breadth First Search (BFS) and Depth First Search (DFS) using actual execution time and the number of nodes expanded.

---

## 2. Algorithms Used :

### BFS – Breadth First Search

BFS is an uninformed search algorithm that explores nodes level by level. It uses a queue to manage the nodes waiting to be explored.

### DFS – Depth First Search

DFS is an uninformed search algorithm that explores one path as deeply as possible before backtracking. It uses a stack to manage the nodes during the search.

---

## 3. Problem Configuration :

The same graph was used for both BFS and DFS.

- **Number of Nodes:** 750
- **Start Node:** 0
- **Goal Node:** 749
- **Number of Runs:** 3
- **Algorithms:** BFS and DFS

### Graph Structure :

Each node is connected to the next four available nodes.


0    →  1, 2, 3, 4
1    →  2, 3, 4, 5
2    →  3, 4, 5, 6
3    →  4, 5, 6, 7
4    →  5, 6, 7, 8
...
745  →  746, 747, 748, 749
746  →  747, 748, 749
747  →  748, 749
748  →  749
749  →  No next node

## 4. Profiling Method :

The performance of both algorithms was measured using Python's `timeit` module.

The following metrics were measured:

1. **Execution time in milliseconds** (Best Case, Worst Case, Average Case).
2. **Number of nodes expanded.**
3. **Goal-search success.**

Each algorithm was executed three times on the same graph structure. The average execution time was calculated from the three runs.

The number of expanded nodes was counted manually during the search.

---

## 5. Experimental Results :

| Metric | BFS | DFS | Better ? |
| :--- | :---: | :---: | :---: |
| **Best Case Time (Min ms)** | 32.19010 | 28.87720 | **DFS** |
| **Worst Case Time (Max ms)** | 33.35930 | 31.82900 | **DFS** |
| **Average Case Time (Mean ms)** | 32.67290 | 30.70167 | **DFS** |
| **Run 1 Time (ms)** | 32.19010 | 31.39880 | **DFS** |
| **Run 2 Time (ms)** | 33.35930 | 31.82900 | **DFS** |
| **Run 3 Time (ms)** | 32.46930 | 28.87720 | **DFS** |
| **Average Nodes Expanded** | **173.00** | 750.00 | **BFS** |
| **Goal Found** | **True** | **True** | **Both** |

---

## 6. Observation :

- **DFS** required less average execution time than BFS across all boundary metrics (Best Case, Worst Case, and Average Case).
- However, **BFS** expanded significantly fewer nodes (**173 nodes**) compared to DFS (**750 nodes**) to reach Goal Node 749.

---

## 7. Justification and Analysis :

Based on the measured results, DFS showed slightly lower execution times across Best Case (28.87720 ms), Worst Case (31.82900 ms), and Average Case (30.70167 ms) compared to BFS (32.67290 ms average).

However, BFS was vastly superior in terms of search space traversal efficiency, expanding only 173 nodes, whereas DFS expanded all 750 nodes.

Because each node connects to four consecutive nodes, BFS traverses level-by-level in steps of 4, allowing it to discover Node 749 in approximately:

$$\approx \frac{750}{4} = 187 \text{ steps (173 expanded nodes)}$$

DFS, on the other hand, follows the deepest branch first, traversing through all 750 nodes before reaching the goal.

Both algorithms successfully found the goal node in all runs. The comparison is based on actual measurements obtained using the `timeit` method.

---

## 8. Conclusion :

This profiling experiment helped in understanding the practical performance trade-offs between BFS and DFS.

Execution time and nodes expanded were measured using the same graph for both algorithms.

- **BFS** proved to be drastically superior in search space efficiency (nodes expanded).
- **DFS** showed slightly faster execution time due to minimal data structure overhead per iteration.

The experiment demonstrated the importance of empirical profiling along with theoretical analysis.

---

## 9. AI Contribution :

Gemini was used as an assistance tool during the development and documentation of this SLE-2.

AI assistance included:
* Preparing the BFS and DFS profiling code.
* Setting up execution-time measurement using `timeit`.
* Adding node-counting functionality.
* Setting up the sequential graph creation logic (`0 -> 1, 2, 3, 4`).
* Organizing the experimental results.
* Assisting with the structure and wording of the SLE-2 documentation.

*The program was executed by the student, and the actual experimental results were collected from the program execution.*

---

## 10. Project Files :

- `BFS_vs_DFS.py` – Python implementation of BFS and DFS with profiling.
- `README.md` – Project description, graph structure, profiling method, and experimental results.
- `AI_contribution_log.md` – Detailed record of AI assistance and student contribution.
- `SLE2_PRN_InaamIqbalMulla.docx` – Final SLE-2 profiling report.

---

## 11. Final Result :

- **BFS Best Case Time:** `32.19010 ms`  
- **DFS Best Case Time:** `28.87720 ms`  

- **BFS Worst Case Time:** `33.35930 ms`  
- **DFS Worst Case Time:** `31.82900 ms`  

- **BFS Average Case Time:** `32.67290 ms`  
- **DFS Average Case Time:** `30.70167 ms`  

- **BFS Average Nodes Expanded:** `173.00`  
- **DFS Average Nodes Expanded:** `750.00`  

- **BFS Goal Found:** `True`  
- **DFS Goal Found:** `True`  

> **Summary:** For this particular graph and experimental setup, BFS expanded drastically fewer nodes (173 vs 750), while DFS showed slightly lower execution time across Best, Worst, and Average cases.