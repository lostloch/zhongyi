def obtainProxy():
    from urllib import request

    # 要访问的目标页面
    # targetUrl = "http://test.abuyun.com/"
    # targetUrl = "http://proxy.abuyun.com/switch-ip"
    # targetUrl = "http://proxy.abuyun.com/current-ip"

    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "HCP3C7O7VC10M27D"
    proxyPass = "9F1D8060D5770E94"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
        "user" : proxyUser,
        "pass" : proxyPass,
    }

    proxy = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }
    return proxy