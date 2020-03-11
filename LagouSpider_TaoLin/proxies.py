# -*- coding:utf-8 -*-
# 设置代理，使用代理为：西瓜代理
def obtainProxy():
    import requests
    
    # 设置header
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    referer    = "http://www.xiguadaili.com/"
    headers    = {"user-agent": user_agent, "referer": referer}
    
    # 代理地址：
    target     = "http://api3.xiguadaili.com/ip/?tid=555136895430776&num=1000&protocol=https"
    
    # 对地址发出请求，获取1000个IP，HTTP格式
    r          = requests.get(target, headers=headers)
    ipText     = r.text
    
    # 对获取到的文本进行处理，分割单个IP
    proxy      = ipText.split('\r\n')
    proxies    = {}
    for rowIP in proxy:
        proxies = {
            'http':'http://' + rowIP,
            'https':'https://' + rowIP
        }
        
    return proxies