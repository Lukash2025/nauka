from .space_vehicle_base import SpaceVehicleBase

class Rocket(SpaceVehicleBase):
    def __init__(self, fuel_level, thrust_power):
        self._fuel_level = fuel_level
        self.thrust_power = thrust_power

    def set_fuel_level(self, new_fuel_level):
        self._fuel_level = new_fuel_level

    def get_fuel_level(self):
        return self._fuel_level

    def launch_sequence(self):
        return f"Poziom paliwa: {self._fuel_level}, moc: {self.thrust_power}"