def detailPageInfo(detailPageURL,positionID,html,jobname):
    from lxml import etree
    
    # 网站名称：
    dataList = ['拉勾']
    
    # 搜索关键词：
    dataList.append(jobname)
    
    # 搜索条件：
    dataList.append('https://www.lagou.com/jobs/list_'+ jobname +'?labelWords=&fromSearch=true&suginput=')
    
    # 职位ID：
    dataList.append(positionID)
    
    # 职位网址：
    dataList.append(detailPageURL)
    
    # 公司名称：
    response = html.xpath("//em[@class='fl-cn']/text()")
    dataList.append(response[0].strip())
    
    # 领域,发展阶段,投资机构,公司规模,公司网址
    response = html.xpath("//ul[@class='c_feature']//h4/text()")
    if len(response) < 5:
        response.insert(2,'NULL')
        dataList = dataList + response
    else:
        dataList = dataList + response
        
    # 职位名称
    response = html.xpath("//h1[@class='name']/text()")
    dataList.append(response[0].strip())
    
    # 标签列表
    response = html.xpath("//ul[@class='position-label clearfix']/li/text()")
    dataList.append(response)
    
    # 职位诱惑
    response = html.xpath("//dd[@class='job-advantage']//p/text()")
    dataList.append(response)
    
    # 职位描述
    response = html.xpath("//div[@class='job-detail']//p/text()")
    dataList.append(response)
    
    # 薪资范围，经验要求，学历要求，工作地点，工作性质
    # string是不可变类型,所以这里一定要重新赋值
    def process(string):
        string = string.replace('/', '') 
        return string
    response = html.xpath("//dd[@class='job_request']//span/text")
    response = list(map(process,result))
    dataList = dataList + response
    
    # 工作地址1，2，3，查看地图
    response  = html.xpath("//body/div[@id='container']/div[@class='content_l fl']/dl[@id='job_detail']/dd[@class='job-address clearfix']/div[1]//a/text()")
    if len(response) == 4:
        response.insert(1,'NULL')
        dataList = dataList + response
    else:
        dataList = dataList + response
        
    # 发布日期
    response = html.xpath("//p[@class='publish_time']/text()")
    response = response[0].replace('\xa0','')
    dataList.append(response)
    
    return dataList