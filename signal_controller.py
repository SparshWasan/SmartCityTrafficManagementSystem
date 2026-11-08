# signal_controller.py for single junction

class Intersection:
    def __init__(self, traffic_data):
        self.traffic_data = traffic_data  # dictionary

    def get_highest_traffic_direction(self):
        directions = ['North', 'South', 'East', 'West']
        return max(directions, key=lambda d: self.traffic_data[d])

    def decide_signal(self):
        direction = self.get_highest_traffic_direction()
        
        return direction
  
class EmergencyIntersection(Intersection):
    def decide_signal(self):
        emergencies = self.traffic_data.get('Emergency')
        if isinstance(emergencies, list):  # Multiple emergencies
            prioritized_emergency = max(emergencies, key=lambda d: self.traffic_data[d])
            print(f"🚨 Multiple emergencies detected! Prioritizing {prioritized_emergency}.")
            return prioritized_emergency
        elif emergencies in ['North', 'South', 'East', 'West']:  # Single emergency
            print(f"🚨 Emergency detected! Prioritizing {emergencies}.")
            return emergencies
        else:
            return super().decide_signal()