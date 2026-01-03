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
- Yearly total burnt area by country (Gathered from EFFIS) 
  Source: Bottom of the page: https://forest-fire.emergency.copernicus.eu/applications/data-and-services
Researched data for weather:
- Temperatures (Gathered from ERA5)
- Humidity (Gathered from ERA5)
- Wind (Gathered from ERA5)
  Source: https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics?tab=overview, I used the API key to extract from this database
  
Researched data for governmental capacity:
- GDP at purchasing power parity (Gathered from World Bank)
- GDP per capita at purchasing power parity (Gathered from World Bank)
- Spending for fire prevention (Gathered from related government reports and Eurostat)
- Spending for fire fighting (Gathered from related government reports and Eurostat)
- _Optional at this stage: Reasons for forest fires, tourism rate_
