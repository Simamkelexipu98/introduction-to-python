Title: Simulation of Energy Consumption and Solar Production
 Video Demo:  https://youtu.be/LkAegt8a5fY
Subtitle: A Python Application for Household Energy Balance Calculation
Description:
NAME : SIMAMKELE XIPU
GitHub: SimamkeleXipu98
Edx: Siim23
Place: Pretoria
Location: South Africa
Date: October 7, 2024

 Project Overview
simulates a household's use of energy and production of renewable energy.
Calculates whether the home creates more energy than it consumes.
produces an energy balance that indicates whether external energy is needed.


 Program Structure
   main(): Central function that controls the simulation.
   get_energy_consumption(): Collects household energy consumption.
   get_solar_production(): Simulates solar panel energy generation.
   calculate_energy_balance(): Computes the energy balance.



 Main Function
   Executes core steps:
   Get energy consumption.

   Get solar energy production.
   Calculate energy balance.
   Displays the result:
   Positive balance: Household produced more energy.
   Negative balance: Household consumed more than it produced.



   Getting Energy Consumption
   Function: get_energy_consumption()
   Prompts user to input household energy usage in kWh.
   Handles invalid input with recursion using try except.
   Returns the valid energy consumption value.




 Solar Energy Production Simulation
  Function: get_solar_production()
  Inputs from the user:
  Hours of sunlight.
  Solar panel efficiency (kWh/hour).
  Calculates total production using the formula:
  Production = Hours of sunlight × Panel efficiency.
  Handles invalid inputs and reprompts if necessary.




  Calculating Energy Balance
  Function: calculate_energy_balance(consumption, production)
  Formula:
   Energy Balance = Solar Production  Energy Consumption
   Positive result: Household generated excess energy.
   Negative result: Household consumed more energy than it produced.



  Example Workflow
   User inputs:
     Energy consumption: 150 kWh.
     Hours of sunlight: 5 hours.
     Solar panel efficiency: 10 kWh/hour.
   Calculation:
     Solar production = 5 × 10 = 50 kWh.
     Energy balance = 50  150 = 100 kWh.
   Output:
    Your household consumed 100 kWh more than it produced.

  Error Handling
   Uses tryexcept blocks to handle invalid inputs.
   Prompts the user again if:
   Energy consumption is not a number.
   Hours of sunlight or panel efficiency are invalid.
   Recursively asks for valid input.

Key Concepts Used
   User Input: Energy consumption and solar production parameters.
   Error Handling: Validates inputs using try except and recursion.
   Basic Arithmetic: Calculates solar energy production and energy balance.
   Program Flow: Linear steps leading to energy balance calculation.

 Future Improvements
   Add more renewable energy sources.
   Implement energy storage (e.g., battery systems).
   Simulate power grid connection or utility bills.
   Introduce weather based solar prediction.

 Conclusion
 The project simulates basic energy consumption and production for a household.
 Provides useful insights into whether the household generates enough energy or needs external        power sources.
 Easy to extend with more features in the future.
