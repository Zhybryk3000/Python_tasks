"""Storage module for class Car, CarFabric and CarsHelperCalculationClass"""
from math import ceil
from random import randint
from typing import Union
import time


class Car:
    """ A class to represent a car """

    NEW_CAR_COST = 10000
    REPAIR_FOR_DIESEL_CAR = 700
    REPAIR_FOR_PETROL_CAR = 500
    MILEAGE_BEFORE_REPAIR_DIESEL = 150000
    MILEAGE_BEFORE_REPAIR_PETROL = 100000
    DIESEL_FUEL_COST = 1.8
    PETROL_FUEL_COST = 2.4
    FUEL_CONSUMPTION_DIESEL_ON_HUNDRED_KM = 0.06
    FUEL_CONSUMPTION_PETROL_ON_HUNDRED_KM = 0.08
    DECREASE_VALUE_DIESEL_PER_THOUSAND_KM = 105
    DECREASE_VALUE_PETROL_PER_THOUSAND_KM = 95
    DIESEL_ENGINE_TYPE = 'diesel'
    PETROL_ENGINE_TYPE = 'petrol'

    def __init__(self, engine: str, gas_tank: int):
        """
        :param engine: type engine in the car
        :param gas_tank: volume gas_tank in the car
        """
        assert engine in ('diesel', 'petrol'), f'Incorrect engine type: {engine}'
        assert gas_tank in (60, 75), f'Incorrect gas_tank type: {gas_tank}'
        self.engine = engine
        self.gas_tank = gas_tank
        self.mileage = randint(55_000, 286_000)

    def number_of_repairs(self) -> int:
        """
        Gets engine type and calculate repairs

        :return:number of repairs for car
        """
        number_of_repairs = Car.MILEAGE_BEFORE_REPAIR_DIESEL if self.engine == Car.DIESEL_ENGINE_TYPE else \
            Car.MILEAGE_BEFORE_REPAIR_PETROL
        return number_of_repairs // self.mileage

    def repair_cost(self) -> int:
        """
        Calculate repair cost depending on engine type

        :return:repair cost for car
        """
        number_of_repairs = Car.number_of_repairs(self)
        repair_cost = Car.REPAIR_FOR_DIESEL_CAR if self.engine == Car.DIESEL_ENGINE_TYPE else Car.REPAIR_FOR_PETROL_CAR
        return repair_cost * number_of_repairs

    def __method(self, fuel_consumption: Union[int, float], fuel_cost: Union[int, float]) -> Union[int, float]:
        """
        Gets param petrol or diesel car for help calculating fuel cost
        :param fuel_consumption:fuel consumption per hundred km
        :param fuel_cost: fuel cost for one liter
        :return:fuel cost
        """
        total_fuel_cost = 0
        kef = 0
        while True:
            if self.mileage > 1000:
                fuel_cost = fuel_consumption * 1000 * fuel_cost
                total_fuel_cost += fuel_cost + (fuel_cost * kef)
                kef += 0.01
                self.mileage -= 1000
            else:
                fuel_cost = fuel_consumption * self.mileage * fuel_cost
                total_fuel_cost += fuel_cost + (fuel_cost * kef)
                break
        return total_fuel_cost

    def fuel_cost(self) -> Union[int, float]:
        """
        Calculate fuel cost for cars after mileage

        :return:fuel cost with module round
        """
        if self.engine == Car.DIESEL_ENGINE_TYPE:
            return round(self.__method(Car.FUEL_CONSUMPTION_DIESEL_ON_HUNDRED_KM, Car.DIESEL_FUEL_COST))
        else:
            # For petrol car
            return round(self.__method(Car.FUEL_CONSUMPTION_PETROL_ON_HUNDRED_KM, Car.PETROL_FUEL_COST))

    def number_of_car_refueling(self) -> int:
        """
        Calculate refueling depending on gas_tank volume

        :return:number of car refueling
        """
        number_of_car_refueling = self.mileage / self.gas_tank
        time.sleep(0.3)
        return ceil(number_of_car_refueling)

    def used_car_cost(self) -> int:
        """
        Calculate car cost depending on mileage and engine type

        :return:car cost after mileage
        """
        if self.engine == Car.DIESEL_ENGINE_TYPE:
            used_car_cost = Car.NEW_CAR_COST - (Car.DECREASE_VALUE_DIESEL_PER_THOUSAND_KM * (self.mileage // 1000))
        else:
            # For petrol car
            used_car_cost = Car.NEW_CAR_COST - (Car.DECREASE_VALUE_PETROL_PER_THOUSAND_KM * (self.mileage // 1000))
        if used_car_cost <= 0:
            return 0
        else:
            return used_car_cost

    def mileage_before_disposal(self) -> Union[int, float]:
        """
        Gets used car cost and calculate time used cars before disposal

        :return:mileage before disposal
        """
        if self.engine == Car.DIESEL_ENGINE_TYPE:
            time_before_disposal = Car.used_car_cost(self) / (Car.DECREASE_VALUE_DIESEL_PER_THOUSAND_KM / 1000)
        else:
            # For petrol car
            time_before_disposal = Car.used_car_cost(self) / (Car.DECREASE_VALUE_PETROL_PER_THOUSAND_KM / 1000)
        return round(time_before_disposal)


class CarFabric:
    """Class for car making"""

    NUMBER_DIESEL_CAR = 3
    NUMBER_NON_STANDARD_GAS_TANK = 5
    VOLUME_STANDARD_GAS_TANK = 60
    VOLUME_NON_STANDARD_GAS_TANK = 75

    @classmethod
    def produce_cars(cls, number_of_produce: int) -> list:
        """
        Gets parameters of the car and make car depending on the car number
        :param number_of_produce: the number of cars to be created
        :return:list of object class Car
        """
        cars = []
        for i in range(number_of_produce):
            if i % CarFabric.NUMBER_DIESEL_CAR == 0 and i % CarFabric.NUMBER_NON_STANDARD_GAS_TANK == 0:
                cars.append(Car(Car.DIESEL_ENGINE_TYPE, CarFabric.VOLUME_NON_STANDARD_GAS_TANK))
            elif i % CarFabric.NUMBER_DIESEL_CAR == 0 and i % CarFabric.NUMBER_NON_STANDARD_GAS_TANK != 0:
                cars.append(Car(Car.DIESEL_ENGINE_TYPE, CarFabric.VOLUME_STANDARD_GAS_TANK))
            elif i % CarFabric.NUMBER_DIESEL_CAR != 0 and i % CarFabric.NUMBER_NON_STANDARD_GAS_TANK == 0:
                cars.append(Car(Car.PETROL_ENGINE_TYPE, CarFabric.VOLUME_NON_STANDARD_GAS_TANK))
            else:
                cars.append(Car(Car.PETROL_ENGINE_TYPE, CarFabric.VOLUME_STANDARD_GAS_TANK))
        return cars


class CarsHelperCalculationClass:
    """Class for calculate another tasks"""

    @staticmethod
    def sorted_diesel_cars(all_cars):
        """
        Method for sorting cars by engine type
        :return:list with diesel cars
        """
        diesel_car = []
        for car in all_cars:
            if car.engine == Car.DIESEL_ENGINE_TYPE:
                diesel_car.append(car)
        return diesel_car

    @staticmethod
    def sorted_petrol_cars(all_cars) -> list:
        """
        Method for sorting cars by engine type
        :return:list with petrol cars
        """
        petrol_car = []
        for car in all_cars:
            if car.engine == Car.PETROL_ENGINE_TYPE:
                petrol_car.append(car)
        return petrol_car

    @staticmethod
    def diesel_used_car_cost() -> list:
        """
        For sort the list with used diesel cars

        :return:list diesel used car cost
        """
        diesel_car_list = []  # list used car cost for diesel cars
        for i in CarsHelperCalculationClass.sorted_diesel_cars(cars_list):
            diesel_car_list.append(i.used_car_cost())
        result_list = [e for e in diesel_car_list if e > 0]
        result_list = sorted(result_list)
        return result_list

    @staticmethod
    def mileage_before_disposal_petrol_car() -> list:
        """
        For sort the list with used petrol cars

        :return: mileage before disposal for petrol cars
        """
        petrol_car_list = []  # list time before disposal for petrol cars
        for car in CarsHelperCalculationClass.sorted_petrol_cars(cars_list):
            petrol_car_list.append(car.mileage_before_disposal())
        result_list = [e for e in petrol_car_list if e > 0]
        result_list = sorted(result_list)
        return result_list

    @staticmethod
    def car_cost() -> int:
        """
        Calculate total cost all used cars

        :return: total car cost
        """
        car_list = []  # list with cost all cars
        for car in cars_list:
            car_list.append(car.used_car_cost())
        total_car_cost = 0
        for i in car_list:
            total_car_cost += i
        return total_car_cost


if __name__ == '__main__':
    cars_list = CarFabric.produce_cars(100)
    separate_task = CarsHelperCalculationClass()
    CarsHelperCalculationClass.sorted_diesel_cars(cars_list)

    my_car = Car('diesel', 60)
    print(my_car.mileage)
    print(my_car.number_of_repairs())
    print(my_car.repair_cost())
    print(my_car.number_of_car_refueling())
    print(my_car.used_car_cost())
    print(my_car.mileage_before_disposal())
    print(separate_task.diesel_used_car_cost())
    print(separate_task.mileage_before_disposal_petrol_car())
    print(separate_task.car_cost())
