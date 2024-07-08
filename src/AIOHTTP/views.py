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


async def test(request):
    return web.Response(text='111111!') 


async def hello(request):
    return web.Response(text='Hello Aiohttp!')


@aiohttp_jinja2.template('inference.html')
async def index(request):
    return    
