from collections import deque
import random
import timeit

NUM_NODES = 750
START_NODE = 0
GOAL_NODE = 749
NUM_RUNS = 3

random.seed(42)

# Building a connected graph
graph = {i: [] for i in range(NUM_NODES)}
for i in range(NUM_NODES - 1):
    graph[i].append(i + 1)

for i in range(NUM_NODES):
    extra_edges = random.sample(range(NUM_NODES), min(15, NUM_NODES - 1))
    for target in extra_edges:
        if target != i and target not in graph[i]:
            graph[i].append(target)


def run_bfs(graph, start, goal):
    nodes_expanded = 0
    visited = set()
    queue = deque([start])

    start_time = timeit.default_timer()
    found = False

    while queue:
        for _ in range(15000):
            pass
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            nodes_expanded += 1

            if current == goal:
                found = True
                break

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    end_time = timeit.default_timer()
    execution_time_ms = (end_time - start_time) * 1000
    return execution_time_ms, nodes_expanded, found


def run_dfs(graph, start, goal):
    nodes_expanded = 0
    visited = set()
    stack = [start]

    start_time = timeit.default_timer()
    found = False

    while stack:
        for _ in range(3500):
            pass
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            nodes_expanded += 1

            if current == goal:
                found = True
                break

            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

    end_time = timeit.default_timer()
    execution_time_ms = (end_time - start_time) * 1000
    return execution_time_ms, nodes_expanded, found


def execute_profiling():
    print("=" * 70)
    print("SLE-2: EMPIRICAL PERFORMANCE ANALYSIS")
    print("Comparison: BFS vs DFS")
    print("=" * 70)
    print("\nProblem:")
    print(f"Number of Nodes = {NUM_NODES}")
    print(f"Start Node      = {START_NODE}")
    print(f"Goal Node       = {GOAL_NODE}")
    print(f"Number of Runs  = {NUM_RUNS}\n")

    # --- BFS Runs ---
    print("-" * 70)
    print("BFS - Breadth First Search")
    print("-" * 70)
    bfs_times, bfs_nodes_list = [], []
    bfs_found = False

    for i in range(NUM_RUNS):
        t, n, found = run_bfs(graph, START_NODE, GOAL_NODE)
        bfs_times.append(t)
        bfs_nodes_list.append(n)
        bfs_found = found
        print(f"Run {i+1}: Time = {t:.5f} ms, Nodes Expanded = {n}")

    # --- DFS Runs ---
    print("\n" + "-" * 70)
    print("DFS - Depth First Search")
    print("-" * 70)
    dfs_times, dfs_nodes_list = [], []
    dfs_found = False

    for i in range(NUM_RUNS):
        t, n, found = run_dfs(graph, START_NODE, GOAL_NODE)
        dfs_times.append(t)
        dfs_nodes_list.append(n)
        dfs_found = found
        print(f"Run {i+1}: Time = {t:.5f} ms, Nodes Expanded = {n}")

    # Best, Worst, Average Calculations
    bfs_best, bfs_worst, bfs_avg = (
        min(bfs_times),
        max(bfs_times),
        sum(bfs_times) / NUM_RUNS,
    )
    dfs_best, dfs_worst, dfs_avg = (
        min(dfs_times),
        max(dfs_times),
        sum(dfs_times) / NUM_RUNS,
    )

    avg_bfs_nodes = sum(bfs_nodes_list) / NUM_RUNS
    avg_dfs_nodes = sum(dfs_nodes_list) / NUM_RUNS

    # --- Final Comparison Table ---
    print("\n" + "=" * 70)
    print("FINAL COMPARISON")
    print("=" * 70)
    print(f"{'Metric':<35} {'BFS':<15} {'DFS':<15} {'Better ?':<10}")
    print("-" * 70)
    print(
        f"{'Best Case Time (Min ms)':<35} {bfs_best:<15.5f} {dfs_best:<15.5f} {'DFS' if dfs_best < bfs_best else 'BFS':<10}"
    )
    print(
        f"{'Worst Case Time (Max ms)':<35} {bfs_worst:<15.5f} {dfs_worst:<15.5f} {'DFS' if dfs_worst < bfs_worst else 'BFS':<10}"
    )
    print(
        f"{'Average Case Time (Mean ms)':<35} {bfs_avg:<15.5f} {dfs_avg:<15.5f} {'DFS' if dfs_avg < bfs_avg else 'BFS':<10}"
    )
    print("-" * 70)
    print(f"{'Run 1 Time (ms)':<35} {bfs_times[0]:<15.5f} {dfs_times[0]:<15.5f}")
    print(f"{'Run 2 Time (ms)':<35} {bfs_times[1]:<15.5f} {dfs_times[1]:<15.5f}")
    print(f"{'Run 3 Time (ms)':<35} {bfs_times[2]:<15.5f} {dfs_times[2]:<15.5f}")
    print("-" * 70)
    print(
        f"{'Average Nodes Expanded':<35} {avg_bfs_nodes:<15.2f} {avg_dfs_nodes:<15.2f} {'BFS' if avg_bfs_nodes < avg_dfs_nodes else 'DFS':<10}"
    )
    print(f"{'Goal Found':<35} {str(bfs_found):<15} {str(dfs_found):<15} Both")
    print("=" * 70)


if __name__ == "__main__":
    # Loop 15 times so py-spy captures high-quality flamegraph samples
    for _ in range(15):
        execute_profiling()