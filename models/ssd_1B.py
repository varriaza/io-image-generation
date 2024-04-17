from diffusers import StableDiffusionXLPipeline
import torch
from models.base_model import BaseModel

class SSD_1B(BaseModel):
    def __init__(self, yaml_file):
        super().__init__(yaml_file)
        self.negative_prompt = self.variables['negative_prompt'].lower()

    def run_model(self) -> None:
        """
        Run the model and save the output image(s).
        """
        torch_dtype=torch.float16
        variant="fp16"

        # Set quality metrics
        if self.quality == "high":
            num_inference_steps = 16
        elif self.quality == "medium":
            num_inference_steps = 8
        elif self.quality == "low":
            num_inference_steps = 4
        else:
            raise ValueError("Quality must be 'high', 'medium', or 'low'")    

        # Load model
        pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch_dtype, use_safetensors=True, variant=variant, )
        pipe.to("cuda")

        self.create_images(pipe, prompt=self.prompt, negative_prompt=self.negative_prompt, num_images_per_prompt=self.num_images, num_inference_steps=num_inference_steps, guidance_scale=9)

