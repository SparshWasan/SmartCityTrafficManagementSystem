import streamlit as st
import pandas as pd
import time
from traffic_simulator import get_traffic_data
from signal_controller import EmergencyIntersection
from data_analysis import high_traffic_cycles, emergency_summary, average_signal_duration
import graphs

st.set_page_config(layout="wide")
if 'traffic_logs' not in st.session_state:
    st.session_state.traffic_logs = pd.DataFrame(columns=[
        'Cycle', 'North', 'South', 'East', 'West',
        'Emergency', 'Average Density', 'Peak Congestion', 'Signal Direction', 'Signal Duration'
    ])
    st.session_state.cycle = 1
st.title("🚦 Smart City Traffic Management System Dashboard")

if st.button("▶ Run Next Cycle"):
    traffic_data = get_traffic_data()
    junction = EmergencyIntersection(traffic_data)
    green_direction = junction.decide_signal()
    waiting_time = traffic_data["Waiting Times"][['North', 'South', 'East', 'West'].index(green_direction)]
    signal_duration = min(max(30, int(waiting_time / 10)), 60)

    st.subheader(f"Cycle {st.session_state.cycle} — Green Light: {green_direction}")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🚘 Peak Congestion", traffic_data["Peak Congestion"])
        st.metric("📊 Avg Density", round(traffic_data["Average Density"], 2))
        st.metric("🕒 Signal Duration", signal_duration)
    with col2:
        st.text("Traffic Data")
        st.dataframe(pd.DataFrame([traffic_data]))

    st.info(f"🟢 Green signal for {green_direction} — {signal_duration} sec")

    st.session_state.traffic_logs.loc[len(st.session_state.traffic_logs)] = {
        'Cycle': st.session_state.cycle,
        'North': traffic_data['North'],
        'South': traffic_data['South'],
        'East': traffic_data['East'],
        'West': traffic_data['West'],
        'Emergency': tuple(traffic_data['Emergency'] if isinstance(traffic_data['Emergency'], list) else [traffic_data['Emergency']]),
        'Average Density': traffic_data['Average Density'],
        'Peak Congestion': traffic_data['Peak Congestion'],
        'Signal Direction': green_direction,
        'Signal Duration': signal_duration
    }
    st.session_state.cycle += 1
    file_path = 'traffic_logs.csv'    
    st.session_state.traffic_logs.to_csv(file_path, index=False)
    st.success(f"Cycle {st.session_state.cycle - 1} logged and saved to {file_path}")
    #time.sleep(1)

st.subheader("📝 Traffic Logs")
st.dataframe(st.session_state.traffic_logs)
if not st.session_state.traffic_logs.empty:
    st.subheader("📈 Analysis")
    df = st.session_state.traffic_logs

    st.write("🔴 High Traffic Cycles")
    st.dataframe(high_traffic_cycles(df))

    st.write("🚨 Emergency Summary")
    st.dataframe(emergency_summary(df))

    st.write("⏱️ Avg Signal Duration per Direction")
    st.dataframe(average_signal_duration(df))

    st.write("📊 Plots")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Traffic Density")
        graphs.plot_traffic_densities(df)
    with col2:
        st.subheader("Peak Congestion")
        graphs.plot_peak_congestion(df)
    with col3:
        st.subheader("Signal Durations")
        graphs.plot_signal_durations(df)
