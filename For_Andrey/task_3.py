from math import ceil
from random import randint
from typing import Union
print(randint.__doc__)
print(ceil.__doc__)
print(Union.__doc__)


class Car:
    """ A class to represent a car """

    NEW_CAR_COST = 10000
    REPAIR_FOR_DIESEL_CAR = 700
    REPAIR_FOR_PETROL_CAR = 500
    MILEAGE_BEFORE_REPAIR_DIESEL = 150_000
    MILEAGE_BEFORE_REPAIR_PETROL = 100_000
    DIESEL_FUEL_COST = 1.8
    PETROL_FUEL_COST = 2.4
    FUEL_CONSUMPTION_DIESEL_ON_HUNDRED_KM = 6 / 100
    FUEL_CONSUMPTION_PETROL_ON_HUNDRED_KM = 8 / 100
    DECREASE_VALUE_DIESEL_PER_THOUSAND_KM = 105
    DECREASE_VALUE_PETROL_PER_THOUSAND_KM = 95
    FIRST_ENGINE_TYPE = 'diesel'
    SECOND_ENGINE_TYPE = 'petrol'

    def __init__(self, engine: str, gas_tank: int):
        assert engine in ('diesel', 'petrol'), f'Incorrect engine type: {engine}'
        assert gas_tank in (60, 75), f'Incorrect gas_tank type: {gas_tank}'
        self.engine = engine
        self.gas_tank = gas_tank
        self.mileage = randint(55_000, 286_000)
        """
        :param engine: type engine in the car
        :param gas_tank: volume gas_tank in the car
        """

    def number_of_repairs(self) -> int:
        """
        Gets engine type and calculate repairs

        :return:number of repairs for car
        """
        if self.engine == Car.FIRST_ENGINE_TYPE:
            number_of_repairs = self.mileage // Car.MILEAGE_BEFORE_REPAIR_DIESEL
        else:
            # For petrol car
            number_of_repairs = self.mileage // Car.MILEAGE_BEFORE_REPAIR_PETROL
        return number_of_repairs

    def repair_cost(self) -> int:
        """
        Calculate repair cost depending on engine type

        :return:repair cost for car
        """
        number_of_repairs = Car.number_of_repairs(self)
        if self.engine == Car.FIRST_ENGINE_TYPE:
            repair_cost = Car.REPAIR_FOR_DIESEL_CAR * number_of_repairs
        else:
            # For petrol car
            repair_cost = Car.REPAIR_FOR_PETROL_CAR * number_of_repairs
        return repair_cost

    def fuel_cost(self) -> Union[int, float]:
        """
        Calculate fuel cost for cars after mileage

        :return:fuel cost with module round
        """
        mileage = self.mileage
        total_fuel_cost = 0
        kef = 0
        if self.engine == Car.FIRST_ENGINE_TYPE:
            while True:
                if mileage > 1000:
                    fuel_cost = Car.FUEL_CONSUMPTION_DIESEL_ON_HUNDRED_KM * 1000 * Car.DIESEL_FUEL_COST
                    total_fuel_cost += fuel_cost + (fuel_cost * kef)
                    kef += 0.01
                    mileage -= 1000
                else:
                    fuel_cost = Car.FUEL_CONSUMPTION_DIESEL_ON_HUNDRED_KM * mileage * Car.DIESEL_FUEL_COST
                    total_fuel_cost += fuel_cost + (fuel_cost * kef)
                    break
        else:
            # For petrol car
            while True:
                if mileage > 1000:
                    fuel_cost = Car.FUEL_CONSUMPTION_PETROL_ON_HUNDRED_KM * 1000 * Car.PETROL_FUEL_COST
                    total_fuel_cost += fuel_cost + (fuel_cost * kef)
                    kef += 0.01
                    mileage -= 1000
                else:
                    fuel_cost = Car.FUEL_CONSUMPTION_PETROL_ON_HUNDRED_KM * mileage * Car.PETROL_FUEL_COST
                    total_fuel_cost += fuel_cost + (fuel_cost * kef)
                    break
        return round(total_fuel_cost)

    def number_of_car_refueling(self) -> int:
        """
        Calculate refueling depending on gas_tank volume

        :return:number of car refueling
        """
        number_of_car_refueling = self.mileage / self.gas_tank
        return ceil(number_of_car_refueling)

    def used_car_cost(self) -> int:
        """
        Calculate car cost depending on mileage and engine type

        :return:car cost after mileage
        """
        if self.engine == Car.FIRST_ENGINE_TYPE:
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
        used_car_cost = Car.used_car_cost(self)
        if self.engine == Car.FIRST_ENGINE_TYPE:
            time_before_disposal = used_car_cost / (Car.DECREASE_VALUE_DIESEL_PER_THOUSAND_KM / 1000)
        else:
            # For petrol car
            time_before_disposal = used_car_cost / (Car.DECREASE_VALUE_PETROL_PER_THOUSAND_KM / 1000)
        return round(time_before_disposal)


class CarFabric:
    """
    Class for car making
    """

    NUMBER_DIESEL_CAR = 3
    NUMBER_NON_STANDARD_GAS_TANK = 5
    STANDARD_GAS_TANK = 60
    NON_STANDARD_GAS_TANK = 75

    def __init__(self, number: int):
        assert type(number) == int, f'Incorrect engine type: {number}'
        self.car_number = number
        """
        :param number: the number of cars will be created
        """

    def produce_cars(self) -> list:
        """
        Gets parameters of the car and make car depending on the car number

        :return:list of object class Car
        """
        cars = []
        for i in range(self.car_number):
            if i % CarFabric.NUMBER_DIESEL_CAR == 0 and i % CarFabric.NUMBER_NON_STANDARD_GAS_TANK == 0:
                cars.append(Car(Car.FIRST_ENGINE_TYPE, CarFabric.NON_STANDARD_GAS_TANK))
            elif i % CarFabric.NUMBER_DIESEL_CAR == 0 and i % CarFabric.NUMBER_NON_STANDARD_GAS_TANK != 0:
                cars.append(Car(Car.FIRST_ENGINE_TYPE, CarFabric.STANDARD_GAS_TANK))
            elif i % CarFabric.NUMBER_DIESEL_CAR != 0 and i % CarFabric.NUMBER_NON_STANDARD_GAS_TANK == 0:
                cars.append(Car(Car.SECOND_ENGINE_TYPE, CarFabric.NON_STANDARD_GAS_TANK))
            else:
                cars.append(Car(Car.SECOND_ENGINE_TYPE, CarFabric.STANDARD_GAS_TANK))
        return cars


number_of_cars = CarFabric(100)

if __name__ == '__main__':

    cars_list = number_of_cars.produce_cars()
    sorted_diesel_car = []
    sorted_petrol_car = []
    for car in cars_list:
        if car.engine == Car.FIRST_ENGINE_TYPE:
            sorted_diesel_car.append(car)
        else:
            sorted_petrol_car.append(car)

    diesel_car_list = []  # list used car cost for diesel cars
    for car in sorted_diesel_car:
        diesel_car_list.append(car.used_car_cost())

    def diesel_used_car_cost(cars: list) -> list:
        """
        For sort the list with used diesel cars

        :param cars:list with all used diesel cars
        :return:list diesel used car cost
        """
        result_list = [e for e in cars if e > 0]
        result_list = sorted(result_list)
        return result_list

    petrol_car_list = []  # list time before disposal for petrol cars
    for car in sorted_petrol_car:
        petrol_car_list.append(car.mileage_before_disposal())

    def mileage_before_disposal_petrol_car(cars: list) -> list:
        """
        For sort the list with used petrol cars

        :param cars: list with all used petrol cars
        :return: mileage before disposal for petrol cars
        """
        result_list = [e for e in cars if e > 0]
        result_list = sorted(result_list)
        return result_list

    car_list = []  # list with cost all cars
    for car in cars_list:
        car_list.append(car.used_car_cost())

    def car_cost(cars: list) -> int:
        """
        Calculate total cost all used cars

        :param cars: list with all used cars
        :return: total car cost
        """
        total_car_cost = 0
        for i in cars:
            total_car_cost += i
        return total_car_cost

    my_car = Car('diesel', 60)
    print(my_car.mileage)
    print(my_car.number_of_repairs())
    print(my_car.repair_cost())
    print(my_car.number_of_car_refueling())
    print(my_car.used_car_cost())
    print(my_car.mileage_before_disposal())
    print(diesel_used_car_cost(diesel_car_list))
    print(mileage_before_disposal_petrol_car(petrol_car_list))
    print(car_cost(car_list))

#  Спросить по list[type] в produce_cars
