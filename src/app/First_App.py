import streamlit as st
st.title("Vorhersage der deutschen  C02-Emissionen")

"Autor: Edwin Ueberschär (https://github.com/EdwinUe)"

from scipy.stats import linregress
st.subheader("Vorhersage")

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
emissions_per_year = [10.3, 10.0, 10.1, 10.2, 9.7, 9.7, 9.7, 9.5, 9.1, 8.5, 7.7]

regression_result = linregress(years, emissions_per_year)
scipy_slope = regression_result.slope
scipy_intercept = regression_result.intercept

def scipy_model(desired_year):
    model_result = scipy_slope * desired_year + scipy_intercept
    return model_result

desired_year = st.slider("Jahr", min_value = 1950, max_value = 2050, value = 2022)

prediction = scipy_model(desired_year)
prediction_rounded = round(prediction, 2)

prediction_prev_year = scipy_model(desired_year-1)
prediction_prev_year_rounded = round(prediction_prev_year, 2)
percantage_diffrence = (((prediction_rounded - prediction_prev_year) / prediction_prev_year)*100)
percantage_diffrence_rounded = round(percantage_diffrence, 2)

st.write("Vorhersage der Emissionen für das Jahr ", desired_year, " ist:")

st.metric("Tonnen pro Jahr pro Kopf",prediction_rounded,delta = percantage_diffrence_rounded,delta_color = "inverse")

st.write("Im Vergleich zum Vorjahr", desired_year-1, "mit", prediction_prev_year_rounded, "Tonnen pro Jahr ist dies eine prozentuale Abweichung von ", percantage_diffrence_rounded, "%.")
""
""
""
"Das Modell ist ein lineares Regressionsmodell auf Grundlage von Daten von 2010 bis 2020."
"Es steht ein Datenpunkt pro Jahr zur Verfügung"
""
"Die Daten stammen aus den folgenden Quellen"
"- https://www.icos-cp.eu/science-and-impact/global-carbon-budget/2021"
"- https://zenodo.org/record/5569235#.YkIDQ-dBz-g"
#%%
