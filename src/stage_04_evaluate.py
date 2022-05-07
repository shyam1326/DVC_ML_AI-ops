from src.utils.all_utils import read_yaml, create_directory, save_local_df, evaluate_merics, save_reports
import argparse
import pandas as pd
import os
import joblib



def evaluate(config_path, params_path):

    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # create path to artifacts directory : artifacts/raw_local_dir/data.cs
    artifacts_dir = config['artifacts']['artifacts_dir']
    split_data_dir = config['artifacts']['split_data_dir']
    test_data_filename = config['artifacts']['test']

        
    test_data_path = os.path.join(artifacts_dir, split_data_dir, test_data_filename)


    df = pd.read_csv(test_data_path, sep=';')

    test_x = df.drop(['quality'], axis=1)
    test_y = df['quality']


    model_dir = config['artifacts']['model_dir']
    model_filename = config['artifacts']['model_filename']
    model_path = os.path.join(artifacts_dir, model_dir, model_filename)
    
    # load model
    model = joblib.load(model_path)
    print("model Loaded succesfully")

    # Prediction
    pred = model.predict(test_x)
    rmse, mae, r2 = evaluate_merics(test_y, pred)
    print(f"RMSE: {rmse}, MAE: {mae}, R2: {r2}")

    scores_dir = config['artifacts']['reports_dir']
    scores_dir_path = os.path.join(artifacts_dir, scores_dir)

    create_directory(dirs = [scores_dir_path])

    scores_filename = config['artifacts']['scores']
    scores_filepath = os.path.join(scores_dir_path, scores_filename)

    scores = {
        'RMSE': rmse,
        'MAE': mae,
        'R2': r2
    }

    save_reports(report = scores, report_path= scores_filepath)



if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")


    parsed_args = args.parse_args()
    # print(parsed_args.config)
    evaluate(config_path= parsed_args.config, params_path= parsed_args.params)
 
