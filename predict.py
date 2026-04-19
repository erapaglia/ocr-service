import replicate

def predict(image, mask):
    # Usa il modello di inpainting di Replicate (stable diffusion)
    output = replicate.run(
        "stability-ai/stable-diffusion-inpainting:db21e45c...",
        input={
            "image": image,
            "mask": mask,
            "prompt": "clean background, remove text, seamless fill",
            "negative_prompt": "distortion, artifacts, blur",
        }
    )
    return {"output": output}
