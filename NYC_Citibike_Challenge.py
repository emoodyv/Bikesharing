import pandas as pd

# 1. Create a DataFrame for the 201908-citibike-tripdata data.
df = pd.read_csv('201908-citibike-tripdata.csv')

# 2. Check the datatypes of your columns.
print(df.dtypes)

# 3. Convert the 'tripduration' column to datetime datatype.
df['tripduration'] = pd.to_datetime(df['tripduration'], unit='m')

# 4. Check the datatypes of your columns.
print(df.dtypes)
print(df)

# 5. Export the Dataframe as a new CSV file without the index.
df.to_csv('NYC_Citibike_Challenge.csv', index=False)