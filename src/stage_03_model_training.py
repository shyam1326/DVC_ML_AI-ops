from src.utils.all_utils import read_yaml, create_directory, save_local_df
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import joblib



def train_model(config_path, params_path):

    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # create path to artifacts directory : artifacts/raw_local_dir/data.cs
    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']
    train_data_filename = config['artifacts']['train']


        
    train_data_path = os.path.join(artifacts_dir, split_data_dir, train_data_filename)


    df = pd.read_csv(train_data_path, sep=';')

    train_x = df.drop(['quality'], axis=1)
    train_y = df['quality']

    alpha = params['model_params']['ElasticNet']['alpha']
    l1_ratio = params['model_params']['ElasticNet']['l1_ratio']
    random_state = params['base']['random_state']

    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    model.fit(train_x, train_y)

    # Create diurectory for model
    model_dir = config['artifacts']['model_dir']
    model_filename = config['artifacts']['model_filename']

    model_dir = os.path.join(artifacts_dir, model_dir)
    create_directory(dirs = [model_dir])

    model_path = os.path.join(model_dir, model_filename)
    
    # save model
    joblib.dump(model, model_path)
    print("model saved succesfully")



if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")


    parsed_args = args.parse_args()
    # print(parsed_args.config)
    train_model(config_path= parsed_args.config, params_path= parsed_args.params)
 
