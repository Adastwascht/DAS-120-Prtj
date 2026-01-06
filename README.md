# DSA 210 Project
This project is about the forest fires in Mediterranean in the near past. The project collects data from various data sources about weather, population density, forest type as expected, but it also is concerned about systematic response to forest fires, in other words government spending and related measures. Due to limited time and resources this project will only focus on a handful of countries from the Mediterranean.

# Motivation
For the past years forest fires are the one of the most critical topics during summer in the Mediterranean countries. Both from the aspect of nature and of the humans forest fires have devastating effects. For this purpose analysing relevant data to find patterns is important for me. 

# Research Questions 

1. How does weather values affect number of fires and total burnt area?
2. How does governmental capacity affect number of fires and total burnt area?

# Data Collection and Resources

Primary indicators:
- Yearly number of forest fires by country (Gathered from European Forest Fire Information System(EFFIS)) 
- Yearly total burnt area per forest area by country (Gathered from EFFIS)
- Fire season number of forest fires by country (Gathered from EFFIS)
- Fire season total burnt area per forest area by country (Gathered from EFFIS)
  
Source: https://forest-fire.emergency.copernicus.eu/applications/data-and-services

Researched data for weather:
- Temperatures (Gathered from ERA5)
- Humidity (Gathered from ERA5)
- Wind (Gathered from ERA5)

Source: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-monthly-means?tab=overview, I used the API key to extract from this database
  
Researched data for governmental capacity:
- GDP per capita at purchasing power parity (Gathered from World Bank)
- Total Government Spending Expenditure % of GDP (Gathered from World Bank)

Source: https://databank.worldbank.org/source/world-development-indicators

# Data Cleaning and Formatting

# EDA

Various combinations of variables are first plotted and then checked for correlation accordingly.
Fire Count and Burnt Area per Forest Area by Country:

First made normal scatter plots but extreme values seemed to sometimes dominate variances and also as number of fires increased data became more noisy. So, log scale was also checked to mitigate those effects.
Fire counts didn't seem to be in correlation with burnt area universally, for some countries (France, Italy) the effects exists but for others it doesn't. 

Monthly Temperature Averages:

Results varied greatly among countries, conducted correlation analysis between burnt area and temprature averages. Temperature didn't seem to a very compatible with burnt area, so I moved on to compare it with yearly fire counts which yealded better but still not good enough results.
