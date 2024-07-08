import os
#from options.test_options_api import TestOptionsAPI
#from data import create_dataset
from models import create_model
from util.visualizer import save_images
import torchvision.transforms.functional as TF
from torch.utils.data import IterableDataset
from data.base_dataset import get_transform
import numpy as np
import torch

import io
import PIL.Image as Image


global model
global opt

def load_model(opts):
      
    global model
    global opt
    model = create_model(opts)      # create a model given opt.model and other options
    model.setup(opts)               # regular setup: load and print networks; create schedulers
    opt = opts
    if opt.eval:
        model.eval()
        
    return
    

def tensor2im(input_image, imtype=np.uint8):
    """"Converts a Tensor array into a numpy image array.

    Parameters:
        input_image (tensor) --  the input image tensor array
        imtype (type)        --  the desired type of the converted numpy array
    """
    if not isinstance(input_image, np.ndarray):
        if isinstance(input_image, torch.Tensor):  # get the data from a variable
            image_tensor = input_image.data
        else:
            return input_image
        image_numpy = image_tensor[0].cpu().float().numpy()  # convert it into a numpy array
        if image_numpy.shape[0] == 1:  # grayscale to RGB
            image_numpy = np.tile(image_numpy, (3, 1, 1))
        image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 255.0  # post-processing: tranpose and scaling
    else:  # if it is a numpy array, do nothing
        image_numpy = input_image
    return image_numpy.astype(imtype)


    
def inference(buffer):
    
    global model
    global opt


    A_img = Image.open(io.BytesIO(buffer))

    #A_path = "data/testA/n02381460_20.jpg"
    #A_img = Image.open(A_path)#.convert('RGB')
    
    input_nc = opt.output_nc if opt.direction == 'BtoA' else opt.input_nc
    transform = get_transform(opt, grayscale=(input_nc == 1)) 
    A = transform(A_img)
    
    A = A.numpy() 
    A = np.array([A])
    A = torch.Tensor(list(A))
    image_list =  {'A': A, 'A_paths': None}

    model.set_input(image_list)  # unpack data from data loader
    model.test()           # run inference
    visuals = model.get_current_visuals()  # get image results

    
    for label, im_data in visuals.items():
        image_numpy = tensor2im(im_data)
        aspect_ratio=1.0

        image_pil = Image.fromarray(image_numpy)
        h, w, _ = image_numpy.shape
    
        if aspect_ratio > 1.0:
            image_pil = image_pil.resize((h, int(w * aspect_ratio)), Image.BICUBIC)
        if aspect_ratio < 1.0:
            image_pil = image_pil.resize((int(h / aspect_ratio), w), Image.BICUBIC)
            
        #image_pil.save("123.png")
  
    return A_img, image_pil