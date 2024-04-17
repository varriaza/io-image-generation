import yaml
from datetime import datetime
from diffusers import DiffusionPipeline, StableDiffusionXLPipeline

class BaseModel:
    def __init__(self, yaml_file):
        self.variables = self.load_variables(yaml_file)
        # Load variables and standardize to lowercase
        self.model_name = self.variables['model'].lower()
        self.quality = self.variables['quality'].lower()
        self.prompt = self.variables['prompt'].lower()
        self.num_images = int(self.variables['num_images'])
        
    def load_variables(self, yaml_file: str) -> dict[str, any]:
        with open(yaml_file, 'r') as file:
            variables = yaml.safe_load(file)
        return variables
    
    def create_filename(self, image_number:str = '') -> str:
        # Get current date and time
        now = datetime.now()
        # Format as string
        timestamp_str = now.strftime('%Y%m%d-%H%M%S')
        # Use timestamp in filename
        if image_number != '':
            filename = f'image_results/{self.model_name}_{timestamp_str}_{image_number}.png'
        else:
            filename = f'image_results/{self.model_name}_{timestamp_str}.png'
        return filename

    def create_images(self, pipe: DiffusionPipeline|StableDiffusionXLPipeline, *args, **kwargs) -> None:
        """
        Run the model and save the output image(s).
        Args:
            pipe (DiffusionPipeline): The model to run.
            *args: Additional arguments for the model.
            **kwargs: Additional keyword arguments for the model.
        """
        images = pipe(*args, **kwargs).images
        if self.num_images == 1:
            filename = self.create_filename()
            images[0].save(filename)
        else:
            for i in range(self.num_images):
                filename = self.create_filename(str(i+1))
                images[i].save(filename)
        