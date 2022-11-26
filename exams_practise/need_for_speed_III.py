def add_cars(number):
    """
    adds cars with their mileage and fuel to a dictionary
    :param number: number of iterations/cars
    :return: returns the dictionary with all the cars
    """
    dictionary = {}
    for _ in range(number):
        car, mileage_as_str, fuel_as_str = input().split("|")
        mileage = int(mileage_as_str)
        fuel = int(fuel_as_str)
        dictionary[car] = {"MILEAGE": mileage, "FUEL": fuel}
    return dictionary


def drive_func(my_car, my_distance, my_fuel, cars):
    if cars[my_car]["FUEL"] < my_fuel:
        print("Not enough fuel to make that ride")
    else:
        cars[my_car]["FUEL"] -= my_fuel
        cars[my_car]["MILEAGE"] += my_distance
        print(f"{my_car} driven for {my_distance} kilometers. {my_fuel} liters of fuel consumed.")
        if cars[my_car]["MILEAGE"] >= 100000:
            print(f"Time to sell the {my_car}!")
            del cars[my_car]
        return cars


def refuel_func(my_car, my_fuel, dict):
    if dict[my_car]["FUEL"] + my_fuel > 75:
        filled = 75 - dict[my_car]["FUEL"]
        dict[my_car]["FUEL"] = 75
    else:
        filled = my_fuel
        dict[my_car]["FUEL"] += my_fuel
    print(f"{my_car} refueled with {filled} liters")
    return dict


def revert_func(my_car, my_kilometers, dict):
    if dict[my_car]["MILEAGE"] - my_kilometers < 10000:
        dict[my_car]["MILEAGE"] = 10000
    else:
        dict[my_car]["MILEAGE"] -= my_kilometers
        print(f"{my_car} mileage decreased by {my_kilometers} kilometers")
    return dict


number_of_cars = int(input())


def need_for_speed(number):
    cars = add_cars(number)
    while True:
        command = input()
        if command == "Stop":
            for k, v in cars.items():
                miles = v["MILEAGE"]
                fuel = v["FUEL"]
                print(f"{k} -> Mileage: {miles} kms, Fuel in the tank: {fuel} lt.")
            break

        split = command.split(" : ")
        action, car = split[:2]
        if action == "Drive":
            distance = int(split[2])
            fuel = int(split[3])
            drive_func(car, distance, fuel, cars)
        elif action == "Refuel":
            fuel = int(split[2])
            # Updates the cars dictionary and prints how much the car is filled with
            refuel_func(car, fuel, cars)
        elif action == "Revert":
            kilometers = int(split[2])
            revert_func(car, kilometers, cars)


need_for_speed(number_of_cars)
