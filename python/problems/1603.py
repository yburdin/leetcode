from common import *


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking_dict = {1: big, 2: medium, 3: small}

    def add_car(self, car_type: int) -> bool:
        if self.parking_dict[car_type] > 0:
            self.parking_dict[car_type] -= 1
            return True
        else:
            return False


class TestParkingSystem(unittest.TestCase):
    def test_1603(self):
        parking_system = ParkingSystem(1, 1, 0)
        self.assertTrue(parking_system.add_car(1))
        self.assertTrue(parking_system.add_car(2))
        self.assertFalse(parking_system.add_car(3))
        self.assertFalse(parking_system.add_car(1))


if __name__ == '__main__':
    unittest.main()
