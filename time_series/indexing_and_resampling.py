data = pd.read_csv('nyc.csv')

# Inspect data
print(data.info())

# Convert the date column to datetime64
data.date = pd.to_datetime(data.date)

# Set date column as index
data.set_index('date',inplace=True)

# Inspect data 
print(data.info())

# Plot data
data.plot(subplots=True)
plt.show()

##########################################################

# Create dataframe prices here
prices = pd.DataFrame()

# Select data for each year and concatenate with prices here 
for year in [ '2013' , '2014' , '2015']:
    price_per_year = yahoo.loc[year, ['price']].reset_index(drop=True)
    price_per_year.rename(columns={'price' : year}, inplace=True)
    prices = pd.concat([prices, price_per_year], axis=1)

# Plot prices
prices.plot()
plt.show()

########################################################


# Inspect data
print(co.info())

# Set the frequency to calendar daily
co = co.asfreq('D') 

# Plot the data
co.plot(subplots=True)
plt.show()



# Set frequency to monthly
co = co.asfreq('M') # makes the plot look clearer

# Plot the data
co.plot(subplots=True)
plt.show()
