import os
import webbrowser
from data_methods import *
import datetime

# Alpha Vantage API key
api_key = '8FCYBQQE0XDXJWDC'

# 2023-06-06 to 2023-10-26?

# Main Loop
while True:
    print("Stock Data Visualizer")
    print("------------------------\n")

    # Input from the user
    stock_symbol = input("Enter the stock symbol: ")

    while True:
        print("Choose a chart type:")
        print("1. Bar Chart")
        print("2. Line Chart")
        chart_choice = input("Enter the number of chart type: ")

        if chart_choice in ['1', '2']:
            break
        else:
            print("\nInvalid choice entered. Please enter 1 or 2.\n")

    while True:
        print("Choose a time series:")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        time_series_choice = input("Enter the number of time series: ")

        if time_series_choice in ['1', '2', '3', '4']:
            break
        else:
            print("\nInvalid choice entered. Please enter 1 to 4.\n")

    start_date = input("Enter begin date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Validate the date range
    try:
        check_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        check_end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        if check_end_date < check_start_date:
            print("\nEnd date cannot be before the begin date.\n")
            continue
        else:
            # Define the time series function based on user choice
            time_series_functions = {
                '1': 'TIME_SERIES_INTRADAY',
                '2': 'TIME_SERIES_DAILY',
                '3': 'TIME_SERIES_WEEKLY',
                '4': 'TIME_SERIES_MONTHLY'
            }
    
        # Default to daily
        time_series_function = time_series_functions.get(time_series_choice, 'TIME_SERIES_DAILY')
        
        # Make the API request and create web browser with graph
        data = retrieve_data(time_series_function, stock_symbol, api_key, start_date, end_date)
        chart = generate_chart(data, chart_choice, time_series_function)

        chart.render_to_file('chart.svg')
        chart_path = os.path.abspath('chart.svg')
        webbrowser.open('file://' + chart_path)
        
    except ValueError:
        print("\nInvalid date format. Please use YYYY-MM-DD format for the dates.\n")
    
    another = input("Would you like to view more stock data? Enter [y] if yes: ")
    if another.lower() != 'y':
        break
