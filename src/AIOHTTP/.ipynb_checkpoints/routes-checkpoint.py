# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:32:03 2020

@author: ai
"""
from .views import hello, index
from .API import inference
from .config import settings
from .config.settings import STATIC_DIR, TEMPLATE_DIR, SCRIPTS_DIR, styles_DIR

import os

import aiohttp_jinja2
import jinja2

def setup_routes(app):
    
    app.router.add_get('/hello', hello)
    app.router.add_get('/', index)
    app.router.add_get('/inference.html', index)

    #post area
    app.router.add_post('/api/inference', inference)

#def setup_static_routes(app):
    

def setup_template_routes(app):
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    

