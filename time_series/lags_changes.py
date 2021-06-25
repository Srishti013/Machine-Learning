# Import data here
google = pd.read_csv('google.csv',parse_dates=['Date'], index_col='Date')

# Set data frequency to business daily
google = google.asfreq('B')

# Create 'lagged' and 'shifted'
google['lagged'] = google['Close'].shift(-90)
google['shifted'] = google['Close'].shift(90)

# Plot the google price series
google.plot()
plt.show()


#####################################################


yahoo['change_30'] = yahoo.price.sub(yahoo.shifted_30)

# Get the 30-day price difference
yahoo['diff_30'] = yahoo.price.diff(periods=30)

# Inspect the last five rows of price
print(yahoo['price'].tail())

# Show the value_counts of the difference between change_30 and diff_30
print((yahoo.change_30.sub(yahoo.diff_30)).value_counts())


#####################################################

# Create daily_return
google['daily_return'] = google.Close.pct_change(1).mul(100)

# Create monthly_return
google['monthly_return'] = google.Close.pct_change(30).mul(100)

# Create annual_return
google['annual_return'] = google.Close.pct_change(360).mul(100)

# Plot the result
google.plot(subplots=True)
plt.show()


#####################################################
