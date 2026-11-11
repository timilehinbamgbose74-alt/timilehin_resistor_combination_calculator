# Resistor Combination Calculator
# Calculates total resistance for resistors in series and in parallel.
# Author: Timilehin Bamgbose
# ND Mechatronics Engineering, YabaTech

def get_positive_float(prompt):
    """
    Asks the user for a number and keeps asking until a valid positive float is entered.
    Returns the float value.
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value <= 0:
                print("Please enter a positive number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number (e.g. 100 or 4.7).")


def calculate_series(resistors):
    """
    Calculates the total resistance of resistors connected in series.
    Series total = R1 + R2 + R3 + ...
    Returns the total resistance.
    """
    total = 0.0
    for r in resistors:
        total = total + r
    return total


def calculate_parallel(resistors):
    """
    Calculates the total resistance of resistors connected in parallel.
    1/Rtotal = 1/R1 + 1/R2 + 1/R3 + ...
    Returns the total resistance.
    """
    reciprocal_sum = 0.0
    for r in resistors:
        reciprocal_sum = reciprocal_sum + (1.0 / r)
    if reciprocal_sum == 0:
        return 0.0
    return 1.0 / reciprocal_sum


def main():
    print("=" * 50)
    print("   RESISTOR COMBINATION CALCULATOR")
    print("=" * 50)
    print("This program calculates total resistance")
    print("for resistors in SERIES and in PARALLEL.")
    print()

    # Get number of resistors
    while True:
        try:
            num = int(input("How many resistors do you have? "))
            if num < 1:
                print("You need at least 1 resistor.")
            else:
                break
        except ValueError:
            print("Please enter a whole number (e.g. 3).")

    # Store resistor values in a list
    resistors = []
    print()
    print("Enter the resistance of each resistor in ohms (Ω):")
    for i in range(num):
        # Prompt like "Resistor 1: "
        value = get_positive_float(f"  Resistor {i + 1}: ")
        resistors.append(value)

    # Calculate both combinations
    series_total = calculate_series(resistors)
    parallel_total = calculate_parallel(resistors)

    # Display results
    print()
    print("-" * 50)
    print("RESULTS")
    print("-" * 50)
    print(f"Number of resistors : {num}")
    print(f"Values (Ω)          : {resistors}")
    print()
    print(f"Series total        : {series_total:.4f} Ω")
    print(f"Parallel total      : {parallel_total:.4f} Ω")
    print("-" * 50)

    # ===== MY OWN TWIST =====
    # After calculating the totals, ask for a supply voltage
    # and show the current that would flow in series and parallel.
    print()
    print("EXTRA FEATURE: Current calculation")
    print("If you apply a voltage across the combination,")
    print("the program can also show the current (I = V / R).")
    print()

    choice = input("Do you want to calculate current for a given voltage? (y/n): ").strip().lower()
    if choice == "y" or choice == "yes":
        voltage = get_positive_float("Enter the supply voltage in volts (V): ")
        series_current = voltage / series_total
        parallel_current = voltage / parallel_total
        print()
        print(f"At {voltage} V:")
        print(f"  Current in SERIES combination   : {series_current:.4f} A")
        print(f"  Current in PARALLEL combination : {parallel_current:.4f} A")
        print()
        print("Note: Parallel always draws more current for the same voltage")
        print("because its total resistance is lower.")
    else:
        print("Skipped current calculation. Goodbye!")

    print()
    print("Thank you for using the Resistor Combination Calculator.")


# Run the program
if __name__ == "__main__":
    main()
