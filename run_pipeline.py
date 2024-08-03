from pipeline.training_pipeline import train_pipeline
# from steps.clean_data import clean_data
# from steps.evaluation import evaluation
# from steps.ingest_data import ingest_data
# from steps.model_train import train_model
# from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri

from zenml.client import Client

if __name__ == "__main__":
    # training = train_pipeline(
    #     ingest_data(),
    #     clean_data(),
    #     train_model(),
    #     evaluation(),
    # )

    # print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipeline(data_path=r"\Users\31ash\Desktop\mlops\data\olist_customers_dataset.csv")
