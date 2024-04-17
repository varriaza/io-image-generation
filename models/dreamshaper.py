from diffusers import DiffusionPipeline
import torch
from models.base_model import BaseModel

class Dreamshaper(BaseModel):
    def __init__(self, yaml_file):
        super().__init__(yaml_file)

    def run_model(self) -> None:
        """
        Run the model and save the output image(s).
        """
        # Load model
        pipe = DiffusionPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7")

        # Set quality metrics
        if self.quality == "high":
            num_inference_steps = 16
            pipe.to(torch_device="cuda", torch_dtype=torch.float32)
        elif self.quality == "medium":
            num_inference_steps = 8
            pipe.to(torch_device="cuda", torch_dtype=torch.float32)
        elif self.quality == "low":
            num_inference_steps = 4
            pipe.to(torch_device="cuda", torch_dtype=torch.float16)
        else:
            raise ValueError("Quality must be 'high', 'medium', or 'low'")         

        self.create_images(pipe, prompt=self.prompt, num_inference_steps=num_inference_steps, guidance_scale=8.0, lcm_origin_steps=50, num_images_per_prompt=self.num_images, output_type="pil")


