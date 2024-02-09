# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:18:23 2024

JUNGYU LEE
301236221
"""

import logging
import boto3
from botocore.exceptions import ClientError
import time

class StorageService:
    def __init__(self, bucket_name):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
    
    def upload_files(self, files):
        is_success = True
        
        total_start_time = time.time()
        
        for file in files:
            try:
                print(f'Ready to upload - {file}')
                start_time = time.time()
                self.s3_client.upload_file(file, self.bucket_name, file)
                end_time = time.time()
                print(f'Upload completed - {file} ')
                print(f'Time taken - {end_time - start_time:.2f} seconds')
            except ClientError as e:
                logging.error(e)
                is_success = False
        
        total_end_time = time.time()
        print(f'Total time taken: {total_end_time - total_start_time:.2f} seconds')
        
        return is_success

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    
    bucket_name = 'contentcen301236221.aws.ai'
    files = ['JUNGYU1.txt', 'JUNGYU2.txt', 'JUNGYU3.txt']
    
    files_upload = StorageService(bucket_name)
    
    if files_upload.upload_files(files):
        print('All files uploaded successfully.')
    else:
        print('Erorr occurred')
            
                
