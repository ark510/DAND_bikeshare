## TODO: import all necessary packages and functions
import csv
import pprint
import random
import datetime
import time
from collections import Counter
#import DateTime

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (data object) The highest level data for a city's bikeshare records in 2017.
    '''
    city_file = None
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                'Would you like to see data for Chicago, New York, or Washington?\n').replace(' ','_')
        if city.lower() not in ('chicago', 'new_york', 'washington'):
            print("please choose a valid city name")
        else:
            break

    if city.lower() == "chicago":
        with open(chicago) as city_file:
            chi = [{k: v for k, v in row.items()}
                        for row in csv.DictReader(city_file, skipinitialspace = True)]
        city_data = chi
        print(chicago)

    elif city.lower() == "new_york":
        with open(new_york_city) as city_file:
            nyc = [{k: v for k, v in row.items()}
                        for row in csv.DictReader(city_file, skipinitialspace = True)]
        city_data = nyc
        print(new_york_city)

    elif city.lower() == "washington":
        with open(washington) as city_file:
            dc = [{k: v for k, v in row.items()}
                        for row in csv.DictReader(city_file, skipinitialspace = True)]
        city_data = dc
        print(washington)

    return city_data
    #print(city_data[:5])

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) the selected time_period as input to subsequent functions based on the user's input to filter by time period (month,day,none)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')

    if time_period.lower() == 'month':
        time_period = 'month'
        #return get_month()
    elif time_period.lower() == 'day':
        time_period = 'day'
        #return get_day()
    else:
        time_period == 'none'
        #print("No time filter selected")
    return time_period

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        Filter returns the specified month's bikeshare data
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()

    month_int = None
    month_start = []
    if month == "january":
        month_int = '01'
    elif month.lower() == "february":
        month_int = '02'
    elif month.lower() == "march":
        month_int = '03'
    elif month.lower() == "april":
        month_int = '04'
    elif month.lower() == "may":
        month_int = '05'
    elif month.lower() == "june":
        month_int = '06'
    else:
        print("sorry, data for that month is out of scope for this project")
    #print(month_int)
    for rows in city_data:
        start_date = rows['Start Time'].split("-")
        if start_date[1] == month_int:
            month_start.append(rows)
    #print(month)
    return month_start

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        xxmonth from get_month() << this argument is only necessary if the user would like to filter by month
    Returns:
        Filter returns the specified day of the week's bikeshare data across all months unless month is specified
    '''
    day = int(input('\nWhich day? Please type your response as an integer.\n'))

    #month = get_month()
    day_start = []
    for rows in city_data:
        start_dates = rows['Start Time'].replace('-',' ').split(' ')
        #print(start_dates[:10])
        if int(start_dates[2]) == day:
            day_start.append(rows)
    #print(day_start[:5])
    return day_start

def popular_month(city_file = 'chicago', time_period = 'none'):
    '''
    Question: What is the most popular month for start time?
    >>Define a function that returns the filtered result for the month with the most trips by count of start time within a city's data file

    Args:
        city_file, time_period = 'none' or 'month'
    Returns:
        (str) Most popular month (out of 6 calendar options) for trip start time defined by count of instances
    '''

    month_start = [] # create a list var to store only the 'Star Time' info
    months = ['01','02','03','04','05','06']
    # 'months' list is defined by the 6 month-corresponding digit combos that are listed in the project template
    for rows in city_data:
        start_dates = rows['Start Time'].split("-")
        # convert 'Start Time':values into separate list elements ie. [2017, 03, 06 12:58:30]
        # this produces a list of nested lists, one element for each 'Start Time'
        if start_dates[1] in months:
            month_start.append(start_dates)
    month_start_new = [[date[1] for date in month_start] for i in range(3)]
    # nested list comprehension of 2-digit month strings 'index[1]' from the 'month_start' list of lists
    most_popular = Counter(month_start_new[0]).most_common(1)
    # Counter returns an ordinal set of dicts with 'month_int' : 'count' where 'count' is number of trips
    most_popular = most_popular[0][0]
    # isolate the first 2-digit month string in the top Counter tuple
    #print(most_popular)
    if most_popular == '06':
        return 'The most popular month for bikeshare in this city is June.'
    elif most_popular == '05':
        return 'The most popular month for bikeshare in this city is May.'
    elif most_popular == '04':
        return 'The most popular month for bikeshare in this city is April.'
    # converts the 2-digit month string into month name

def popular_day(city_file = 'chicago', time_period = 'none'):
    '''
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    >> Define a function that returns the day of the week - across all months - with the most trips by count of start time within a city's data file

    Args:
        city_data, time_period = None
    Returns:
        (str) Most popular day of the week for trip start time defined by count of instances
    '''

    #from datetime import date
    day_start = []
    weekdays = []
    # create a list var to store only the 'Star Time' info
    for rows in city_data:
        start_dates = rows['Start Time'].replace('-','').split(' ')
        day_start.append(start_dates[0])
        # append giant list of dates to the 'day_start' var in string format so able to convert to weekday()
    for dates in day_start:
        days = datetime.datetime.strptime(dates, '%Y%m%d').weekday()
        weekdays.append(days)

    most_popular = Counter(weekdays).most_common(1)
    # returns a single tuple in a list with the most common weekday and trip count as integers
    most_popular = most_popular[0][0]
    # isolate the weekday integer and convert to weekday name as string
    if most_popular == 1:
        return 'The most popular day for bikeshare is Tuesday in this city'
    elif most_popular == 2:
        return 'The most popular day for bikeshare is Wednesday in this city'
    elif most_popular == 3:
        return 'The most popular day for bikeshare is Thursday in this city'
    elif most_popular == 4:
        return 'The most popular day for bikeshare is Friday in this city'
    else:
        return 'The most popular day for bikeshare is Monday in this city'


def popular_hour(city_file = 'chicago', time_period = 'none'):
    '''
    Question: What is the most popular hour of day for start time?
    >> Define a function that returns the hour of the day from the 24-hour clock with the most trips

    Args:
        city_file, time_period = 'none' or 'month' or 'day'
    Returns:
        (str) Most popular hour am/pm for trip start time defined by 24-hour clock hour digit
    '''

    #month = get_month()
    #day = get_day(month)
    hours = []
    for rows in city_data:
        start_dates = rows['Start Time'].replace('-','').split(' ')
        start_hours = start_dates[1].split(':')
        # isolate 2-digit hour string
        hours.append(start_hours[0])
        # append giant list of hour strings to the 'hours' in order to count totals
    most_popular_hour = Counter(hours).most_common(1)
    # returns a single tuple in a list with the most common hour as string and trip count as integer
    hour = most_popular_hour[0][0]
    # isolate the hour string and convert to am/pm hour as string result
    if int(hour) > 12:
        return str(int(hour) - 12) + 'PM local time is the most popular hour of the day for bikeshare in this city.'
    else:
        return hour[1] + 'AM local time is the most popular hour of the day for bikeshare in this city.'
    # return the result as a string with am/pm designation


def trip_duration(city_file = 'chicago', time_period = 'none'):
    '''
    Question: What is the total trip duration and average trip duration?

    Args:
        city_file, time_period = 'none' or 'month' or 'day'
    Returns:
        (str) Total trip duration and average trip duration within the selected time period for the selected city
    '''

    trip_times = []
    for rows in city_data:
        trip_time = rows['Trip Duration']
        trip_times.append(int(float(trip_time)))
        # creates a sublist with all of the trip durations in seconds for the city as integers
    city_total = (sum(trip_times))/60
    # totals the trip durations for the entire city and returns in number of hours
    city_average = ((sum(trip_times))/len(trip_times))/60
    #print(city_total, int(city_average))
    return 'The total duration of all trips is {} minutes and the average trip duration is {} minutes'.format(int(city_total), int(city_average))
    

def popular_stations(city_file = 'chicago', time_period = 'none'):
    '''
    Question: What is the most popular start station and most popular end station?

    Args:
        city_file, time_period = 'none' or 'month' or 'day'
    Returns:
        (str) The most popular Start and End stations as defined by number of trips within the selected time period for the selected city
    '''

    start_stations = []
    end_stations = []
    for rows in city_data:
        start_station = rows['Start Station']
        start_stations.append(start_station)
        end_station = rows['End Station']
        end_stations.append(end_station)

    most_popular_start = Counter(start_stations).most_common(1)
    most_popular_end = Counter(end_stations).most_common(1)
    #print(most_popular_start, most_popular_end)
    return 'The most popular station where trips were started is {}, while the most popular station where trips were ended is {}'.format(most_popular_start[0][0], most_popular_end[0][0])


def popular_trip(city_file = 'chicago', time_period = 'none'):
    '''xxTODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    >> Return the most popular trip as defined by the Start/End station pairs being counted from the city file

    Args:
        city_file, time_period = 'none or 'month' or 'day'
    Returns:
        (str) The most trip as defined by a Start and End station pair by number of trips within the selected time period for the selected city
    '''
    station_pairs_list = []
    station_pairs_tups = []
    for rows in city_data:
        stations = ['Start Station', 'End Station']
        station_pairs = dict((k, rows[k]) for k in stations if k in rows)
        station_pairs_list.append(station_pairs)
        # append a collection of dicts to the 'station_pairs_list' that contain Start: and End Station: as keys
    for dicts in station_pairs_list:
        # loop through all of the Start: and End Station: dicts to collect the station names and match as tuples
        station_pairs_tups.append(tuple(dicts.values()))
        # append the Start: and End Station: tuples to a list for Counter to run
        #print(station_pairs_tups[:10])
    most_popular_trip = Counter(station_pairs_tups).most_common(1)
    # use the Counter function to display the most_popular_trip and number of occurances defined by station pairs

    most_popular_trip = str(most_popular_trip[0][0])
    #print(most_popular_trip)
    return 'The most popular trip in this city as defined by the Start & End station pairing is {}.'.format(most_popular_trip)


def users(city_file = 'chicago', time_period = 'none'):
    '''
    Question: What are the counts of each user type?
    This function will return the counts of each user type for trips in the selected time period in the selected city

    Args:
        city_file, time_period = 'none or 'month' or 'day'
    Returns:
        (str) the number of users in each category as currently defined in the city data: Subscriber or Customer
    '''

    user_types = []
    for rows in city_data:
        users = rows['User Type']
        user_types.append(users)
    #print(user_counts[:5])
    user_counts = Counter(user_types).most_common()

    return "The most common user types with the associated counts by number of trips are: {}.".format(user_counts)

def gender(city_file = 'new_york', time_period = 'none'):
    '''
    Question: What are the counts of gender?
    This function will return the counts of each gender type found in the data: Female, Male or undefined

    Args:
        city_file = 'new_york' or 'chicago', time_period = 'none or 'month' or 'day'
    Returns:
        (str) the number of users of each gender as currently defined (Female, Male or undefined) in the city data and time period.
    '''

    user_gender = []
    for rows in city_data:
        gender_type = rows['Gender']
        user_gender.append(gender_type)
    #print(user_gender[:5])
    gender_counts = Counter(user_gender).most_common()

    return "The counts by gender of each user by number of trips are: {}.".format(gender_counts)

def birth_years(city_file = 'new_york', time_period = 'none'):
    '''
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?

    Args:
        city_file = 'new_york' or 'chicago', time_period = 'none' or 'month' or 'day'
    Returns:
        (str) the earliest, latest and most common birth years in the city data and time period previously selected.
    '''

    birth_years = []
    for rows in city_data:
        years = rows['Birth Year']#.split('.')
        # removes blank entries from the birth_years list
        if years != '':
            birth_years.append(int(float(years)))
    #print(birth_years[:5])
    earliest_year = min(birth_years)
    #if earliest_year < 1900:
        #earliest_year = earliest_year[1].replace('8','9')
    latest_year = max(birth_years)
    count_year = Counter(birth_years).most_common(1)
    popular_year = count_year[0][0]
    #print(earliest_year, latest_year, popular_year)
    return "The earliest birth year in this user group is {} while the latest birth year is {}.  The most common birth year is {}.".format(earliest_year, latest_year, popular_year)


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        Returns 5 rows of randomized data as nested dictionaries within the filtered data set
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n').lower()

    pp = pprint.PrettyPrinter()
    while True:
        if display == 'yes':
            pp.pprint(random.sample(city_data, 5))
            display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n').lower()
        else:
            break

city_data = get_city()
time_period = get_time_period()
if time_period == 'month':
    city_data = get_month()
elif time_period == 'day':
    city_data = get_day()

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)

    # Filter by time period (month, day, none)

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        result_month = popular_month()
        print(result_month)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':

        start_time = time.time()

        result_day = popular_day()
        print(result_day)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    result_hour = popular_hour()
    print(result_hour)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    result_duration = trip_duration()
    print(result_duration)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    result_stations = popular_stations()
    print(result_stations)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    result_trip = popular_trip()
    print(result_trip)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    result_users = users()
    print(result_users)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    if city_data == 'washington':
        display_data()
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() == 'yes':
            statistics()
        else:
            exit()
    else:
        result_gender = gender()
        print(result_gender)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    result_birth = birth_years()
    print(result_birth)

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        get_city()
        get_time_period()

        statistics()

if __name__ == "__main__":
	statistics()
