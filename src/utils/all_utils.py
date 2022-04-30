import yaml
import os

def read_yaml(path : str) -> dict:
    with open(path, 'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
    
    return content