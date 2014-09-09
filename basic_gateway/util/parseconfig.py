#encoding:utf-8
'''
Created on Feb 27, 2014

@author: liuxue
'''
import yaml

class SysConfig:
    config_data = {}
    @classmethod
    def load(cls, path):
        SysConfig.config_data = yaml.load(open(path, 'r'))
        assert SysConfig.config_data != {}, u'空的系统配置项'
        
    @classmethod
    def get(cls, k):
        return SysConfig.config_data.get(k)

def initial_sys_config(path):
    SysConfig.load(path)

def get_sys_config(k):
    return SysConfig.get(k)