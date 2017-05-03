import sys
import pandas as pd
from pandas import DataFrame, Series

def csv_reader (file_name, datetime_col_index) :
    return pd.read_csv(file_name, index_col=datetime_col_index, parse_dates=True)

def downsample_first(frame, interval):
    return frame.resample(interval).first().dropna()

def is_violent(frame):
    violent_crimes = ['BATTERY', 'ROBBERY', 'HOMICIDE', 'ASSAULT']
    return frame[frame['Primary Type'].map(lambda x: x in violent_crimes)]


def weekly_average(frame):
    return frame.resample('W-MON').mean().dropna()

def find_arrest_rate(frame):
    # frame = downsample_first(frame, '30Min')
    # frame = is_violent(frame)
    # frame = weekly_average(is_violent(downsample_first(frame, '30Min')))
    return weekly_average(is_violent(downsample_first(frame, '30Min')))['Arrest']


# This executable takes an argument as a system input argument which
# points to the dataset (a path including the name of the dataset) and
# an integer, datetime_col_index.

# When this executable runs, it runs the __main__ method defined at the end.
# Additional function definitions and import statements should be outside this function.
# All other code should be in the __main__ method.

# Throughout this assignment, we've provided sample data.  You can check your
# dataframes against this data by outputting your frame to a csv file using
# <myframe>.to_csv(<provide a file name>)

# ####### Part 1:  Creating the DataFrame

# Read in the data and index it using a TimeSeries.  Compare to a solution file.
#
# The dataset we are going to practice with is 'Crimes_medium.csv'. It has about
# 100,000 records of crimes with detailed information.
# This executable has a function called (exactly):
#   csv_reader(file_name, datetime_col_index)
# that takes the path to a CSV file, file_name and an integer, datetime_col_index.
# It reads the CSV file into a dataframe such that the column number given by
# datetime_col_index is used as the index and that the index is a TimeSeries type.
#
# To complete this part, figure out the arguments to *this executable*, such that
# the resulting dataset looks like the one in 'indexed.csv'
# i.e. if you write the output of csv_reader() to a file using the
# to_csv() method, it is identical.

# ####### Part 2.  Resampling your data.
#
# Add a function to your executable called:
#   downsample_first(frame, interval)
# that takes a DataFrame, frame and a string, interval.
#
# Your function should return a DataFrame that has been downsampled such that:
# - only the first observation for each interval remains.
# - observations that are N/A are dropped
#
# You can assume that interval is a legal interval string for the
# Series.resample() function.
#
# For an interval of 30 minutes, you can check your work against the test file:
#   'downsampled_30min.csv'

# ####### Part 3.  Filtering your data
#
# Add a function to your executable called:
#   is_violent(series)
# that takes a Series, series.
#
# Your function should return a Series that has been filtered to only include
# violent crimes items.
#
# For our purposes, we'll assume that violent crimes are crimes where the
# value of 'Primary Type' is one of:
# BATTERY, ROBBERY, HOMICIDE, ASSAULT, CRIM SEXUAL ASSAULT.
#
# Hint:  you may want to put the values above in an array in order to set up your filter.
#

# ####### Part 4.  Compute a rolling mean.
#
# Add a function to your executable called:
#   weekly_average(series)
# that takes a Series, series that is indexed by a TimeSeries.
#
# Your function should return a Series whose values are the weekly average
# (computed Monday-to-Monday) for that series.

# ####### Part 5.  Compute the arrest rate for violent crimes.
#
# Add a function to your executable called:
#   find_arrest_rate(frame)
# that takes a DataFrame, frame that is indexed by a TimeSeries.
#
# Your function should compute the arrest rate by week for violent crimes only.
# (i.e. the average of the 'Arrest' column for the week) and return the last 10 weekly arrest rates.
#
# You should be able to rely on the functions you've already written to do this.
#


if __name__ == '__main__':
    # crimes=csv_reader(sys.argv[1], int(sys.argv[2]))
    # crimes = downsample_first(crimes,'30Min')
    # crimes = weekly_average(crimes)
    # crimes =  is_violent(crimes)
    crimes = find_arrest_rate(csv_reader(sys.argv[1], int(sys.argv[2])))


    crimes.to_csv('test4.csv')
