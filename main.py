import requests
import json
from data_methods import *

# you will need to download requests and json and whatever charting method is chosen to run this file

# Main Page
import pygal
import datetime
from pygal.style import LightStyle

# Alpha Vantage API key
api_key = 'M5U4GAA5AW5TD1I1'

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

    begin_date = input("Enter begin date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Validate the date range
    try:
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

        if end_date < begin_date:
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
        
        # Make the API request
        url = f'https://www.alphavantage.co/query?function={time_series_function}&symbol={stock_symbol}&apikey={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            # Process the data and create a chart based on user choice
            dates = list(data[f'Time Series ({time_series_function})'].keys())
            closing_prices = [float(data[f'Time Series ({time_series_function})'][date]['4. close']) for date in dates]
            
            # Create a chart !!(Note: Probably don't need this on main, if so, please delete)!!
            if chart_choice == '1':
                chart = pygal.Bar(style=LightStyle, x_label_rotation=45, show_legend=False, title=f'{stock_symbol} Stock Data (Bar Chart)')
            elif chart_choice == '2':
                chart = pygal.Line(style=LightStyle, x_label_rotation=45, show_legend=False, title=f'{stock_symbol} Stock Data (Line Chart)')
            
            chart.x_labels = dates
            chart.add('Closing Price', closing_prices)
            chart.render_in_browser()

        else:
            print("Error: Failed to retrieve data from Alpha Vantage.")
    except ValueError:
        print("\nInvalid date format. Please use YYYY-MM-DD format for the dates.\n")
