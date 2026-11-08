import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def high_traffic_cycles(df, threshold=30):
    return df[df['Peak Congestion'] > threshold]

def emergency_summary(df):
    df['Emergency'] = df['Emergency'].apply(lambda x: tuple(x) if isinstance(x, list) else x)
    return df.groupby('Emergency').size().reset_index(name='Frequency')

def average_signal_duration(df):
    return df.groupby('Signal Direction')['Signal Duration'].mean()

def run_analysis(file_path):
    df = load_data(file_path)
    print("\nHigh-Traffic Cycles:")
    print(high_traffic_cycles(df))
    print("\nEmergency Summary:")
    print(emergency_summary(df))
    print("\nAverage Signal Duration Per Direction:")
    print(average_signal_duration(df))