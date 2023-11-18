from box.exceptions import BoxValueError
from box import ConfigBox
from pathlib import Path
from typing import Union, Any
import base64
import os
import yaml
from src.cnnClassifier.logging import logger
import json
import dill
# from ensure import ensure_annotations

"""_summary_

ensure_raises_regex = unittest_case.assertRaisesRegexp

changed with ensure_raises_regex = getattr(unittest_case, 'assertRaisesRegex', 
unittest_case.assertRaisesRegexp)

Still doesnt work


"""


def read_yaml(path: Path) -> ConfigBox:
    """reads yaml files returns configbox object

    Args:
        path (Path): _description_

    Returns:
        ConfigBox: _description_
    """
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path} loaded succesfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file empty")

    except Exception as e:
        raise e


def create_dirs(path_to_dirs: list, verbose=True):
    """create list of directories

    Args:
        path_to_dirs (list): _description_
        verbose (bool, optional): _description_. Defaults to True.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")


def save_json(path: Path, data: dict):
    """saves dict data in json format 
    inside specified path

    Args:
        path (Path): _description_
        data (dict): _description_
    """

    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    logger.info(f"json file saved at : {path}")


def load_json(path: Path) -> ConfigBox:
    """ load json data returns configbox object

    Args:
        path (Path): _description_
        data (dict): _description_
    """

    with open(path) as file:
        content = json.load(file)
    logger.info(f"json file loaded succesfully from {path}")
    return ConfigBox(content)


def save_bin(data: Union[bytes, bytearray], path: Path):
    """Saves binary data to the given path. 
    'YOU can check later maybe'2!!!!!!!'

    Args:
        data (Union[bytes, bytearray]): Binary data to be saved.
        path (Path): Path where the binary data will be saved.
    """
    with open(path, 'wb') as file:
        dill.dump(obj=data, file=file)
    logger.info(f"Binary file saved at: {path}")


def load_bin(path: Path) -> Any:
    """Load Binary Data

    Args:
        path (Path): _description_

    Returns:
        Any: _description_
    """
    data = dill.load(path)
    logger.info(f"Binary fşle loaded from {path}")
    return data


def get_size(path: Path) -> str:
    """Get size in KB

    Args:
        path (Path): _description_

    Returns:
        str: _description_
    """
    size = round(os.path.getsize(path)/1024)
    return f"~ {size} KB"


def decode_image(imgstr, filename):
    imgdata = base64.b64decode(imgstr)
    with open(filename, "wb") as file:
        file.write(imgdata)
        file.close()


def encode_image_base64(cropped_image_path):
    with open(cropped_image_path, "rb") as file:
        return base64.b16encode(file.read())
