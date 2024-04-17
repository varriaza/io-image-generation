from diffusers import StableDiffusionXLPipeline
import torch
from models.base_model import BaseModel

class SSD_18(BaseModel):
    def __init__(self, yaml_file):
        super().__init__(yaml_file)
        self.negative_prompt = self.variables['negative_prompt'].lower()

    def run_model(self) -> None:
        # Set quality metrics
        if self.quality == "high":
            torch_dtype=torch.float32
            variant="fp32"
        elif self.quality == "medium":
            torch_dtype=torch.float16
            variant="fp16"
        elif self.quality == "low":
            torch_dtype=torch.float16
            variant="fp16"
        else:
            raise ValueError("Quality must be 'high', 'medium', or 'low'")    

        # Load model
        pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch_dtype, use_safetensors=True, variant=variant)
        pipe.to("cuda")

        self.create_images(pipe, prompt=self.prompt, negative_prompt=self.negative_prompt)

