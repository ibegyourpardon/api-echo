'''
Date: 2022-02-04 22:41:14
LastEditors: ibegyourpardon
LastEditTime: 2022-02-04 22:58:30
FilePath: /api-echo/gunicorn.conf.py
'''
workers = 1    # 定义同时开启的处理请求的进程数量，根据网站流量适当调整
worker_class = 'sync'
bind = "0.0.0.0:5000"