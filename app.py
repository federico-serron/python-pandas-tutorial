import pandas as pd

# Creating a data fram from reading a csv file
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

# Creating a serie, it means creating a simple array 1D
ages = pd.Series([23,45,7,34,6,63,36,78,54,34])

# Creating an array with a range of dates
dates = pd.date_range('05-01-2021', '05-12-2021')

# Applying a function (made by me) to a every single item into the serie
my_series = pd.Series([2, 4, 6, 8, 10])
def splitByTwo(s):
    return s / 2
applied = my_series.apply(splitByTwo)


# Printing results
print(applied)