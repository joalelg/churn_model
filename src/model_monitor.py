
import yaml
import argparse
import pandas as pd
import evidently
# from evidently.dashboard import Dashboard
# from evidently.tabs import DataDriftTab,CatTargetDriftTab
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.metric_preset import DataQualityPreset
from evidently.metric_preset import RegressionPreset
from evidently.metric_preset import ClassificationPreset
from evidently.metric_preset import TargetDriftPreset


def read_params(config_path):
    """
    read parameters from the params.yaml file
    input: params.yaml location
    output: parameters as dictionary
    """
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def model_monitoring(config_path):
    config = read_params(config_path)
    train_data_path = config["raw_data_config"]["raw_data_csv"]
    new_train_data_path=config["raw_data_config"]["new_train_data_csv"]
    target = config["raw_data_config"]["target"]
    monitor_dashboard_path = config["model_monitor"]["monitor_dashboard_html"]
    monitor_target = config["model_monitor"]["target_col_name"]

    ref=pd.read_csv(train_data_path)
    cur=pd.read_csv(new_train_data_path)

    ref=ref.rename(columns ={target:monitor_target}, inplace = False)
    cur=cur.rename(columns ={target:monitor_target}, inplace = False)
    
    data_drift_report = Report(metrics=
        [DataDriftPreset(num_stattest='ks', cat_stattest='psi', num_stattest_threshold=0.2,
                         cat_stattest_threshold=0.2),
         TargetDriftPreset(num_stattest='ks', cat_stattest='psi'),
         DataQualityPreset()
        ])  

    data_drift_report.run(reference_data=ref, current_data=cur)
    data_drift_report    

    data_drift_report.save_html(monitor_dashboard_path)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    model_monitoring(config_path=parsed_args.config)
