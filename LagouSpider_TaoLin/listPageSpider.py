def listPageSpider(jobname):
    import requests
    import time
    import json
    from urllib.parse import quote
    
    currentSite = 'Lagou'
    # jobname     = input("请输入您要搜索的关键词")
    keyword     = quote(jobname)
    # city      = quote(input("请输入您要搜索的城市"))

    # 设置开始页面的URL，即浏览器上的URL
    # https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=
    keywordStartURL = 'https://www.lagou.com/jobs/list_'+ keyword +'?labelWords=&fromSearch=true&suginput='

    # 设置真正的URL，即储存职位信息的URL
    keywordRealURL  = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    
    # 设置headers，模拟浏览器
    first_header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        'Host': 'www.lagou.com',
        'Referer': keywordStartURL,
        'Sec-Fetch-Dest': "empty",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Site': "same-origin",
                        }
    headers = {
        'Host': "www.lagou.com",
        'Origin': "https://www.lagou.com",
        'Referer': keywordStartURL,
        'Sec-Fetch-Dest': "empty",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Site': "same-origin",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        'X-Anit-Forge-Code': "0",
        'X-Anit-Forge-Token': "None",
        'X-Requested-With': "XMLHttpRequest"
        }
    count = 0
    for pageNumber in range(1,400):
        # 第一页：
        # payload = "first=true^&pn=1^&kd=^%^E6^%^95^%^B0^%^E6^%^8D^%^AE^%^E5^%^88^%^86^%^E6^%^9E^%^90"
        # 第二页：
        # payload = "first=false^&pn=2^&kd=^%^E6^%^95^%^B0^%^E6^%^8D^%^AE^%^E5^%^88^%^86^%^E6^%^9E^%^90^&sid=f097614de68b4d6fbba99e597d490baa"
        # 第三页：
        # payload = "first=false^&pn=3^&kd=^%^E6^%^95^%^B0^%^E6^%^8D^%^AE^%^E5^%^88^%^86^%^E6^%^9E^%^90^&sid=f097614de68b4d6fbba99e597d490baa"

        if pageNumber == 1:
            data = {
                'first': True,
                'pn': pageNumber, 
                'kd': jobname
            }
        else:
            data = {
                'first': False, 
                'pn': pageNumber, 
                'kd': jobname
            }
        # 每发送10个POST请求就重新获取一个cookie
        if count % 10 ==0:
            # 请求cookie
            requestsSession = requests.Session()
            requestsSession.get(keywordStartURL,headers = first_header)
            cookie = requestsSession.cookies
            time.sleep(1)
            # 对真正储存信息的URL进行请求
            response = requestsSession.post(keywordRealURL, headers=headers, data = data,cookies = cookie) 
            count    = count+1
            time.sleep(1)
        else:
            time.sleep(1)
            # 对真正储存信息的URL进行请求
            response = requestsSession.post(keywordRealURL, headers=headers, data = data,cookies = cookie)
            count    = count+1
            time.sleep(1)
        yield response.json()