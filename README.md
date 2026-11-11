# Resistor Combination Calculator

## What it does
This program asks how many resistors you have and the value of each one in ohms. It then calculates and displays the total resistance when the resistors are connected in series and when they are connected in parallel. As an extra feature, it can also calculate the current that would flow through each combination if you supply a voltage.

## How to run it
Install Python 3, then run:
```
python resistor_combination_calculator.py
```

## Sample output
```
==================================================
   RESISTOR COMBINATION CALCULATOR
==================================================
This program calculates total resistance
for resistors in SERIES and in PARALLEL.

How many resistors do you have? 3

Enter the resistance of each resistor in ohms (Ω):
  Resistor 1: 100
  Resistor 2: 220
  Resistor 3: 330

--------------------------------------------------
RESULTS
--------------------------------------------------
Number of resistors : 3
Values (Ω)          : [100.0, 220.0, 330.0]

Series total        : 650.0000 Ω
Parallel total      : 56.8966 Ω
--------------------------------------------------

EXTRA FEATURE: Current calculation
If you apply a voltage across the combination,
the program can also show the current (I = V / R).

Do you want to calculate current for a given voltage? (y/n): y
Enter the supply voltage in volts (V): 12

At 12.0 V:
  Current in SERIES combination   : 0.0185 A
  Current in PARALLEL combination : 0.2109 A

Note: Parallel always draws more current for the same voltage
because its total resistance is lower.

Thank you for using the Resistor Combination Calculator.
```

## My own twist
After showing the series and parallel totals, the program asks if you want to calculate current. If you say yes, it asks for a supply voltage and uses Ohm’s law (I = V / R) to show the current that would flow in the series combination and in the parallel combination. This helps students quickly see the practical difference between the two connections.

## What I learned
- How to use a list to store multiple values entered by the user.
- How to write functions that return calculated values and reuse them.
- The importance of checking user input so the program does not crash when someone types a letter instead of a number.

## Author
Timilehin Bamgbose, ND Mechatronics Engineering, YabaTech.
