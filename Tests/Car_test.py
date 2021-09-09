import unittest
from unittest import mock
from For_Andrey.task_3 import *


class CarTest(unittest.TestCase):
    """
    For memories
    @mock.patch('For_Andrey.task_3.randint', return_value=200000)
    def setUp(self, _):
        self.diesel_car = Car('diesel', 75, 1)
        self.petrol_car = Car('petrol', 60, 1)
    """

    @mock.patch('For_Andrey.task_3.randint', return_value=200000)
    def test_number_of_repairs(self, _):
        test_car = Car('diesel', 75, 1)
        actual_result = test_car.number_of_repairs()
        expected_result = 1
        self.assertEqual(actual_result, expected_result,
                         f'incorrect data between the actual and expected values')

    @mock.patch('For_Andrey.task_3.Car.number_of_repairs', return_value=2)
    def test_repair_cost(self, _):
        test_car = Car('diesel', 75, 1)
        actual_result = test_car.repair_cost()
        expected_result = 1400
        self.assertEqual(actual_result, expected_result,
                         f'incorrect data between the actual and expected values')

    @mock.patch('For_Andrey.task_3.randint', return_value=120000)
    def test_fuel_cost(self, _):
        test_car = Car('petrol', 60, 1)
        actual_result = test_car.fuel_cost()
        expected_result = 36749
        self.assertEqual(actual_result, expected_result,
                         f'incorrect data between the actual and expected values')

    @mock.patch('For_Andrey.task_3.randint', return_value=75000)
    def test_number_of_car_refueling(self, _):
        test_car = Car('petrol', 75, 1)
        actual_result = test_car.number_of_car_refueling()
        expected_result = 1000
        self.assertEqual(actual_result, expected_result,
                         f'incorrect data between the actual and expected values')

    @mock.patch('For_Andrey.task_3.randint', return_value=60000)
    def test_used_car_cost(self, _):
        test_car = Car('diesel', 75, 1)
        actual_result = test_car.used_car_cost()
        expected_result = 3700
        self.assertEqual(actual_result, expected_result,
                         f'incorrect data between the actual and expected values')

    @mock.patch('For_Andrey.task_3.randint', return_value=250000)
    def test_used_car_cost_without_zero(self, _):
        test_car = Car('diesel', 75, 1)
        actual_result = test_car.used_car_cost()
        expected_result = 0
        self.assertEqual(actual_result, expected_result,
                         f'incorrect data between the actual and expected values')

    @mock.patch('For_Andrey.task_3.Car.used_car_cost', return_value=2400)
    def test_mileage_before_disposal(self, _):
        test_car = Car('petrol', 60, 1)
        actual_result = test_car.mileage_before_disposal()
        expected_result = 25263
        self.assertEqual(actual_result, expected_result,
                         f'incorrect data between the actual and expected values')


class CarFabricTest(unittest.TestCase):

    def test_produce_cars(self):
        with self.assertRaises(ValueError) as e:
            CarFabric.produce_cars('123')
        # for memories
        self.assertEqual('Number of cars must be numbers', e.exception.args[0])

    def test_produce_cars_petrol_60(self):
        self.assertEqual(CarFabric.produce_cars(1)[0].engine, 'petrol', 'incorrect engine type of the car')
        self.assertEqual(CarFabric.produce_cars(1)[0].gas_tank, 60, 'incorrect gas_tank of the car')

    def test_produce_cars_petrol_75(self):
        self.assertEqual(CarFabric.produce_cars(5)[4].engine, 'petrol', 'incorrect engine type of the car')
        self.assertEqual(CarFabric.produce_cars(5)[4].gas_tank, 75, 'incorrect gas_tank of the car')

    def test_produce_cars_diesel_60(self):
        self.assertEqual(CarFabric.produce_cars(3)[2].engine, 'diesel', 'incorrect engine type of the car')
        self.assertEqual(CarFabric.produce_cars(3)[2].gas_tank, 60, 'incorrect gas_tank of the car')

    def test_produce_cars_diesel_75(self):
        self.assertEqual(CarFabric.produce_cars(15)[14].engine, 'diesel', 'incorrect engine type of the car')
        self.assertEqual(CarFabric.produce_cars(15)[14].gas_tank, 75, 'incorrect gas_tank of the car')


class CarsHelperCalculationClassTest(unittest.TestCase):

    def test_sort_cars_with_defined_engine_typ(self):
        test_car_1 = Car('diesel', 75, 1)
        test_car_2 = Car('petrol', 60, 2)
        car_list = [test_car_1, test_car_2]
        self.assertEqual(CarsHelperCalculationClass.sort_cars_with_defined_engine_type(car_list, 'diesel'),
                         [test_car_1], 'Sorting does not work')


if __name__ == '__main__':
    unittest.main()
