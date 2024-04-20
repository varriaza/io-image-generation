import yaml
from datetime import datetime


class BaseModel:
    def __init__(self, yaml_file):
        self.variables = self.load_variables(yaml_file)
        # Load variables and standardize to lowercase
        self.model_name = self.variables["model"].lower()
        self.quality = self.variables["quality"].lower()
        self.prompt = self.variables["prompt"].lower()
        self.num_images = int(self.variables["num_images"])

    def load_variables(self, yaml_file: str) -> dict[str, any]:
        """
        Load the variables from the yaml file.
        """
        with open("config_files/" + yaml_file, "r") as file:
            variables = yaml.safe_load(file)
        return variables

    def create_filename(self) -> str:
        """
        Create a filename for the output image(s).
        Args:
            image_number (str): The number of the image. Used for multiple images. Defaults to ''.
        Returns:
            str: The filename.
        """
        # Get current date and time
        now = datetime.now()
        # Format as string
        timestamp_str = now.strftime("%Y%m%d-%H%M%S")
        # Use timestamp in filename
        filename = f"image_results/{self.model_name}_{timestamp_str}"
        return filename

    def create_images(
        self, pipe, *args, **kwargs
    ) -> None:
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
            images[0].save(filename + ".png")
        else:
            filename = self.create_filename()
            for i in range(self.num_images):
                images[i].save(filename + f"_{i + 1}.png")
