
# 🧩 AI Maze Solver: Pathfinding Comparison

A visual study comparing **Informed** vs. **Uninformed** search algorithms within a 10x10 grid environment.

## 📌 Project Overview

This repository contains a Python-based application that demonstrates how Artificial Intelligence algorithms navigate through obstacles to find the shortest path from a start point to a destination.

### 🧠 Implemented Algorithms

1. **A* Search (Informed):** Optimized using the Manhattan Distance heuristic.
2. **Breadth-First Search (BFS):** Explores all possibilities layer-by-layer to find the shortest path.
3. **Depth-First Search (DFS):** Follows a single path as deep as possible before backtracking.

---

## 🛠️ System Requirements

To run this project, you need the following Python libraries installed:

* **Streamlit:** For the web-based dashboard.
* **Matplotlib:** For rendering the maze grid.
* **Pandas:** For managing performance metrics.

---

## 🚀 Execution Instructions

Follow these steps to run the project on your local machine:

### 1. Install Dependencies

```bash
pip install streamlit matplotlib pandas

```

### 2. Prepare the Data

Run the script to generate the 10x10 maze structure:

```bash
python save_pkl.py

```

### 3. Launch the Application

Start the Streamlit server to view the interactive UI:

```bash
streamlit run app.py

```

---

## 📊 Performance Comparison

| Algorithm | Heuristic Used | Guaranteed Optimal? | Expansion Speed |
| --- | --- | --- | --- |
| **A*** | Manhattan | **Yes** | Very Fast |
| **BFS** | None | **Yes** | Moderate |
| **DFS** | None | No | Varies |
