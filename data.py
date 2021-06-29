# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:07:22 2021

@author: acer
"""

import glassdoor_selenium_scraper as gs
import pandas as pd

path = "C:/Users/acer/Documents/ds_salary_proj/scraping-glassdoor-selenium-master/chromedriver"

df = gs.get_jobs('data scientist',15,False,path)