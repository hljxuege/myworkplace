#encoding:utf-8
'''
Created on Nov 4, 2013

@author: liuxue
'''
'''
上传流程

在七牛云存储中，整个上传流程大体分为这样几步：

业务服务器颁发 uptoken（上传授权凭证）给客户端（终端用户）
客户端凭借 uptoken 上传文件到七牛
在七牛获得完整数据后，发起一个 HTTP 请求回调到业务服务器
业务服务器保存相关信息，并返回一些信息给七牛
七牛原封不动地将这些信息转发给客户端（终端用户）
'''
import qiniu.conf
import qiniu.rs
import sys
qiniu.conf.ACCESS_KEY = "5vnrmvpnIqY-q7gTKsd-Pdw12jDcCaYUYbmpzqEh"
qiniu.conf.SECRET_KEY = "QmfYBTeRr9UWnxk-8RJbsFD98lB0ZR_mdQHekFWM"
def get_uptoken():
    policy = qiniu.rs.PutPolicy('wm-test')
    policy.callbackUrl='http://180.78.111.112:8008/app'
    policy.callbackBody='name=$(fname)&hash=$(etag)&location=$(x:location)&=$(x:prise)'
    uptoken = policy.token()

    return uptoken

def get_dnurl(key):
    base_url = qiniu.rs.make_base_url('wm-test.u.qiniudn.com', key)
    policy = qiniu.rs.GetPolicy()
    private_url = policy.make_request(base_url)
    
    return private_url

def upload_pic(uptoken, key, filename):
    import qiniu.io
    
    ret, err = qiniu.io.put_file(uptoken, key, filename)
    if err is not None:
        sys.stderr.write('error: %s ' % err)
    return
if __name__ == '__main__':
    u_t = get_uptoken()
    key = '1.jpg'
    print upload_pic(u_t, key, '/home/liuxue/Downloads/mahua-logo.jpg')
    print get_dnurl(key)