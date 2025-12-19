def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    num_str = d
    num_str = num_str.strip("$")
    num_float = float(num_str)
    return(num_float)



def percent_to_float(p):
    num_per = p
    num_per = num_per.strip("%")
    num_float = float(num_per)
    return(num_float/100)

main()
