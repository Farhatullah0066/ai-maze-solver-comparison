
import streamlit as st

# 1. Sidebar for Global Settings
st.sidebar.title("Maze Settings")

# Dropdown for Algorithm Selection
algo_choice = st.sidebar.selectbox(
    "Select Algorithm", 
    ("A*", "BFS", "DFS")
)

# Numeric Input for Start and Goal Coordinates
st.sidebar.subheader("Set Positions")
start_x = st.sidebar.number_input("Start X", 0, 9, 1)
start_y = st.sidebar.number_input("Start Y", 0, 9, 1)

goal_x = st.sidebar.number_input("Goal X", 0, 9, 8)
goal_y = st.sidebar.number_input("Goal Y", 0, 9, 8)

# 2. Main Area for Action
if st.button("🚀 Start Solving"):
    st.write(f"Running {algo_choice} from ({start_x}, {start_y}) to ({goal_x}, {goal_y})...")
    # Here you would call your actual search functions






import streamlit as st
import pickle
import collections
import heapq
import time
import matplotlib.pyplot as plt
import pandas as pd

# --- LOAD DATA FROM PKL ---
try:
    with open('maze_data.pkl', 'rb') as f:
        data = pickle.load(f)
    MAZE = data["maze"]
    START = data["start_pos"]
    GOAL = data["goal_pos"]
except FileNotFoundError:
    st.error("Please run the save_pkl.py script first to generate maze_data.pkl!")
    st.stop()

# --- ALGORITHM LOGIC (From your Project) ---
def get_neighbors(r, c):
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(MAZE) and 0 <= nc < len(MAZE[0]) and MAZE[nr][nc] != 1:
            neighbors.append((nr, nc))
    return neighbors

def reconstruct_path(parent, goal, start):
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    return path[::-1]

def a_star_search(start, goal):
    pq = [(0, 0, start)] 
    parent = {start: None}
    g_cost = {start: 0}
    nodes_expanded = 0
    while pq:
        nodes_expanded += 1
        f, g, current = heapq.heappop(pq)
        if current == goal:
            return reconstruct_path(parent, goal, start), nodes_expanded
        for neighbor in get_neighbors(*current):
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                heapq.heappush(pq, (f, new_g, neighbor))
                parent[neighbor] = current
    return None, nodes_expanded

def bfs_search(start, goal):
    queue = collections.deque([start])
    parent = {start: None}
    visited = {start}
    nodes_expanded = 0
    while queue:
        nodes_expanded += 1
        current = queue.popleft()
        if current == goal:
            return reconstruct_path(parent, goal, start), nodes_expanded
        for neighbor in get_neighbors(*current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return None, nodes_expanded

# --- STREAMLIT UI LAYOUT ---
st.set_page_config(page_title="Maze Solver UI", layout="wide")
st.title("🧩 AI Maze Solver Dashboard")
st.markdown("Comparing **BFS** vs **A*** based on path efficiency and node expansion.")

# Sidebar for Controls
st.sidebar.header("Settings")
run_btn = st.sidebar.button("Run Algorithms")

if run_btn:
    # Execution and Analysis
    results = []
    solvers = [("A* Search", a_star_search), ("BFS Search", bfs_search)]
    
    cols = st.columns(2)
    
    for i, (name, func) in enumerate(solvers):
        start_time = time.time()
        path, nodes = func(START, GOAL)
        runtime = time.time() - start_time
        
        results.append({
            "Algorithm": name, 
            "Steps": len(path)-1 if path else 0, 
            "Nodes Expanded": nodes, 
            "Time (s)": round(runtime, 6)
        })

        with cols[i]:
            st.subheader(f"Visualization: {name}")
            
            # Visualization Logic
            vis_maze = [row[:] for row in MAZE]
            color_map = {0: 1.0, 1: 0.0, 2: 0.5, 3: 0.7, 4: 0.3}
            if path:
                for r, c in path:
                    if (r, c) != START and (r, c) != GOAL:
                        vis_maze[r][c] = 4
            
            plot_data = [[color_map[cell] for cell in row] for row in vis_maze]
            fig, ax = plt.subplots()
            ax.imshow(plot_data, cmap='viridis')
            ax.axis('off')
            st.pyplot(fig)
            
            st.write(f"✅ **Path found in {len(path)-1} steps**")

    # Comparative Analysis Table
    st.divider()
    st.subheader("📊 Comparative Analysis")
    st.table(pd.DataFrame(results))
    
    # Visualization Comparison
    st.bar_chart(pd.DataFrame(results).set_index("Algorithm")["Nodes Expanded"])
else:
    st.info("Click 'Run Algorithms' in the sidebar to start the comparison.")