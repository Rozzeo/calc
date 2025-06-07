# import calculator
#
#
# if __name__ == '__main__':
#     calc = calculator.Calculator()
#     calc.add_car(
#         calculator.Car("Toyota",price=30000,fuel_economy=1200,insurance_cost=2500)),
#     calc.add_car(
#         calculator.ElectricCar("Toyota",200000,5500,1200,150)),
#     calc.add_car(
#         calculator.Car("Range Rover",670000,3,1200,2500))
#
#
#
#     calc.print_cars()
# # if __name__== '__main__'
# import calculator
#
# if __name__ == '__main__':
#     calc = calculator.Calculator()
#     # calc.add_car(calculator.Car("Toyota", price=30000, fuel_economy=7,service_cost=12000, insurance_cost=2500),
#     #              )
#     calc.add_car(calculator.ElectricCar("Toyota", 200000, 5500, 1200)
#                  )
#     calc.add_car(calculator.Car("Range Rover", 670000, 3, 1200, 2500))
#     calc.print_cars()
import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()

    # Adding cars
    calc.add_car(calculator.Car("Toyota", price=30000, fuel_economy=7, service_cost=1200, insurance_cost=2500))
    calc.add_car(calculator.ElectricCar("Tesla", price=200000, insurance_cost=5500, power_consumption=1200))
    calc.add_car(calculator.Car("Range Rover", price=670000, fuel_economy=3, service_cost=1200, insurance_cost=2500))

    # Printing results
    calc.print_cars()
