from pathlib import Path

# ✅ RELATIVE IMPORTS (THIS FIXES EVERYTHING)
from ..constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from ..utils.common import read_yaml, create_directories
from ..entity.config_entity import (
    DataIngestionConfig,
    TrainingConfig,
    EvaluationConfig
)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    # -----------------------------
    # Data Ingestion (CSV)
    # -----------------------------
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

    # -----------------------------
    # Training (NLP / CSV)
    # -----------------------------
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        params = self.params

        training_data = (
            Path(self.config.data_ingestion.unzip_dir)
            / "amazon_data_science_books_cleaned.csv"
        )

        create_directories([training.root_dir])

        return TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            training_data=training_data,
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            max_features=params.MAX_FEATURES,
            ngram_range=tuple(params.NGRAM_RANGE),
        )

    # -----------------------------
    # Evaluation
    # -----------------------------
    def get_evaluation_config(self) -> EvaluationConfig:
        return EvaluationConfig(
            model_path=Path("artifacts/training/model.h5"),  # sklearn model
            training_data=Path(
                self.config.data_ingestion.unzip_dir
            ) / "amazon_data_science_books_cleaned.csv",
        )
