def get_weather_data(year):
    url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&Day=14&timeframe=1&submit=Download+Data"
    #               <http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year=%7Byear%7D&Month=%7Bmonth%7D&Day=14&timeframe=1&submit=Download+Data>"
    data_by_month = []
    for month in range(1, 12):
        url = url_template.format(year=year, month=month)
        weather_data = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True).dropna(axis=1)
        weather_data.columns = map(lambda x: x.replace('\xb0', ''), weather_data.columns)
        weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
        data_by_month.append(weather_data.dropna())
    url = url_template.format(year=year-1, month='12')
    weather_data = pd.read_csv(url, skiprows=16, index_col='Date/Time', parse_dates=True).dropna(axis=1)
    weather_data.columns = map(lambda x: x.replace('\xb0', ''), weather_data.columns)
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    data_by_month.append(weather_data.dropna())
    return pd.concat(data_by_month)