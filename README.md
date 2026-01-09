# DSA 210 Project
This project is about the forest fires in Mediterranean in the near past. The project collects data from various data sources about weather, population density, forest type as expected, but it also is concerned about systematic response to forest fires, in other words government spending and related measures. Due to limited time and resources this project will only focus on a handful of countries from the Mediterranean.

# Motivation
For the past years forest fires are the one of the most critical topics during summer in the Mediterranean countries. Both from the aspect of nature and of the humans forest fires have devastating effects. For this purpose analysing relevant data to find patterns is important for me. 

# Research Questions 

How does weather values affect number of fires and total burnt area?

# Data Collection and Resources

Primary indicators:
- Yearly number of forest fires by country (Gathered from European Forest Fire Information System(EFFIS)) 
- Yearly total burnt area per forest area by country (Gathered from EFFIS)
- Fire season number of forest fires by country (Gathered from EFFIS)
- Fire season total burnt area per forest area by country (Gathered from EFFIS)
- Yearly number of forest fires per forest area by country (Gathered from EFFIS and World Bank)
  
Source: https://forest-fire.emergency.copernicus.eu/applications/data-and-services

Researched data for weather:
- Temperatures (Gathered from ERA5)
- Humidity (Gathered from ERA5)
- Wind (Gathered from ERA5)

Source: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-monthly-means?tab=overview, I used the API key to extract from this database
  
# Data Cleaning and Formatting

# EDA

Various combinations of variables are first plotted and then checked for correlation accordingly.

- Fire Count and Burnt Area per Forest Area by Country:
First made normal scatter plots but extreme values seemed to sometimes dominate variances and also as number of fires increased data became more noisy. So, log scale was also checked to mitigate those effects.
Fire incidence didn't seem to be in correlation with burnt area universally, for some countries (France, Italy) the effects exists but for others it doesn't. I realized that they were different indicators where burnt area is dependent of the country response and other structural factors(severity) whereas fire count is the frequency/likelihood. Correlation tables also confirmed the case of weak correlations and high variability between countries.

- Fire Season Yearly Temperature Averages:
Results varied greatly among countries, conducted correlation analysis between burnt area and temprature averages. Temperature didn't seem to a very compatible with burnt area, so I moved on to compare it with yearly fire counts which yielded better but still not good enough results. Correlation tables confirmed the visual inspection made prior. This is the first instance of a case of combinations being needed.

- Fire Season Total Precipitation:
Results were generally towards a negative sloped relationship. Burnt area shoved visual correlation in some countries, fire counts showed a stronger (-) relationship. The consistency(low precipitation yearly consistently coincided with extreme damage years) of total precipitation indicated its importance in explaining fires. Although correlation tables showed considerably stronger results inter-country variability was still high.

- Fire Season Average Wind Speed:
Wind showed the weakest of results and consequently was framed as the least important factor(as expected intuitively). There results were mixed between countries, some had (+) and some had (-) slopes. This analysis also raised questions about whether pairwise comparisons were able to catch the whole picture.

- Overall:
Pairwise correlation analyses showed inconsistent(heterogeneous) and weak results. A model which utilized a combination of these factors seemed the better choice at this point. Linear Regression appeared as the first candidate before moving onto clustering and dimentionality reduction. There may be some threshold kind of factors at play also, since it sound intuitive that some factors require others parameters to have reached a certain amount (ie. strong wind and temperature doesn't cause fires if there is a lot of rainfall)





