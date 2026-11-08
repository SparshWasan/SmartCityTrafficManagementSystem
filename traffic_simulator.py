import random
import numpy as np

def get_traffic_data():
    traffic_data = {
        'North': random.randint(0, 50),  # Density (units)
        'South': random.randint(0, 50),
        'East': random.randint(0, 50),
        'West': random.randint(0, 50),
        'Emergency': random.choice([
            None, 'North', 'South', 'East', 'West',
            ['North', 'South'], ['East', 'West'], 
            ['North', 'East'], ['North', 'West'], 
            ['South', 'East'], ['South', 'West']
        ])
    }

    densities = np.array([
        traffic_data['North'],
        traffic_data['South'],
        traffic_data['East'],
        traffic_data['West']
    ])
    traffic_data["Waiting Times"] = densities * 10 # if 1 unit of vehicle takes 10 seconds to pass
    traffic_data["Average Density"] = np.mean(densities)
    traffic_data["Peak Congestion"] = np.max(densities)
    return traffic_data

