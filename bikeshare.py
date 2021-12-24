import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','new york city','washington']
    print('Which city would you like to see data for? The available options are Chicago,New York City,Washington')
    city = ' '
    while city not in cities:
        city = input('Enter city name: ').lower()
        if city in cities:
            break
        else:
            print("The city you entered doesn't have available data. Please enter an available option: ")
                
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','all']
    print('Which month would you like to see data for? Type in a month between January - June. If you will like to see data for all the months, type in "all".')
    
    month = ' '
    while month not in months:
        month = input('Enter Preferred month: ').lower()
        if month in months:
            break
        else:
            print("Please enter an option as in the instruction above: ")
    
         # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_the_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    print('Which day would you like to see data for? Type in a day between Monday - Sunday. If you will like to see data for the week, type in "all".')
    day = ' '
    while day not in day_of_the_week:
        day = input('Enter Preferred Day: ').lower()
        if day in day_of_the_week:
            break
        else:
            print("Please enter an option as in the instruction above: ")
    print('Here is your selection: The city of ' + city.title() + ' for the month of ' + month.title() + ' and the day of the week ' + day.title() )
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June','all':'all'}
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is {}'.format(months[popular_month]))
    
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week is {}'.format(popular_day_of_week))
    
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is {}'.format(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(popular_start_station))
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(popular_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    df['start-end station'] =  'FROM ' + df['Start Station'] + ' TO ' + df['End Station']
    popular_station_combination = df['start-end station'].mode()[0]
    print('The most frequent combination of station is {}'.format(popular_station_combination))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total time of travel took {} secs'.format(total_travel_time))
    
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The average time of travel is {} secs'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Calculating number of User Type')
    user_types_count = df['User Type'].value_counts()
    print(user_types_count)
    
    # TO DO: Display counts of gender
    print('\nCalculating number of Users by Gender')
    user_gender_count = df['Gender'].value_counts()
    print(user_gender_count)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nCalculating Age statistics')
    earliest_year_of_birth = df['Birth Year'].min()
    print('The earliest year of birth of users is {}'.format(int(earliest_year_of_birth)))
    
    most_recent_year_of_birth = df['Birth Year'].max()
    print('The most recent year of birth of users is {}'.format(int(most_recent_year_of_birth)))
    
    most_common_year_of_birth = df['Birth Year'].mode()[0]
    print('The most popular year of birth of users is {}'.format(int(most_common_year_of_birth)))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """This function when called displays a number of rows of the particular city."""
    display = input('\nWould you like to see the first 5 rows of the dataset? Enter yes or no.\n')
    start_loc = 0
    end_loc = 5
    while display.lower() != 'no':
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc += 5
        display = input("Do you wish to continue to the next 5 rows?: ").lower()
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()