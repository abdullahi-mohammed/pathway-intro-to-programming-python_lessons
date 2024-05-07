# Author: Abdullahi Mohammed
# Date:   18th, feb. 2024.
# Purpose: Data Analysis
# stretch challenge: i added the country abbreviations from the data

# Enter the year of interest: 1959

# The overall max life expectancy is: 86.751 from Monaco in 2019
# The overall min life expectancy is: 17.76 from Iceland in 1882

## For the year 1959:
# The average life expectancy across all countries was 54.95
# The max life expectancy was in Norway with 73.49
# The min life expectancy was in Mali with 28.077

highest_life_expectancy = 0
lowest_life_expectancy = float("inf")

high_life_expectancy_country = ""
high_life_expectancy_country_abbr = ""
high_life_expectancy_year = 0

low_life_expectancy_country = ""
low_life_expectancy_country_abbr = ""
low_life_expectancy_year = 0

total_life_expectancy = 0
count = 0
average_life_expectancy = 0
interest_highest_life_expectancy = 0
interest_high_life_expectancy_country = ""
interest_lowest_life_expectancy = float("inf")
interest_low_life_expectancy_country = ""

year_of_interest = int(input("Enter the year of interest: ").strip())
        
with open("life-expectancy.csv") as life_expectancy:
    next(life_expectancy)
    for i, line in enumerate(life_expectancy):
        line = line.strip()
        part = line.strip().split(",")
        
        life_expectancy_country = part[0]
        life_expectancy_year = int(part[2])
        life_expectancy = float(part[3])
        
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            high_life_expectancy_country = part[0]
            high_life_expectancy_country_abbr = part[1]
            high_life_expectancy_year = part[2]
        
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            low_life_expectancy_country = part[0]
            low_life_expectancy_country_abbr = part[1]
            low_life_expectancy_year = part[2]
        
        if life_expectancy_year == year_of_interest:
            total_life_expectancy += life_expectancy
            count += 1
            
            if life_expectancy > interest_highest_life_expectancy:
                interest_highest_life_expectancy = life_expectancy
                interest_high_life_expectancy_country = part[0]
        
            if life_expectancy < interest_lowest_life_expectancy:
                interest_lowest_life_expectancy = life_expectancy
                interest_low_life_expectancy_country = part[0]
    
    if count > 0:
        average_life_expectancy = total_life_expectancy / count
            
print(f"The overall max life expectancy is: {highest_life_expectancy} from {high_life_expectancy_country}, {high_life_expectancy_country_abbr} in {high_life_expectancy_year} ")    
print(f"The overall min life expectancy is: {lowest_life_expectancy} from {low_life_expectancy_country}, {low_life_expectancy_country_abbr} in {low_life_expectancy_year}\n")
    
print(f"For the year {year_of_interest}: ")
print(f"The average life expectancy across all countries was {average_life_expectancy}")
print(f"The max life expectancy was in {interest_high_life_expectancy_country} with {interest_highest_life_expectancy}")
print(f"The min life expectancy was in {interest_low_life_expectancy_country} with {interest_lowest_life_expectancy}")