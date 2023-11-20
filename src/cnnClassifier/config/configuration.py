from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml, create_dirs
from src.cnnClassifier.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFING_FILE_PATH, params_filepath=PARAMS_FILE_PATH) -> None:
        """takes config and params file path 
        creates dirs accordingly...

        Args:
            config_filepath (_type_, optional): _description_. Defaults to CONFING_FILE_PATH.
            params_filepath (_type_, optiona l): _description_. Defaults to PARAMS_FILE_PATH.
        """

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_dirs([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_dirs([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_dirs([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_classes=self.params.CLASSES,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS
        )
        return prepare_base_model_config
