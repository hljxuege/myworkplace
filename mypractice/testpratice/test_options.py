#encoding:utf-8
'''
Created on Feb 27, 2014

@author: liuxue
'''
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print args.echo
