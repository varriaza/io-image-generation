from models.dreamshaper import Dreamshaper
from models.lightning import Lightning
from models.ssd_1B import SSD_1B
import yaml
import sys

def load_variables(yaml_file) -> dict[str, any]:
    """
    Load the variables from the yaml file.
    """
    try:
        with open("config_files/" + yaml_file, 'r') as file:
            variables = yaml.safe_load(file)
    except FileNotFoundError:
        if yaml_file == "ssd_18.yml":
            raise FileNotFoundError(f"File {yaml_file} not found in config_files/. Please check your spelling! The correct file name uses a 'b' not an '8'.yml")
        raise FileNotFoundError(f"File {yaml_file} not found in config_files/. Please check your spelling!")
    return variables

def main(yaml_file):
    """
    Run the model specified in the yaml file.
    """
    # Load variables and standardize to lowercase
    variables = load_variables(yaml_file)
    model_name = variables['model'].lower()

    if model_name == "dreamshaper":
        model = Dreamshaper(yaml_file)
    elif model_name == "lightning":
        model = Lightning(yaml_file)
    elif model_name == "ssd_1b":
        model = SSD_1B(yaml_file)
    else:
        raise NotImplementedError(f"Model {model_name} not implemented. Please check your spelling. Case does not matter.")

    model.run_model()    

if __name__ == "__main__":
    main(sys.argv[1])

