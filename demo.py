from adultcensus.pipeline.pipeline import Pipeline
from adultcensus.exception import adultcensusException
from adultcensus.logger import logging
from adultcensus.config.configuration import Configuartion
from adultcensus.component.data_transformation import DataTransformation

def main():
    try:
        pipeline = Pipeline()
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        # # data_validation_config = Configuartion().get_data_transformation_config()
        # # print(data_validation_config)
        # schema_file_path=r"D:\Project\machine_learning_project\config\schema.yaml"
        # file_path=r"D:\Project\machine_learning_project\adultcensus\artifact\data_ingestion\2022-06-27-19-13-17\ingested_data\train\adultcensus.csv"

        # df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()

