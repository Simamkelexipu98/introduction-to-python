def main():

    consumption = get_energy_consumption()
    solar_production = get_solar_production()
    balance = calculate_energy_balance(consumption,solar_production)


    if balance >=0:
        print(f"Your household produced {balance} kwh more enegry than consumed!")
    else:
        print(f"Your household consumed {-balance} kwh more than it produced.")


def get_energy_consumption():

    try:
        consumption = float(input("Enter household enegry consumption in kwh: "))
        return consumption
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return get_energy_consumption()


def get_solar_production():

    try:
        hours_of_sunlight = float(input("Enter hours of sunlight today: "))
        panel_efficiency = float(input("Enter solar panel efficiency in kwh/hour: "))
        production = hours_of_sunlight * panel_efficiency
        return production
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return get_solar_production()

def calculate_energy_balance(consumption,production):
    return production-consumption


if __name__ == "__main__":
    main()
