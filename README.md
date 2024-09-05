# Predictive Modeling for Falcon 9 First Stage Landing Success 🚀

This project focuses on predicting the landing success of SpaceX's Falcon 9 first stage using historical data and various machine learning models. The analysis spans from data collection to visualization, interactive dashboard creation, and predictive modeling.

## Project Overview

SpaceX has revolutionized space travel by successfully reusing Falcon 9 first-stage boosters. This project aims to replicate their approach by predicting the landing success of the Falcon 9 first stage. The repository includes data collection via APIs and web scraping, Exploratory Data Analysis (EDA), interactive mapping, and the development of machine learning models for predictive analytics.

### Key Components:
1. **Data Collection:**
   - SpaceX Launch Data via REST APIs.
   - Historical Falcon 9 launch records via web scraping from Wikipedia.

2. **Exploratory Data Analysis (EDA):**
   - Data wrangling, visualization with Python libraries (e.g., Matplotlib, Seaborn).
   - SQL-based data exploration.
   - Interactive data visualization using Folium and Plotly Dash.

3. **Predictive Modeling:**
   - Classification models (Logistic Regression, Support Vector Machine, Decision Tree, K-Nearest Neighbors).
   - Model tuning using GridSearchCV.
   - Performance evaluation with metrics like accuracy, precision, and F1 score.

## Project Structure


### Notebooks and Files:
- [**SpaceX Data Collection API Notebook**](https://github.com/Sigmanurag/Predictive-Modeling-for-Falcon-9-First-Stage-Landing-Success-/blob/main/jupyter-labs-spacex-data-collection-api.ipynb)
- [**Web Scraping Falcon 9 Launch Records**](https://github.com/Sigmanurag/Predictive-Modeling-for-Falcon-9-First-Stage-Landing-Success-/blob/main/jupyter-labs-webscraping.ipynb)
- [**EDA with Data Visualization**](https://github.com/Sigmanurag/Predictive-Modeling-for-Falcon-9-First-Stage-Landing-Success-/blob/main/edadataviz.ipynb)
- [**EDA using SQL**](https://github.com/Sigmanurag/Predictive-Modeling-for-Falcon-9-First-Stage-Landing-Success-/blob/main/jupyter-labs-eda-sql-coursera_sqllite.ipynb)
- [**Interactive Map with Folium**](https://github.com/Anurag561-tech/Predictive-Modeling-for-Falcon-9-First-Stage-Landing-Success-/blob/main/Space-X%20Launch%20Sites%20Locations%20Analysis%20with%20Folium-Interactive%20Visual%20Analytics.ipynb)
- [**Interactive Dashboard with Plotly Dash**](https://github.com/Anurag561-tech/Predictive-Modeling-for-Falcon-9-First-Stage-Landing-Success-/blob/main/Build%20an%20Interactive%20Dashboard%20with%20Ploty%20Dash%20-%20spacex_dash_app.py)
- [**Predictive Modeling**](https://github.com/Anurag561-tech/Predictive-Modeling-for-Falcon-9-First-Stage-Landing-Success-/blob/main/SpaceX_Machine%20Learning%20Prediction.ipynb)

## Results
- **Model Accuracy**: The best-performing model (Logistic Regression) achieved an accuracy of **83%**.
- **Launch Success Trends**: Geographical factors (e.g., proximity to coastlines, highways) and specific orbits (e.g., ES-L1, GEO) influence launch success rates.

## Visualization

- **Interactive Folium Maps**: Launch sites, geographical proximity analysis, and spatial visualization of launch success.
- **Plotly Dash Dashboard**: Filter launches by site and payload mass, visualizing success rates with pie charts and scatter plots.

## Requirements
- Python 3.x
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn, Plotly Dash
- Folium, BeautifulSoup, Requests
- SQLite for SQL analysis

## Conclusion

This project demonstrates the application of data science techniques in predicting the success of SpaceX Falcon 9 first-stage landings. By utilizing historical launch data and applying various machine learning models, we have gained valuable insights into factors influencing launch outcomes. These insights reveal how data-driven strategies can optimize launch operations and improve decision-making processes.

By understanding which factors contribute most to landing success, this project serves as a foundation for more efficient rocket launches and cost-saving measures in the aerospace industry. It also highlights the potential for further development in predictive modeling to enhance performance and increase reliability in future space missions.

---
© 2024 Anurag Srivastava







