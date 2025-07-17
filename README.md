# SpaceX Falcon 9 First Stage Landing Prediction

![Project Status](https://img.shields.io/badge/status-completed-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 🚀 Project Overview

This project was developed as the final deliverable for the [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science). The objective was to predict whether the **first stage of the SpaceX Falcon 9 rocket** would land successfully or not, using machine learning techniques applied to mission telemetry and launch data.

SpaceX frequently reuses its rocket boosters, significantly reducing the cost of space missions. Accurately predicting booster landings helps in improving mission planning, cost optimization, and launch reliability.

---

## 📊 Key Highlights

* **Data Sources:** Launch records from SpaceX, collected via APIs, web scraping, and curated databases.
* **Techniques Used:**

  * Exploratory Data Analysis (EDA)
  * Feature Engineering
  * Classification Algorithms (Logistic Regression, SVM, Decision Trees, kNN)
  * Hyperparameter Tuning
  * Interactive Dashboard with Plotly Dash
* **Best Model:** Decision Tree (post tuning)
* **Performance:**

  * Accuracy: 83.33%
  * Jaccard Score: 0.75 - 0.80
  * F1-Score: up to 0.88

---

## 📊 Model Evaluation Results

| Metric        | LogReg | SVM    | Decision Tree | kNN    |
| ------------- | ------ | ------ | ------------- | ------ |
| Accuracy      | 0.8333 | 0.8333 | **0.8333**    | 0.8333 |
| Jaccard Score | 0.8000 | 0.8000 | **0.7500**    | 0.8000 |
| F1-Score      | 0.8889 | 0.8889 | **0.8571**    | 0.8889 |

> Confusion Matrix for best model (Decision Tree):
>
> * 12/12 successful landings correctly predicted
> * 3 failed landings misclassified as successful (false positives)

---

## 📂 Repository Structure

```
├── code/
│   ├── Multiple Jupyter Notebooks for EDA, preprocessing, modeling, and dashboard
│   ├── spaceX_dash_app.py : Plotly Dash web app
│   └── spaceX_launch_dash.csv : Dataset
│
├── presentation/
│   └── Interactive Dashboard with Plotly Dash.pdf
│
├── report/
│   └── Final technical report in LaTeX (with figures and tables)
```

---

## 📝 Dependencies

* Python 3.8+
* pandas, numpy, matplotlib, seaborn
* scikit-learn
* dash, plotly
* BeautifulSoup, requests
* sqlite3
* LaTeX (for compiling report)

To install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📈 Dashboard Preview

An interactive web dashboard was created using **Plotly Dash** to visualize launch patterns and booster success rates. It includes:

* Launch success pie charts
* Payload vs success scatter plots
* Launch site filtering

The `.pdf` file version of the dashboard interface is available in the `presentation/` folder.

---

## 👤 Author

Gabriel Santiago Murillo Barragán
Biomedical Engineering, Universidad de los Andes
Medical Student, Universidad Nacional de Colombia
[Email me](mailto:gabrielsmurillo@unal.edu.co)

---

## 🔖 License

This project is licensed under the MIT License.
