import random
from math import ceil
# Использовал math в методе number_of_car_refueling для округления до болшего числа. Можно было и без него.
# Если модули лишний раз лучше не импортировать - дай знать.


class Car:

    New_car_cost = 10000
    Repair_for_diesel_car = 700
    Repair_for_petrol_car = 500
    Mileage_before_repair_diesel = 150_000
    Mileage_before_repair_petrol = 100_000
    Diesel_fuel_cost = 1.8
    Petrol_fuel_cost = 2.4
    Fuel_consumption_diesel_on_hundred_km = 6 / 100
    Fuel_consumption_petrol_on_hundred_km = 8 / 100
    Decrease_value_diesel_per_thousand_km = 105
    Decrease_value_petrol_per_thousand_km = 95

    def __init__(self, engine, gas_tank):
        assert engine in ('diesel', 'petrol'), f'Incorrect engine type: {engine}'
        assert gas_tank in (60, 75), f'Incorrect gas_tank type: {gas_tank}'
        self.engine = engine
        self.gas_tank = gas_tank
        self.mileage = random.randint(55_000, 286_000)

    # Пробег
    def car_mileage(self):
        mileage = self.mileage
        return mileage

    # Рассчитываем количество тех.обслуживаний машины
    def number_of_repairs(self):
        mileage = self.mileage
        number_of_repairs = 0
        if self.engine == 'diesel':
            number_of_repairs = mileage // Car.Mileage_before_repair_diesel
        elif self.engine == 'petrol':
            number_of_repairs = mileage // Car.Mileage_before_repair_petrol
        return number_of_repairs

    # Рассчитываем стоимость всех тех.обслуживаний
    def repair_cost(self):
        number_of_repairs = Car.number_of_repairs(self)
        repair_cost = 0
        if self.engine == 'diesel':
            repair_cost = Car.Repair_for_diesel_car * number_of_repairs
        elif self.engine == 'petrol':
            repair_cost = Car.Repair_for_petrol_car * number_of_repairs
        return repair_cost

    # Получился очень длинный метод для рассчёта стоимости бензина. Короче не придумал
    # Главная проблема в том, что расход увеличивается на 1% с каждой 1000 км. Поэтому много букв
    # В конце округлил до ближайшего целого числа
    def fuel_cost(self):
        mileage = self.mileage
        total_fuel_cost = 0
        kef = 0
        if self.engine == 'diesel':
            while True:
                if mileage > 1000:
                    fuel_cost = Car.Fuel_consumption_diesel_on_hundred_km * 1000 * Car.Diesel_fuel_cost
                    total_fuel_cost += fuel_cost + (fuel_cost * kef)
                    kef += 0.01
                    mileage -= 1000
                else:
                    fuel_cost = Car.Fuel_consumption_diesel_on_hundred_km * mileage * Car.Diesel_fuel_cost
                    total_fuel_cost += fuel_cost + (fuel_cost * kef)
                    break
        else:
            while True:
                if mileage > 1000:
                    fuel_cost = Car.Fuel_consumption_petrol_on_hundred_km * 1000 * Car.Petrol_fuel_cost
                    total_fuel_cost += fuel_cost + (fuel_cost * kef)
                    kef += 0.01
                    mileage -= 1000
                else:
                    fuel_cost = Car.Fuel_consumption_petrol_on_hundred_km * mileage * Car.Petrol_fuel_cost
                    total_fuel_cost += fuel_cost + (fuel_cost * kef)
                    break
        return round(total_fuel_cost)

    # Количество заправок автомобиля
    # Тут я принебрёг увеличением расхода на 1% за каждую 1000км
    # Машина столько не проедет, чтобы погрешность составила хотя бы одну заправку
    def number_of_car_refueling(self):
        mileage = self.mileage
        number_of_car_refueling = mileage / self.gas_tank
        number_of_car_refueling = ceil(number_of_car_refueling)
        return number_of_car_refueling

    # Остаточная стоимость автомобиля
    def used_car_cost(self):
        mileage = self.mileage
        used_car_cost = 0
        if self.engine == 'diesel':
            used_car_cost = Car.New_car_cost - (Car.Decrease_value_diesel_per_thousand_km * (mileage // 1000))
        elif self.engine == 'petrol':
            used_car_cost = Car.New_car_cost - (Car.Decrease_value_petrol_per_thousand_km * (mileage // 1000))
        if used_car_cost <= 0:
            return 0
        else:
            return used_car_cost

    # Сколько пробега осталось до утилизации
    def time_before_disposal(self):
        used_car_cost = Car.used_car_cost(self)
        time_before_disposal = 0
        if self.engine == 'diesel':
            time_before_disposal = used_car_cost / (Car.Decrease_value_diesel_per_thousand_km / 1000)
        elif self.engine == 'petrol':
            time_before_disposal = used_car_cost / (Car.Decrease_value_petrol_per_thousand_km / 1000)
        time_before_disposal = round(time_before_disposal)
        return time_before_disposal


# Класс для создания машин
class CarFabric:

    Number_diesel_car = 3  # Каждая 3-я машина - дизельная
    Number_non_standard_gas_tank = 5  # Каждая 5-ая машина с нестандартным бензобаком
    Standard_gas_tank = 60
    Non_standard_gas_tank = 75
    mileage = random.randint(55_000, 286_000)

    def __init__(self, number):
        assert type(number) == int, f'Incorrect engine type: {number}'
        self.car_number = number

    # В качестве переменных использовал атрибуты класса. Хз на сколько правильно. Выглядит нечитабельно
    def produce_cars(self):
        number = self.car_number
        cars = []
        for i in range(number):
            if i % CarFabric.Number_diesel_car == 0 and i % CarFabric.Number_non_standard_gas_tank == 0:
                cars.append(Car('diesel', CarFabric.Non_standard_gas_tank))
            elif i % CarFabric.Number_diesel_car == 0 and i % CarFabric.Number_non_standard_gas_tank != 0:
                cars.append(Car('diesel', CarFabric.Standard_gas_tank))
            elif i % CarFabric.Number_diesel_car != 0 and i % CarFabric.Number_non_standard_gas_tank == 0:
                cars.append(Car('petrol', CarFabric.Non_standard_gas_tank))
            else:
                cars.append(Car('petrol', CarFabric.Standard_gas_tank))
        return cars


number_of_cars = CarFabric(100)
# for car in number_of_cars.produce_cars():
# print(car.number_of_repairs())

cars_list = number_of_cars.produce_cars()
sorted_diesel_car = []
sorted_petrol_car = []
for car in cars_list:
    if car.engine == 'diesel':
        sorted_diesel_car.append(car)
    else:
        sorted_petrol_car.append(car)

# Дизельные машины с остаточной стоимостью
for car in sorted_diesel_car:
    print(car.used_car_cost(), end=' ')
print()

# Бензиновые машины. Время до утилизации
for car in sorted_petrol_car:
    print(car.time_before_disposal(), end=' ')
print()

# Суммарная стоимость машин в парке после пробега
total = []
for car in cars_list:
    total.append(car.used_car_cost())
result = 0
for numbers in total:
    result += numbers
print(result)
