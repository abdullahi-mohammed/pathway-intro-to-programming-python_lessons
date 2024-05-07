# Author: Abdullahi Mohammed
# Date:   22th, feb. 2024.
# Purpose: Wind chill calculator

# What is the temperature? 8
# Fahrenheit or Celsius (F/C)? F
# At temperature 8.0F, and wind speed 5 mph, the windchill is: -1.11F
# At temperature 8.0F, and wind speed 10 mph, the windchill is: -6.02F
# At temperature 8.0F, and wind speed 15 mph, the windchill is: -9.15F
# At temperature 8.0F, and wind speed 20 mph, the windchill is: -11.50F
# At temperature 8.0F, and wind speed 25 mph, the windchill is: -13.40F
# At temperature 8.0F, and wind speed 30 mph, the windchill is: -15.00F
# At temperature 8.0F, and wind speed 35 mph, the windchill is: -16.39F
# At temperature 8.0F, and wind speed 40 mph, the windchill is: -17.62F
# At temperature 8.0F, and wind speed 45 mph, the windchill is: -18.73F
# At temperature 8.0F, and wind speed 50 mph, the windchill is: -19.74F
# At temperature 8.0F, and wind speed 55 mph, the windchill is: -20.67F
# At temperature 8.0F, and wind speed 60 mph, the windchill is: -21.53F

# Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)

T = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")
V = 0
C = "C"



def get_temperature_in_F(T):
    if C == unit.upper():
        # multiply the Celsius temperature by (9/5) and then add 32.
        T = T * (9 / 5) + 32
        return T
    return T
T = get_temperature_in_F(T)
def get_wind_chill(T, V):
    return 35.75 + 0.6215 * T - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
    
    
for i in range(0, 12):
    if V < 60:
        V += 5
        wind_chill = get_wind_chill(T, V)
        print(f"At temperature {T}F, and wind speed {V} mph, the windchill is: {wind_chill:.2f}F")