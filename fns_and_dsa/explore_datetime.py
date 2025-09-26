from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()  # get current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculate the future date after adding days_to_add to current_date.
    """
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Ask user for days and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

