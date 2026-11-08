import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def load_traffic_data(file_path):
    return pd.read_csv(file_path)

def plot_traffic_densities(df):
    cycles = df['Cycle']
    plt.plot(cycles, df['North'], label='North', marker='o')
    plt.plot(cycles, df['South'], label='South', marker='s')
    plt.plot(cycles, df['East'], label='East', marker='^')
    plt.plot(cycles, df['West'], label='West', marker='x')

    plt.title('Traffic Density Over Cycles')
    plt.xlabel('Cycle')
    plt.ylabel('Traffic Density')
    plt.legend(loc='upper right')
    plt.grid()
    #plt.show()
    st.pyplot(plt)

def plot_peak_congestion(df):
    plt.bar(df['Cycle'], df['Peak Congestion'], color='skyblue')

    plt.title('Peak Congestion Across Cycles')
    plt.xlabel('Cycle')
    plt.ylabel('Peak Congestion')
    plt.grid(axis='y')
    #plt.show()
    st.pyplot(plt)

def plot_signal_durations(df):
    durations = df.groupby('Signal Direction')['Signal Duration'].sum()

    durations.plot(kind='bar', color='orange')
    plt.title('Total Signal Duration per Direction')
    plt.xlabel('Direction')
    plt.ylabel('Total Signal Duration')
    plt.grid(axis='y')
    #plt.show() for main.py
    st.pyplot(plt) #for app.py