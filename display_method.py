
#from flask import Flask, render_template, request, Response
#from data_methods import retrieve_data
from display_method import extract_chart_data, create_line_chart
import pygal

#main = Flask(__name__)
#api_key = 'M5U4GAA5AW5TD1I1'

#this method extract data from api into time_series (d,w,m), num_points (range dates)
def extract_chart_data(time_series: dict, num_points: int = 10) -> tuple:
    dates = list(time_series.keys())[:num_points]
    dates.reverse()
    open_prices = [float(time_series[date]['1. open']) for date in dates]
    high_prices = [float(time_series[date]['2. high']) for date in dates]
    low_prices = [float(time_series[date]['3. low']) for date in dates]
    close_prices = [float(time_series[date]['4. close']) for date in dates]

    return dates, open_prices, high_prices, low_prices, close_prices

#This method create a line chart
def create_line_chart(symbol, timeframe, dates, open_prices, high_prices, low_prices, close_prices):
    line_chart = pygal.Line()
    line_chart.title = f"Stock Data for {symbol} - {timeframe}"
    line_chart.x_labels = dates
    line_chart.add('Open', open_prices)
    line_chart.add('High', high_prices)
    line_chart.add('Low', low_prices)
    line_chart.add('Close', close_prices)
    return line_chart

""" @main.route('/')
def index():
    return render_template('index.html')

@main.route('/stock_data', methods=['POST'])
def stock_data():
    symbol = request.form['symbol']

    # Define timeframes
    timeframes = {
        'Daily': 'TIME_SERIES_DAILY',
        'Weekly': 'TIME_SERIES_WEEKLY',
        'Monthly': 'TIME_SERIES_MONTHLY'
    }

    for timeframe, function in timeframes.items():
        stock_data = retrieve_data(function, symbol, api_key)

        if stock_data and f'Time Series ({timeframe})' in stock_data:
            dates, open_prices, high_prices, low_prices, close_prices = extract_chart_data(stock_data[f'Time Series ({timeframe})'])

            # Create Pygal line chart
            line_chart = create_line_chart(symbol, timeframe, dates, open_prices, high_prices, low_prices, close_prices)

        # Save the chart to a file (optional)
        line_chart.render_in_browser()
        return render_template('stock_data.html', chart_url='static/stock_chart.svg')
    else:
        return f"Error retrieving {timeframe} stock data"

if __name__ == '__main__':
    main.run(debug=True) """

