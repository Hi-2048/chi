from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os
import numpy as np
from torchvision.transforms import functional as F
import torch
from torchmetrics.image.fid import FrechetInceptionDistance
dataset_path = "path to the standard image"
fake_path =  "path to the fake image"
image_paths = sorted([os.path.join(dataset_path, x) for x in os.listdir(dataset_path)])
real_images = [np.array(Image.open(path).convert("RGB")) for path in image_paths]

def preprocess_image(image):
    image = torch.tensor(image).unsqueeze(0)
    image = image.permute(0, 3, 1, 2) / 255.0
    return F.center_crop(image, (256, 256))

real_images = torch.cat([preprocess_image(image) for image in real_images])

image_paths = sorted([os.path.join(fake_path, x) for x in os.listdir(fake_path)] )
fake_images = [
        np.array(Image.open(path).convert("RGB")) 
        for path in image_paths
        ]
fake_images = torch.cat([preprocess_image(image) for image in fake_images])
# print(real_images.shape)
# print(fake_images.shape)

kid = KernelInceptionDistance(normalize=True)
kid.update(real_images,real=True)
kid.update(fake_images,real=False)
kid_mean, kid_std = kid.compute()
print(f"KID: (mean:{kid_mean},std:{kid_std})")

fid = FrechetInceptionDistance(normalize=True)
fid.update(real_images, real=True)
fid.update(fake_images, real=False)
print(f"FID:|||: {float(fid.compute())}")
