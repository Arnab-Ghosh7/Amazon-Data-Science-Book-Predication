from cnnClassifier import logger

from cnnClassifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline
)
from cnnClassifier.pipeline.stage_03_training import (
    ModelTrainingPipeline
)
from cnnClassifier.pipeline.stage_04_evaluation import (
    EvaluationPipeline
)


def run_stage(stage_name: str, pipeline_class):
    try:
        logger.info("==================================================")
        logger.info(f">>>>>> Stage started: {stage_name} <<<<<<")

        pipeline = pipeline_class()
        pipeline.main()

        logger.info(f">>>>>> Stage completed: {stage_name} <<<<<<")
        logger.info("==================================================\n")

    except Exception as e:
        logger.exception(f"❌ Error in stage: {stage_name}")
        raise e


if __name__ == "__main__":

    # -----------------------------
    # Stage 01: Data Ingestion
    # -----------------------------
    run_stage(
        stage_name="Data Ingestion",
        pipeline_class=DataIngestionTrainingPipeline
    )

    # -----------------------------
    # Stage 03: Training (NLP Model)
    # -----------------------------
    run_stage(
        stage_name="Training",
        pipeline_class=ModelTrainingPipeline
    )

    # -----------------------------
    # Stage 04: Evaluation
    # -----------------------------
    run_stage(
        stage_name="Evaluation",
        pipeline_class=EvaluationPipeline
    )
