import torch
from diffusers import (
    StableDiffusionXLPipeline,
    UNet2DConditionModel,
    EulerDiscreteScheduler,
)
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
from models.base_model import BaseModel

base = "stabilityai/stable-diffusion-xl-base-1.0"
repo = "ByteDance/SDXL-Lightning"
ckpt = "sdxl_lightning_4step_unet.safetensors"  # Use the correct ckpt for your step setting!


class Lightning(BaseModel):
    def __init__(self, yaml_file):
        super().__init__(yaml_file)

    def run_model(self) -> None:
        """
        Run the model and save the output image(s).
        """
        # Note: float32 does not work with this model
        torch_dtype = torch.float16
        variant = "fp16"

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
        unet = UNet2DConditionModel.from_config(base, subfolder="unet").to(
            "cuda", torch_dtype
        )
        unet.load_state_dict(load_file(hf_hub_download(repo, ckpt), device="cuda"))

        pipe = StableDiffusionXLPipeline.from_pretrained(
            base, unet=unet, torch_dtype=torch_dtype, variant=variant
        ).to("cuda")
        # Ensure sampler uses "trailing" timesteps.
        pipe.scheduler = EulerDiscreteScheduler.from_config(
            pipe.scheduler.config, timestep_spacing="trailing"
        )

        self.create_images(
            pipe,
            prompt=self.prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=0,
            num_images_per_prompt=self.num_images,
        )
