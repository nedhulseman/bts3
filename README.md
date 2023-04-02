# ![The Logo](https://github.com/nedhulseman/bts2/blob/main/bts%20logo.png) Beat The Streak
This project is a part of the [Beat The Streak Competition](https://www.mlb.com/apps/beat-the-streak) hosted by [Major League Baseball](http://www.mlb.com). 

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is create sound and accurate predictions for batters getting at least one hit on any given day. In addition, we want to learn more about what factors influence a batter's probability of getting a hit.



### Methods Used
* Logistic Regression
* Random Forest
* LightGBM


### Technologies
* Python
* Selenium 
* Flask
* HTML
* CSS


## Project Description
We pulled our data using the package baseball_scraper which provides play level information on historical baseball games going back to 2013.

## Needs of this project

- frontend developer
- data exploration
- data processing/cleaning
- statistical modeling
- automation of pick submission

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is obtained from the get_data.py script    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. Downlaod the appropriate Google Chrome Driver [here](https://chromedriver.chromium.org/downloads)
5. Install required packages from [requirement.txt](https://github.com/nedhulseman/bts2/blob/main/requirements.txt)

## File Descriptions
1. Main.py completes the gathering and manipulation of data for both training and deployment for time period of interest.
2. Main_train.py trains the models models using given a start date and end date provided. 
3. App.py spins up application to see current and previous results and predicted probabilities.

## Data Dictionary
The data is obtained using the package [baseball-scraper] (https://pypi.org/project/baseball-scraper/). The data dictionary for the raw variables can be found [here](https://baseballsavant.mlb.com/csv-docs).


## Contributing Members

**Team Leads (Contacts) : [Jabari Myles](https://github.com/mylesj8259) [Ned Hulseman](https://github.com/nedhulseman)**

#Model Data Other Members:

|Field                 | Field Name         | Script | Implemented |
|------------------------|--------------------|-----------------|-------------|
| rp_BA                  | Recent Play Batting AVG   | createTableRPPlayer.get_rpplayer | Yes |
| rp_AB_div_PA           | Recent Play Batting AB/PA |  createTableRPPlayer.get_rpplayer | Yes |
| ytd_BA                 | YTD Batting AVG.          | .  | Yes |
| ytd_AB_div_PA          | YTD AB/PA                 | .  | Yes |
| rp_hits_var            | Recent Play Hit Variance  | .  | Yes |
| ytd_hits_var           | YTD Hit Variance          |.   | Yes |
| hit_ind                | Did player get hit? (target)  |.   | Yes |
| rp_BA_sp               | Recent Play Batting AVG for Starting Pitcher |.  |.  | Yes |
| rp_AB_div_PA_sp        | Recent Play YTD Batting AVG for SP  |  |.   | Yes |
| ytd_BA_sp              | YTD Batting AVG for SP  |.  | Yes |
| ytd_AB_div_PA_sp       | YTD AB/PA for SP  |.  | Yes |
| match_year_PAs         | Batter/SP YTD # of PAs  |.  | Yes |
| match_year_BA          | Batter/SP YTD Batting AVG    |.  | Yes |
| match_year_AB_div_PA   | Batter/SP YTD AB/PA    |.  | Yes |
| match_career_PAs       | Batter/SP Career PAs  |.  | Yes |
| match_career_BA        | Batter/SP Career BAs  |.  | Yes |
| match_career_AB_div_PA | Batter/SP Career AB/PA  |.  | Yes |
| game_date              | Game Date  |.  | Yes |
| game_pk                | Game ID  |.  | Yes |
| batter                 | Batter ID  |.  | Yes |
| starting_pitcher       | Starting Pitcher ID  |.  | Yes |
| ABs                    | Batter Career ABs   |.  | Yes |
| hits                   | Batter Career Hits  |.  | Yes |
| Bot               | Batting in Bottom of Inning (Home Team)  |.  | Yes |
| Top                | Batting in Top of Inning (Away Team)  |.  | Yes |
| L-L               | Batter is Lefty; SP is Lefty  |.  | Yes |
| L-R               | Batter is Lefty; SP is Righty |.  | Yes |
| R-L                | Batter is Righty; SP is Lefty  |.  | Yes |
| R-R                | Batter is Righty; SP is Righty  |.  | Yes |
| rp_BA_bp               | Recent Play Batting AVG for Bullpen |.  |.  | No |
| rp_AB_div_PA_bp        | Recent Play YTD Batting AVG for Bullpen  |  |.   | No |
| ytd_BA_bp              | YTD Batting AVG for Bullpen  |.  | No |
| ytd_AB_div_PA_bp       | YTD AB/PA for Bullpen  |.  | No |



# Using BTS2!
1. Get Statcast data
2. 
