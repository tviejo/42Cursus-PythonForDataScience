from load_csv import load
from projection_life import projection_life

gdpp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
life_ex = load("life_expectancy_years.csv")
projection_life(gdpp, life_ex)
