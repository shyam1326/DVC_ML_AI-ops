from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os

def get_data(config_path):
    config = read_yaml(config_path)
    data_path = config['data_source']
    data = pd.read_csv(data_path, sep=';')

    # Save the data in a local directory
    # create path to artifacts directory : artifacts/raw_local_dir/data.cs
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)

    create_directory(dirs=[raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    
    data.to_csv(raw_local_file_path, sep=';', index=False)






if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()
    # print(parsed_args.config)
    get_data(config_path= parsed_args.config)
 