# DSA 210 Project
This project is about the forest fires in Mediterranean in the near past. The project collects data from various data sources about weather, population density, forest type as expected, but it also is concerned about systematic response to forest fires, in other words government spending and related measures. Due to limited time and resources this project will only focus on a handful of countries from the Mediterranean. 
The docs link for the report images and respective explanations (the report is the readme itself): https://docs.google.com/document/d/1Wkv6w7k9nX8pgV3_HMwuxHuyrA1awZuVN6Idq8xv2Ks

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

# Hypothesis Testing

- Hypotheses tested at this stage:
    For each weather variable W(temperature, wind, precipitation):
  
      H0: Beta_x = 0 (Variable has no association with the wildfire outcome)
      HA: Beta_x != 0 (Variable has statistically significant association with the wildfire outcome)


    These hypotheses are tested for both fire incidence(frequency) and burnt area(severity).
  
- Methodology:
Multivariable regression was used since the effect was expected to be a combination. A country effect variable was also introduced to account for fixed factors related to the countries. p-values were estimated using the standart errors at country level. Significance level was set at 5%.

- Burned Ratio Results:

  Temperature showed a positive coefficient(0.17) with p=0.003(significant). This can be used to conclude that temperature is positively associated with fire severity

  Precipitation showed a negative coefficient(-0.71) with p=0.001(significant). This can be used to conclude that precipitaion is negatively associated with fire severity

  Wind showed a negative coefficient(-0.04) with p=0.817(not significant). Wind data cannot be used to show proper association with fire severity.

  R^2 value was 0.62, which indicated some moderate explanatory power. As also warned by the library itself, there still exists suspicions of multicolinarity between variables, which drove further ML applications.

- Fire Incidence Results:

  Temperature showed a negative coefficient(-0.22) with very high significance. Although it showed significance, the counter-intuitiveness is apparent. This can be explained by some interdependency and regime dependent structure of the data at this point(further investigations will provide evidence towards this claim)

  Precipitation showed a negative coefficient(-1.44) with very high significance. This can be used to conclude that precipitaion is negatively associated with fire frequence. This also confirms precipitaion being a dominating variable among all three.

  Suprisingly wind showed a negative coefficient(-0.89) with very high significance. This at this point seems to have been caused my some regime dependency or interdependence among variables, this also shows wind's possible significance for further investigations.

Model showed moderate explanatory power compared to the null case. (pseudo R^2=0.1860)

- Overall:
All hypotheses other than burnt area/wind showed statistically significant results. Fire incidence seemed to be better associated with weather factors compared to burnt ratio. Both models showed indications towards a need to investigate interdependency. The limitations of linear regression being its additiveness and it being completely linear rather than considering tresholds or interdependency must be kept in mind when interpreting these results.

# ML Applications

- Motivation:
  Hypothesis testing revealed the need for further investigations on nonlinear interactions and strong heterogeneoity between countries. So, ML is done to uncover different regimes, search for nonlinear relations and be complementary to hypothesis testing.

- The First One: PCA
  PCA allows for the identification of dominant climate regimes and visualizing the climate structure.

  First, every variable was standartized as expected in PCA. Then, PCA was applied to fire season weather variables.

  As for results, the two principal components(PC1,PC2) seemed to explain ~91% of the variance. PC1(~62%) appeared to be the contrast between high moisture & low temperature/wind components and low moisture & hot/windy components, whereas PC2(~28) appeared to be between high temperature & low wind and low temperature & high wind.

- Second One: K-Means
  PCA showed that most of the climate variability could be represented in two dimensions. K-Means clustering was applied to identify distinct climate regimes during the fire season. The aim was to see if there existed regimes which weren't able to be detected by linear regression.

  K-Means was applied with PC1 and PC2, since they were standartized and structured. Different values of K were tested, and silhouette scores were used as the main cariteria.

  Although higher K values had slightly better silhouette scores, K = 6 was selected. This number of clusters seemed to provide sufficient separation between climate regimes while preserving interpertability and avoiding 

  When wildfire outcomes were examined across clusters, clear differences emerged. Some clusters corresponded to dry and windy regimes with high fire incidence and higher burned ratios, while others represented wetter or milder regimes with consistently lower fire activity. This result provided direct evidence that wildfire behavior is regime-dependent rather than globally linear.

  The clustering results supported earlier findings from hypothesis testing, where some variables(wind,temp) appeared insignificant in global regressions but became meaningful within specific climate regimes.

- Third One: Decision Trees with Raw Data
  While clustering provided insight into regime-level differences, it didn't directly model wildfire outcomes. Decision trees were applied to capture nonlinear relationships, threshold effects, and interactions between weather variables.

  Decision tree regressors were trained separately for two targets:
  burned ratio (severity),
  fire count (frequency).

  Temperature, precipitation, and wind speed were used as raw input features to preserve physical interpretability. The dataset was split into training(75%) and test(25%) sets, and hyperparameters such as maximum depth and minimum samples per leaf were tuned to avoid overfitting.

  For fire count, decision trees achieved high predictive performance on the test set (R² ≈ 0.90). Precipitation consistently appeared as the primary splitting variable, confirming its dominant role in determining fire frequency. Temperature and wind further refined the predictions within dry regimes.

  For burned ratio, predictive performance was notably lower (test R² ≈ 0.20). This indicated that fire severity is more difficult to predict using seasonal averages alone and is likely influenced by additional factors such as suppression capacity, fuel continuity, and extreme short-term events.

  These results highlighted a key distinction: weather conditions are much more effective at explaining how often fires occur than how severe they become. (As discussed in hypothesis testing part)

- Fourth One: Decision Trees with PCA
  To test whether regime-level information improves performance, decision trees were also trained using PC1 and PC2 instead of raw weather variables. This put the focus on climate structure rather than individual measurements.

  For burned ratio, performance improved substantially compared to raw-feature trees (test R² ~0.37). PC2 emerged as the most important feature, indicating that wind–temperature contrasts play a significant role in determining fire severity once ignition occurs.

  For fire count, performance decreased compared to raw-feature trees (test R² ~0.65). This suggests that while PCA is useful for reducing noise and capturing regimes, it may dilute strong single-variable signals—particularly precipitation—that are crucial for predicting fire frequency.

- Overall:
  ML methods complemented hypothesis testing by uncovering nonlinear, regime-dependent behavior that linear models could not capture. PCA revealed that climate variability during the fire season is effectively low-dimensional. K-Means showed that wildfire activity differs substantially across climate regimes. Decision trees demonstrated that fire frequency and fire severity respond differently to climatic conditions and require different modeling strategies.

  Overall, the ML analysis provided a structured explanation for why some variables appeared weak or counter-intuitive in linear regression, while still playing an important role within specific climatic regimes.

# Results

This project investigated the relationship between fire season weather conditions and wildfire activity in selected Mediterranean countries, focusing on two distinct wildfire outcomes: fire incidence (frequency) and burned ratio (severity). Results from exploratory analysis, hypothesis testing, and machine learning methods consistently indicated that wildfire behavior is both multivariate related and regime dependent.

From hypothesis testing, precipitation emerged as the most robust and consistent climatic factor. It showed a strong negative association with both fire incidence and burned ratio, indicating that moisture availability plays a central role in limiting both the likelihood and severity of forest fires. Temperature and wind, on the other hand, exhibited more complex behavior. While temperature showed a positive association with burned ratio and a significant but counter-intuitive negative association with fire incidence, wind speed was only statistically significant for fire incidence and not for burned ratio.

The OLS model for burned ratio achieved an R^2 of approximately 0.62, suggesting moderate explanatory power when climate variables and country fixed effects are considered together. In contrast, fire incidence models based on Poisson and Negative Binomial regressions showed moderate pseudo-R^2 values (~0.16–0.19), reflecting the inherently stochastic nature of wildfire occurrence even after normalization.

Machine learning methods helped clarify and extend these findings. PCA demonstrated that nearly all climate variability during the fire season could be summarized by two principal components. The first component (PC1) represented a moisture gradient separating wet, mild conditions from dry, hot, and windy regimes, while the second component (PC2) captured a temperature–wind contrast relevant to fire spread dynamics.

K-Means clustering applied to the PCA space revealed distinct climate regimes with systematically different wildfire outcomes. Some clusters were consistently associated with high fire incidence and higher burned ratios, while others showed low wildfire activity. This confirmed that global linear effects mask regime-specific behavior.

Decision tree models further supported these conclusions. Fire incidence was highly predictable from seasonal climate variables, particularly precipitation, indicating strong nonlinear and threshold effects. Burned ratio, however, proved substantially harder to predict, even with nonlinear models, suggesting that severity depends on additional factors beyond seasonal climate averages.

# Discussion

Taken together, the results suggest that fire frequency and fire severity are governed by different mechanisms. Fire incidence appears to be strongly controlled by broad climatic conditions, especially moisture availability, while burned ratio depends more heavily on regime-specific and conditional effects involving temperature and wind.

The apparent contradictions observed in linear regression results—such as the negative association between temperature and fire incidence or the insignificance of wind for burned ratio—are better understood once regime dependence and multivariate interactions are considered. PCA and clustering revealed that weather variables do not act independently, and decision trees showed that their effects are often conditional on thresholds and combinations rather than additive linear contributions.

Importantly, machine learning methods did not replace hypothesis testing but rather complemented it. Hypothesis testing established statistically significant associations, while ML methods explained why these associations vary across regimes and why linear models alone are insufficient for capturing wildfire dynamics.

Overall, the findings indicate that Mediterranean wildfire behavior cannot be adequately described by single-variable or globally linear models. Instead, wildfire activity reflects a combination of moisture conditions, thermal stress, wind dynamics, and regime-specific interactions.

# Limitations

Several limitations should be considered when interpreting the results of this study:

Analysis was done with monthly/seasonal averages which may provide inaccurate results considering that fires are also associated with extreme conditions.

The linear regression model used for this project may be too rigid to comprehensively express the model.

The primary data used in this project was initially collecte by reports, so there might be organizational inefficiencies etc. that actually damage the initial data.

The relatively small sample size, especially for some countries, limits the complexity of models and the ability to explore higher-order interactions.

Machine learning models are focused on interpretability and did not include socio-economic or institutional variables due to data limitations.

Results are specific to selected Mediterranean countries and may not generalize to other climatic regions.

# References:
I have stored all my conversations with LLMs(only ChatGPT) and openly available data was used for academic purposes.
