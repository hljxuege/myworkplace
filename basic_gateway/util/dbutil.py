#encoding:utf-8
'''
Created on 2012-7-4

@author: Liuxue
'''
from DBUtils.PooledDB import PooledDB
import MySQLdb
from MySQLdb.cursors import Cursor
from logging import getLogger
import os

from errors.dberror import DatabaseError


os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class MysqlPool(object):
    pool = None
    conn = None
    @staticmethod
    def load(host, port, db, user, pswd, timeout):
        MysqlPool.pool = PooledDB(MySQLdb, 1, 1, host=host , port=port, user=user, \
                                  passwd=pswd, db=db, charset='utf8', connect_timeout=timeout, \
                                  cursorclass=Cursor)
        
        MysqlPool.pool.connection().close()
        
    @staticmethod
    def get_mysql_pool():
        return MysqlPool.pool

def initial_mysql(host, port, db, user, pswd, timeout):     
    MysqlPool.load(host, port, db, user, pswd, timeout)

def get_mysql():
    return MysqlPool.get_mysql_pool()

def open_conn():
    '''
    打开数据库连接
    @return: 返回数据库连接
    @raise exception: 
    '''
    try:
        conn = get_mysql().connection()
    except MySQLdb.DatabaseError, e:
        raise DatabaseError(u'数据库连接失败！', 'open_conn'+str(e))
    except Exception, e: 
        raise DatabaseError(u'数据库连接失败！', 'open_conn'+str(e))
    return conn


def fetch_data(conn, sql_param): 
    '''
    通过给定sql语句获取数据，并返回该数据
    @param conn: 数据库连接对象
    @param sql_param: 包含SQL语句和param的元组
    @return: 数据库查询结果
    '''
    try:
        cur = conn.cursor()
        cur.execute(sql_param[0], sql_param[1])
        data = cur.fetchall()
    except Exception, e: 
        raise DatabaseError(u'获取数据失败！','fetch_data'+str(e))
    finally:
        cur.close()

    return data

def fetch_one (conn, sql_param): 
    '''
    通过给定sql语句获取数据，并返回该数据
    @param conn: 数据库连接对象
    @param sql_param: 包含SQL语句和param的元组
    @return: 数据库查询结果
    '''
    try:
        cur = conn.cursor()
        cur.execute(sql_param[0], sql_param[1])
        data = cur.fetchone()
    except Exception, e: 
        raise DatabaseError(u'获取数据失败！','fetch_one'+str(e))
    finally:
        cur.close()

    return data

def update_data(conn, sql_param):
    '''
    通过给定sql语句获取数据，并返回该数据
    @param conn: 数据库连接对象
    @param sql_param: 包含SQL语句和param的元组
    @return: 字典数组
    '''
    cur = None
    try:
        cur = conn.cursor()
        cur.execute(sql_param[0], sql_param[1])
        conn.commit()
        return cur.rowcount
    except Exception, e: 
        raise DatabaseError(u'数据库更新！', 'update_data'+str(e))
    finally:
        if cur:
            cur.close()

    return None

def _getInsertId(cur):
    cur.execute("SELECT @@IDENTITY AS id")
    result = cur.fetchall()
    return result[0][0]

def insert_one(conn, sql_param):
    '''
    通过给定sql语句插入数据，并返回该数据的id
    @param conn: 数据库连接对象
    @param sql_param: 包含SQL语句和param的元组
    @return: 字典数组
    '''
    cur = None
    try:
        cur = conn.cursor()
        cur.execute(sql_param[0], sql_param[1])
        conn.commit()
        return _getInsertId(cur)
    except Exception, e: 
        raise DatabaseError(u'数据库错误', 'insert_one！'+str(e))
    finally:
        if cur:
            cur.close()

def mysqldatetime2datetime(datetime, logger):#with seconds
    try:
        return datetime.strftime('%Y-%m-%d %H:%M:%S') 
    except Exception ,e:
        if not logger:
            logger = getLogger('baseservice.sysexcept')
        logger.warning(u'数据库时间格式化异常%s'%(e, ))
        return '0000-00-00 00:00:00'

def covert_none_2_zero(o):
    if o is None:
        return 0
    else:
        return o
    
if __name__ == '__main__':
    c = open_conn()
