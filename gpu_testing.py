import pynvml

# This script is used to double check what kind of GPU we are running with
pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0)
gpu_name = pynvml.nvmlDeviceGetName(handle)
vram_size = pynvml.nvmlDeviceGetMemoryInfo(handle).total / (1024**3)
print(f"GPU Name: {gpu_name}")
print(f"VRAM size: {vram_size:.2f} GB")
pynvml.nvmlShutdown()
