churn_model
==============================

## ML churn prediction model MLOps project
Entire machine learning lifecycle with the MLOps tools.

A simple ML churn  model trained using open-source tools. Experiments, API and front-end deployment are done using Flask, GitHub actions, and Heroku. Finally, production model monitoring is done using EvidentlyAI.

The model is built using Kaggle  [churn data](https://www.kaggle.com/c/customer-churn-prediction-2020/data?select=train.csv) subset.
#### Data fields
* number_vmail_messages, numerical. Number of voice-mail messages.
* total_day_calls, numerical. Total number of day calls.
* total_eve_minutes, numerical. Total minutes of evening calls.
* total_eve_charge, numerical. Total charge of evening calls.
* total_intl_minutes, numerical. Total minutes of international calls.
* number_customer_service_calls, numerical. Number of calls to customer service


## Pipeline Creation using DVC
To manage the pipeline we use [DVC](https://dvc.org/)  which, together with Git,  allows to  code and data versioning for reproducibility.
![DVC display](images/dvc01.png)

An advantage of using DVC is that it only executes the stage if any of it's dependencies (data, code or parametres) are changed. 

![DVC display no changes](images/dvc02.png)

## Experiment cicle with MLFlow
Store and manage experiments, i.e. model paramenter and hyper parameter variations, using  [MlFlow](https://mlflow.org/). This tool allows to store and compare all experiment settings in order to compare them and promote the  best performing model to production.

First we launch the server.  

     $ mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 -p 1234
Then the tool will be available for our experiments.
![MlFlow Display](images/mlflow.png) 

## Unit Tests
Set unit tests with Pytest.
![Unit test display vsCode](images/unit_tests_vscode.png)


## Monitor model using EvidentlyAI
Evidently  allows to compare new available data with the data used to train  the model. We can generate Dashbords or json outputs to inspect if if the distribution of any of the new data training features has significantly changed (concept drifft) or if there is a model performance decay (model drift).  Eventually, a shell script could be enabled to automatically retrain the model if there is a detected drift.
![Evidently01](images/Evidently01.png) 
![Evidently01](images/Evidently03.png) 
![Evidently01](images/Evidently04.png) 



## App API and front end display with Flask
A simple web application has been created using [Flask](https://flask.palletsprojects.com/en/2.3.x/) web framework to consume the created model publishing an end point to present the user interface. The resulting app front-end is displayed allowing to get churn predictions from given introduced values as shown in the image below (click to enlarge).
![App demo](images/app_demo.gif)



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
