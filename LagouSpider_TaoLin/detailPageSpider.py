def detailPageSpider(positionID,jobname,failList):
    detailPageURL = 'https://www.lagou.com/jobs/' + str(positionID) + '.html?show=087544dcf3cf440099dd69beffd236c3'
    headers = {
        'Host': "www.lagou.com",
        'Referer': 'https://www.lagou.com/jobs/'+ str(id) +'.html',
        'Sec-Fetch-Dest': "empty",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Site': "same-origin",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        }
    result = requests.get(detailPageURL,headers = headers, proxies = obtainProxy(),allow_redirects=False)
    data   = result.text
    html = etree.HTML(data)
    
    # 随机获取的IP可能会不好用，出现SSL报错
    try:
        htmlData = detailPageSpider(detailPageURL,positionID,html,jobname)
    
    # 将未爬取到的IP储存在failList中
    except:
        failList.append(id)
        return []
    return htmlData
    