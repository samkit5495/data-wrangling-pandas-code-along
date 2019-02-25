# --------------
import pandas as pd 

# Read the data using pandas module.
ipl_dataset = pd.read_csv(path)

# Find the list of unique cities where matches were played
print('the list of unique cities where matches were played')
print(ipl_dataset['city'].unique())

# Find the columns which contains null values if any ?
print('the columns which contains null values if any')
ipl_dataset_null_values = ipl_dataset.isnull().any()
print(ipl_dataset_null_values)
print(list(ipl_dataset.columns[ipl_dataset_null_values]))

# List down top 5 most played venues
print('List down top 5 most played venues')
print(ipl_dataset.groupby('venue')['match_code'].nunique().nlargest(5))

# Make a runs count frequency table
print('a runs count frequency table')
print(ipl_dataset['runs'].value_counts())

# How many seasons were played and in which year they were played 
print('How many seasons were played and in which year they were played ')
ipl_dataset['year'] = ipl_dataset['date'].str[:4]
print(ipl_dataset['year'].nunique())

# No. of matches played per season
print('No. of matches played per season')
print(ipl_dataset.groupby(['year'])['match_code'].nunique())

# Total runs across the seasons
print(ipl_dataset.groupby(['year'])['runs'].sum())

# Teams who have scored more than 200+ runs. Show the top 10 results
print('Teams who have scored more than 200+ runs. Show the top 10 results')
ipl_dataset_team_wise_score = ipl_dataset.groupby(['batting_team','match_code','inning'],as_index=False)['runs'].sum()
ipl_dataset_team_wise_score_above_200 = ipl_dataset_team_wise_score[ipl_dataset_team_wise_score>200]
print(ipl_dataset_team_wise_score_above_200.groupby('batting_team')['runs'].sum().nlargest(10))

# What are the chances of chasing 200+ target
print('What are the chances of chasing 200+ target')
ipl_dataset_team_wise_score = ipl_dataset.groupby(['batting_team','match_code','inning'],as_index=False)['runs'].sum()
high_inning_1_total = ipl_dataset_team_wise_score[ipl_dataset_team_wise_score['inning'] == 1]
high_inning_2_total = ipl_dataset_team_wise_score[ipl_dataset_team_wise_score['inning'] == 2]
joined_data = pd.merge(high_inning_1_total,high_inning_2_total,on='match_code')
chased_matches_won = joined_data['runs_x']<joined_data['runs_y']
winning_percentage = chased_matches_won.sum()/len(chased_matches_won)
print(winning_percentage)

# Which team has the highest win count in their respective seasons ?
print('Which team has the highest win count in their respective seasons ?')
team_match_won_count = ipl_dataset.groupby(['year','winner'])['match_code'].nunique()
team_match_won_count = team_match_won_count.reset_index()
team_match_won_count.loc[team_match_won_count.groupby(['year'])['match_code'].idxmax()]



