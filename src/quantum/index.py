import torch

def checkCuda():
    if torch.cuda.is_available():
        print("CUDA is available")
    else:
        print("No CUDA device available")


checkCuda()
