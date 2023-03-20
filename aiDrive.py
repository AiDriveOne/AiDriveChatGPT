class AIDrivenVehicle:
    def __init__(self, vehicle_type, max_speed):
        self.vehicle_type = vehicle_type
        self.max_speed = max_speed

    def ai_drive(self, speed):
        if speed > self.max_speed:
            print(f"Warning: Cannot drive at {speed} km/h. Maximum speed for this {self.vehicle_type} is {self.max_speed} km/h.")
            speed = self.max_speed

        print(f"Driving {self.vehicle_type} at {speed} km/h using AI control system.")

def main():
    vehicle_type = "car"
    max_speed = 120
    desired_speed = 80

    my_vehicle = AIDrivenVehicle(vehicle_type, max_speed)
    my_vehicle.ai_drive(desired_speed)

if __name__ == "__main__":
    main()
