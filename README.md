# 🚦 Smart City Traffic Management System

A Python-based intelligent traffic control and simulation platform designed to dynamically optimize multi-directional intersection signal timings and prioritize emergency vehicles in real time. Built with an interactive **Streamlit** dashboard, **NumPy** simulation modeling, and **Pandas/Matplotlib** data analytics.

---

## 📌 Project Overview

Urban intersections often suffer from inefficient fixed-timer traffic signals, leading to unnecessary delays and impeding emergency service vehicles. 

This project simulates a four-way intersection (`North`, `South`, `East`, `West`) where:
1. **Dynamic Signal Allocation**: Signal durations (30s – 60s) scale dynamically based on real-time vehicle density and calculated waiting times.
2. **Emergency Vehicle Priority**: Emergency vehicles are detected and granted immediate green light clearance. When multiple emergencies occur simultaneously, priority is resolved based on the highest vehicle density.
3. **Real-time Logging & Analytics**: Every simulation cycle is logged into a CSV dataset, enabling on-the-fly congestion trend analysis and visual metrics via interactive charts.

---

## ✨ Features

- **Dynamic Signal Controller**:
  - Utilizes Object-Oriented Programming (OOP) inheritance (`Intersection` and `EmergencyIntersection`).
  - Prioritizes directions with maximum congestion or active emergency signals.
  - Dynamically calculates signal duration constrained between 30 and 60 seconds.
- **Traffic Simulator**:
  - Simulates randomized vehicle counts per direction (0–50 units).
  - Simulates single and multi-directional emergency events.
  - Generates waiting time calculations, average densities, and peak congestion metrics.
- **Interactive Web Dashboard (Streamlit)**:
  - Step-by-step cycle execution (`▶ Run Next Cycle`).
  - Real-time KPI metrics (Peak Congestion, Average Density, Signal Duration).
  - Live inspection table for current cycle telemetry.
- **Data Analysis & Visualization**:
  - High-traffic cycle detection (threshold filtering).
  - Emergency incident frequency breakdown.
  - Average and total signal duration per direction.
  - Line plots for multi-directional density over time.
  - Bar charts for peak congestion trends and direction duration distribution.

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Frontend / Dashboard:** [Streamlit](https://streamlit.io/)
- **Data Manipulation & Analysis:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Data Visualization:** [Matplotlib](https://matplotlib.org/)

---

## 📁 Project Structure

```plaintext
SmartCityTrafficManagementSystem/
│
├── app.py                  # Main Streamlit web application & UI dashboard
├── signal_controller.py    # OOP logic for intersection & emergency prioritization
├── traffic_simulator.py    # Traffic density generator & waiting time calculation
├── data_analysis.py        # Statistical queries (high traffic, emergencies, averages)
├── graphs.py               # Matplotlib plotting routines integrated into Streamlit
├── traffic_logs.csv        # Persisted cycle log history
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SparshWasan/SmartCityTrafficManagementSystem.git
   cd SmartCityTrafficManagementSystem
   ```

2. **Create and Activate a Virtual Environment (Optional but Recommended):**
   - **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Required Dependencies:**
   ```bash
   pip install streamlit pandas numpy matplotlib
   ```

---

## 🚀 Running the Application

Launch the Streamlit web dashboard:

```bash
streamlit run app.py
```

Once executed, open your browser and navigate to:
```text
http://localhost:8501
```

### Using the Dashboard:
1. Click **`▶ Run Next Cycle`** to simulate a new traffic snapshot.
2. Observe the assigned green light direction, calculated signal duration, and real-time metrics.
3. Review the updated **Traffic Logs** table and the **Data Analysis & Plots** at the bottom of the page.

---

## 🧠 System Architecture & Logic

### 1. Priority Resolution (`signal_controller.py`)
```
                          [ New Cycle ]
                               │
                    Are emergencies present?
                             /   \
                          Yes     No
                          /         \
    Multiple emergencies?           Select direction with
          /       \                 highest vehicle count
        Yes        No
        /            \
Prioritize lane with   Prioritize the single
highest vehicle count  emergency lane
```

### 2. Signal Timing Equation
$$\text{Duration} = \min\left(\max\left(30, \left\lfloor\frac{\text{Waiting Time}}{10}\right\rfloor\right), 60\right)$$

---

## 📊 Sample Output & Logging

Every cycle persists the following telemetry in `traffic_logs.csv`:
- **Cycle**: Incremental cycle counter
- **North, South, East, West**: Vehicle density (units) per lane
- **Emergency**: Active emergency direction(s) or `None`
- **Average Density**: Mean vehicle density across all 4 directions
- **Peak Congestion**: Maximum single-lane density
- **Signal Direction**: Lane granted green light
- **Signal Duration**: Allotted green signal time (seconds)

---