#!/usr/bin/env python3
import requests
"""
test
"""

def get(url):
    res = requests.get(url)
    return res.text

if __name__ == "__main__":
    url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240401%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240401T171706Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a05506dee9a560b799a6de62aa45a55672bade97ceab6f3a496052c0e2faab16"
    print(get(url))
