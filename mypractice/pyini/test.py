#encoding:utf-8
'''
Created on Nov 14, 2013

@author: liuxue
'''
#coding=utf-8   
  
import ConfigParser   
  
def writeConfig(filename):   
    config = ConfigParser.ConfigParser()   
    # set db   
    section_name = 'db'  
    config.add_section( section_name  )   
    config.set( section_name, 'dbname', 'MySQL')   
    config.set( section_name, 'host', '127.0.0.1')   
    config.set( section_name, 'port', '80')   
    config.set( section_name, 'password', '123456')   
    config.set( section_name, 'databasename', 'test')   
       
    # set app   
    section_name = 'app'  
    config.add_section( section_name  )   
    config.set( section_name, 'loggerapp', '192.168.20.2')   
    config.set( section_name, 'reportapp', '192.168.20.3')   
       
    # write to file   
    config.write( open(filename, 'a') )   
       
def updateConfig(filename, section, **keyv):   
    config = ConfigParser.ConfigParser()   
    config.read(filename)   
    [config.set(section, key, keyv[key]) for key in keyv if config.has_option(section, key)]   
    config.write( open(filename, 'r+') )   
       
# if __name__ == '__main__':   
#     file_name = 'test.ini'  
#     writeConfig(file_name)   
#     updateConfig(file_name, 'app', reportapp = '192.168.100.100')   
#     print "end__"  

#coding=utf-8

import ConfigParser

def writeConfig(filename):
    config = ConfigParser.ConfigParser()
    # set db
    section_name = 'db'
    config.add_section( section_name  )
    config.set( section_name, 'dbname', 'MySQL')
    config.set( section_name, 'host', '127.0.0.1')
    config.set( section_name, 'port', '80')
    config.set( section_name, 'password', '123456')
    config.set( section_name, 'databasename', 'test')
    
    # set app
    section_name = 'app'
    config.add_section( section_name  )
    config.set( section_name, 'loggerapp', '192.168.20.2')
    config.set( section_name, 'reportapp', '192.168.20.3')
    
    # write to file
    config.write( open(filename, 'a') )
    
def updateConfig(filename, section, **keyv):
    config = ConfigParser.ConfigParser()
    config.read(filename)
    [config.set(section, key, keyv[key]) for key in keyv if config.has_option(section, key)]
    config.write( open(filename, 'r+') )
    
if __name__ == '__main__':
    file_name = 'test.ini'
    writeConfig(file_name)
    updateConfig(file_name, 'app', reportapp = '192.168.100.100')
    print "end__"
