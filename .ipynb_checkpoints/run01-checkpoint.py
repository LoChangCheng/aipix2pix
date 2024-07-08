import os
import subprocess
import src.tools

# parameter

# model/latest_net_G.pth =>　--checkpoints_dir model,  --epoch latest
# model/20_net_G.pth => --checkpoints_dir model, --epoch 20
checkpoints_dir = 'model'
epoch = 'latest'

#The option 'direction' can be used to swap images in domain A and domain B.
direction = 'BtoA'

# gpu ids: e.g. 0  0,1,2, 0,2. use -1 for CPU 
gpu_ids = 0

port = 8801

src.tools.Delete_ipynb_checkpoints('data/')

arg = "--port %d --model test --phase test --checkpoints_dir %s --epoch %s --netG unet_256 --direction %s --dataset_mode single --norm batch --num_test 1  --gpu_ids %d" %(port, checkpoints_dir, epoch, direction, gpu_ids)

cmd = "python src/AIOHTTP-main.py " + arg

subprocess.run(cmd, creationflags = subprocess.CREATE_NEW_CONSOLE)