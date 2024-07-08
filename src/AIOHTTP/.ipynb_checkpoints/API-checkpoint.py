# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:32:11 2020

@author: ai
"""
from aiohttp import web
import os
import json
import aiohttp_jinja2
import jinja2
import io
import base64
import numpy as np

import API_inference


async def inference(request):
    
    data = await request.post()
    
    message = b''
    if not data['file']:
        message += str("Please select an image!").encode('UTF-8')
        return web.Response(body=message, content_type="text/html")
        
    
    buffer = data['file'].file.read()
    before_img, after_img = API_inference.inference(buffer)    
    before_img = before_img.resize(after_img.size)
    
    
    before_img_buffer = io.BytesIO()
    before_img.save(before_img_buffer, format='PNG')
    
    after_img_buffer = io.BytesIO()
    after_img.save(after_img_buffer, format='PNG')

    #img_buffer = io.BytesIO(after_img)  

    message += "real".encode('UTF-8')
    message += '<br>'.encode('UTF-8')
    message += '<img src="data:image/jpeg;base64,'.encode('UTF-8')
    message += base64.b64encode(before_img_buffer.getvalue())
    message += '"/><br>'.encode('UTF-8')
    
    message += "fake".encode('UTF-8')
    message += '<br>'.encode('UTF-8')
    message += '<img src="data:image/jpeg;base64,'.encode('UTF-8')
    message += base64.b64encode(after_img_buffer.getvalue())
    message += '"/><br>'.encode('UTF-8')

    content = message
    return web.Response(body=content, content_type="text/html")

def load_model(opt):
    
    API_inference.load_model(opt)
    
    return 