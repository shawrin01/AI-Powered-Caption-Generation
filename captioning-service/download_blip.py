from huggingface_hub import snapshot_download

# BLIP model download path
local_dir = "./blip_model"

# Download the model from Hugging Face
snapshot_download(repo_id="Salesforce/blip-image-captioning-base", local_dir=local_dir)

print(f"Model downloaded to: {local_dir}")
