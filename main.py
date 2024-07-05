import pandas as pd
# Create individual dataframes for each year
df2016=pd.read_csv('/Downloads/Kaggle Dataset/Polls/2016_poll_results.csv')
df2017=pd.read_csv('/Downloads/Kaggle Dataset/Polls/2017_poll_results.csv')
df2018=pd.read_csv('/Downloads/Kaggle Dataset/Polls/2018_poll_results.csv')
df2019=pd.read_csv('/Downloads/Kaggle Dataset/Polls/2019_poll_results.csv')
#df2020=pd.read_csv('/Downloads/Kaggle Dataset/Polls/2020_poll_results.csv') this data was not available
df2021=pd.read_csv('/Downloads/Kaggle Dataset/Polls/2021_poll_results.csv')
df2022=pd.read_csv('/Downloads/Kaggle Dataset/Polls/2022_poll_results.csv')
df2023=pd.read_csv('/Downloads/Kaggle Dataset/Polls/2023_poll_results.csv')



# Select only 'Contestant', 'my_eurovision_scoreboard_points', and 'Year' columns
df_2016_selected = df2016[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2017_selected = df2017[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2018_selected = df2018[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2019_selected = df2019[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2021_selected = df2021[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2022_selected = df2022[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2023_selected = df2023[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]




# Select and pivot data for each year

# Year 2016
df_2016_selected = df2016[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2016_pivot = df_2016_selected.pivot(index='Contestant', columns='Year', values='my_eurovision_scoreboard_points')
df_2016_pivot.reset_index(inplace=True)
df_2016_pivot.columns.name = None

# Year 2017
df_2017_selected = df2017[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2017_pivot = df_2017_selected.pivot(index='Contestant', columns='Year', values='my_eurovision_scoreboard_points')
df_2017_pivot.reset_index(inplace=True)
df_2017_pivot.columns.name = None

# Year 2018
df_2018_selected = df2018[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2018_pivot = df_2018_selected.pivot(index='Contestant', columns='Year', values='my_eurovision_scoreboard_points')
df_2018_pivot.reset_index(inplace=True)
df_2018_pivot.columns.name = None

# Year 2019
df_2019_selected = df2019[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2019_pivot = df_2019_selected.pivot(index='Contestant', columns='Year', values='my_eurovision_scoreboard_points')
df_2019_pivot.reset_index(inplace=True)
df_2019_pivot.columns.name = None

# Year 2021
df_2021_selected = df2021[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2021_pivot = df_2021_selected.pivot(index='Contestant', columns='Year', values='my_eurovision_scoreboard_points')
df_2021_pivot.reset_index(inplace=True)
df_2021_pivot.columns.name = None

# Year 2022
df_2022_selected = df2022[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2022_pivot = df_2022_selected.pivot(index='Contestant', columns='Year', values='my_eurovision_scoreboard_points')
df_2022_pivot.reset_index(inplace=True)
df_2022_pivot.columns.name = None

# Year 2023
df_2023_selected = df2023[['Contestant', 'my_eurovision_scoreboard_points', 'Year']]
df_2023_pivot = df_2023_selected.pivot(index='Contestant', columns='Year', values='my_eurovision_scoreboard_points')
df_2023_pivot.reset_index(inplace=True)
df_2023_pivot.columns.name = None




# Adding the flags. 2018 had the most number of contestants so this year was chosen
data_2018 = {
    'Contestant': ['Albania', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium', 'Bulgaria', 
                   'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 
                   'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Latvia', 'Lithuania', 
                   'Malta', 'Moldova', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 
                   'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovenia', 'Spain', 'Sweden', 
                   'Switzerland', 'Ukraine', 'United Kingdom'],
    '2018': [38986, 13739, 54112, 65729, 25039, 38938, 52658, 120453, 12846, 196767, 101608, 53234, 88486, 
             75559, 111732, 4218, 69443, 56368, 39081, 4079, 35189, 143309, 77730, 16222, 44007, 18729, 22829, 
             4630, 19810, 29328, 28452, 14917, 39008, 6812, 7399, 4472, 14786, 26065, 35029, 62212, 40363, 
             67514, 18900]
}

df_2018_pivot = pd.DataFrame(data_2018)

# Function to generate URL for Flourish Studio country flags
def generate_flag_url(country):
    base_url = "https://public.flourish.studio/country-flags/svg/"
    country_to_code = {
        'Albania': 'al', 'Armenia': 'am', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Belarus': 'by', 
        'Belgium': 'be', 'Bulgaria': 'bg', 'Croatia': 'hr', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 
        'Estonia': 'ee', 'Finland': 'fi', 'France': 'fr', 'Georgia': 'ge', 'Germany': 'de', 'Greece': 'gr', 
        'Hungary': 'hu', 'Iceland': 'is', 'Ireland': 'ie', 'Israel': 'il', 'Italy': 'it', 'Latvia': 'lv', 
        'Lithuania': 'lt', 'Malta': 'mt', 'Moldova': 'md', 'Montenegro': 'me', 'Netherlands': 'nl', 
        'North Macedonia': 'mk', 'Norway': 'no', 'Poland': 'pl', 'Portugal': 'pt', 'Romania': 'ro', 'Russia': 'ru', 
        'San Marino': 'sm', 'Serbia': 'rs', 'Slovenia': 'si', 'Spain': 'es', 'Sweden': 'se', 'Switzerland': 'ch', 
        'Ukraine': 'ua', 'United Kingdom': 'gb'
    }
    return base_url + country_to_code.get(country, 'unknown') + ".svg"

# Add the Country Flag URL column to df_2018_pivot
df_2018_pivot['Country Flag URL'] = df_2018_pivot['Contestant'].map(generate_flag_url)



# Create a list of DataFrames to concatenate
dfs_to_concat = [df_2016_pivot, df_2017_pivot, df_2018_pivot, df_2019_pivot, df_2021_pivot, df_2022_pivot, df_2023_pivot]

# Concatenate the DataFrames along columns (axis=1)
df_concatenated = pd.concat(dfs_to_concat, axis=1)


# Output file to be visualised in Flourish
df_concatenated.to_csv('flourish_tuco.csv')
