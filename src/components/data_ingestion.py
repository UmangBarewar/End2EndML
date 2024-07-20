import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

    # This defines a configuration class using the @dataclass decorator. It specifies the paths where the train, 
    # test, and raw data will be saved.

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        # This class initializes the data ingestion process. The constructor creates an instance of DataIngestionConfig.

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")

            # Create the artifacts directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Saved raw data in artifact directory")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
# This method does the actual data ingestion:

# It reads a CSV file into a pandas DataFrame.
# Creates the 'artifacts' directory if it doesn't exist.
# Saves the raw data to a CSV file.
# Splits the data into training and testing sets.
# Saves the training and testing data to separate CSV files.
# Returns the paths of the training and testing data files.
# If any exception occurs, it raises a CustomException.

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()