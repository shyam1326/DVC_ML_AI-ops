import yaml
import os
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import json

def read_yaml(path : str) -> dict:
    with open(path, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
    
    return content

def create_directory(dirs : list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory {dir_path}")

def save_local_df(data, data_path):
    data.to_csv(data_path, sep=';', index=False)
    print(f"Data is saved at {data_path}")

def evaluate_merics(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    return rmse, mae, r2

def save_reports(report:dict, report_path:str):
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"Report is saved at {report_path}")