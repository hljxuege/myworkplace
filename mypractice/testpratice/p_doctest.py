#encoding:utf-8
'''
Created on Apr 28, 2013

@author: liuxue
'''

def simple_run_docTest():
    '''
    >>> simple_run_docTest()
    'A'
    '''
    return 'A'

if __name__ == "__main__":
    import doctest
    doctest.testmod()