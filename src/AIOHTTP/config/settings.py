# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:32:19 2020

@author: ai
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # 專案路徑
STATIC_DIR = os.path.join(BASE_DIR, 'template/src/assets')       # 靜態檔案路徑
SCRIPTS_DIR = os.path.join(BASE_DIR, 'template/src/assets/scripts')       # 靜態檔案路徑
styles_DIR = os.path.join(BASE_DIR, 'template')
TEMPLATE_DIR = os.path.join(BASE_DIR, '../')   # 模版HTML路徑     