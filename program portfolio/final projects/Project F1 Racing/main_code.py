import sys
from tabulate import tabulate as t

def for_driver():
    # Open the file containing driver information
    with open("f1_drivers.txt", "r") as file:
        driver_info = []

        for line in file:
            # Split the line into individual details and store them in a list
            driver_information = line.strip().split(',')
            driver_info.append(driver_information)

    # Display driver information in a table format
    print("_________________DRIVERS' INFORMATION___________________\n")
    for_top = ["Number", "Code", "Driver Name", "Team"]
    print(t(driver_info, headers=for_top, tablefmt="fancy_grid"))

# Function to retrieve the race location from the file
def get_location(file_path):
    with open(file_path, "r") as file:
        information = file.readlines()
      
    # The first line of the file contains the race location  
    race_location = information[0].strip() # Remove any extra spaces or newlines
    return race_location


# Function to extract and process lap times from the file
def get_lap_times(file_path):
    with open(file_path, "r") as file:
        information = file.readlines()
        
    lap_times = {}
    
    for line in information[1:]:  # Skip the first line (race location)
        code_of_driver = line[:3].strip()  # Extract driver code (first three characters of the line)
        try:
            # Extract and convert the lap time to a float
            for_time_lap = float(line[3:].strip())  
            
        except ValueError:
            # Skip lines with invalid lap time formats
            print(f"Skipping invalid line: {line.strip()}")
            continue

        if code_of_driver in lap_times:
            lap_times[code_of_driver].append(for_time_lap)
        else:
            lap_times[code_of_driver] = [for_time_lap]
            
    return lap_times

# Function to display the results in a tabular format
def display_results(lap_times):
    table = []
    for driver, times in lap_times.items(): # Process each driver and their lap times
        fastest_time = min(times)  # Find the fastest lap time for each driver
        table.append([driver, fastest_time])  # Append driver and their fastest lap time to the table

    print(t(table, headers=["Driver Code", "Fastest Lap Time"], tablefmt="fancy_grid"))



def main():
    for_driver()
    
    # Ensure a lap times file is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python main.py <lap_times_file>")
        return

    file_path = sys.argv[1]
    lap_times = get_lap_times(file_path)
    race_location = get_location(file_path)
    print(f"Race Location: {race_location}\n") 
    display_results(lap_times)

if __name__ == "__main__":
    main()
