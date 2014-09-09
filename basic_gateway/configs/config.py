#encoding:utf-8
'''
Created on Oct 24, 2012

@author: liuxue
'''
#PROJECT NAME
import __dump__
import os

#项目名称
PROJECT_NAME = 'basic gateway'
#项目号码
PROJECT_CODE = 980000
#项目目录
PROJECT_PATH = os.path.dirname(__dump__.__file__)

DEFAULT_PORT = 9891

#日志配置文件
DEFAULT_LOG_CONFIG_PATH = os.path.join(PROJECT_PATH, 'configs', 'logging.conf')
#默认配置文件位置 
DEFAULT_APP_CONFIG_PATH = os.path.join(PROJECT_PATH, 'configs', 'config.yaml')


