from models.dreamshaper import Dreamshaper
from models.lightning import Lightning
from models.ssd_18 import SSD_18
import yaml
import sys

def load_variables(yaml_file) -> dict[str, any]:
        with open(yaml_file, 'r') as file:
            variables = yaml.safe_load(file)
        return variables

def main(yaml_file):
    # Load variables and standardize to lowercase
    variables = load_variables(yaml_file)
    model_name = variables['model'].lower()

    if model_name == "dreamshaper":
        model = Dreamshaper(yaml_file)
    elif model_name == "lightning":
        model = Lightning(yaml_file)
    elif model_name == "ssd-18":
        model = SSD_18(yaml_file)
    else:
         raise NotImplementedError(f"Model {model_name} not implemented. Please check your spelling. Case does not matter.")

    model.run_model()    

if __name__ == "__main__":
    main(sys.argv[1])

