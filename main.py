import os 
import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN
from resize import resizing
from color_enhance import colorizing
def main() -> int:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RealESRGAN(device, scale = 2)
    model.load_weights('weights/RealESRGAN_x2.pth', download=True)
    for i, image in enumerate(os.listdir("inputs")):
        image = Image.open(f"inputs/{image}").convert('RGB')
        sr_image = model.predict(image)
        sr_image.save(f'results/{i}.png')
        resizing(f'results/{i}.png', 2)
        colorizing(f'results/{i}.png', f'results/{i}.png')
        
if __name__ == '__main__':
    main()

