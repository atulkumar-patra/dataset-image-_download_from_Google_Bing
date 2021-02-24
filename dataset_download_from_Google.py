# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:25:04 2021

@author: atulk
"""

from google_images_download import google_images_download

#instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"aeroplane, school bus",
             "limit":5,"print_urls":False}
paths = response.download(arguments)

#print complete paths to the downloaded images
print(paths)

#bing
from bing_image_downloader import downloader
downloader.download("aadhar card", limit=20,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("adhar card", limit=20,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)