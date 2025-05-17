import pandas as pd
import os
from mlProject.components.logger import logger  # Correct import for the logger
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        try:
            # Log the start of the training
            logger.info(f"Starting training with train data from {self.config.train_data_path} and test data from {self.config.test_data_path}")
            
            # Loading train and test data
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)
            logger.info("Data loaded successfully")
        
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return

        # Preprocessing the data
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Log training model details
        logger.info(f"Training ElasticNet model with alpha={self.config.alpha}, l1_ratio={self.config.l1_ratio}")

        # Train the model
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        # Save the trained model
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(lr, model_path)
        
        # Log the model saving process
        logger.info(f"Model saved at {model_path}")
