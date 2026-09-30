# Temperature Control System
# EEE Mini Project - Python

class TemperatureController:

    def __init__(self, set_temperature):
        self.set_temperature = set_temperature
        self.temperature = 25.0

    def control(self):
        error = self.set_temperature - self.temperature

        if error > 1:
            action = "Heater ON"
            self.temperature += 2
        elif error < -1:
            action = "Heater OFF / Cooling"
            self.temperature -= 1
        else:
            action = "Temperature Stable"

        return action

    def simulate(self, steps):
        print("\nTemperature Control Simulation")
        print("--------------------------------")

        for i in range(1, steps + 1):
            action = self.control()

            print(
                f"Step {i}: "
                f"Temperature = {self.temperature:.1f} °C | "
                f"Action = {action}"
            )


# Main program
print("=== Temperature Control System ===")

set_temperature = float(input("Enter desired temperature (°C): "))

controller = TemperatureController(set_temperature)

controller.simulate(10)
