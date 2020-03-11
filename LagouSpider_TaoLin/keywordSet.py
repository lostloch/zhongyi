# -*- coding:utf-8 -*-

# 设置指定搜索关键词(keyword,city)的url地址
from urllib.parse import quote

currentSite = 'Lagou'
keyword     = input("请输入您要搜索的关键词")
city        = input("请输入您要搜索的城市")

# 设置开始页面的URL，即浏览器上的URL
# https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/p-city_0?px=default&gx=&isSchoolJob=1#filterBox
keywordStartURL = 'https://www.lagou.com/jobs/list_'+quote(keyword)+'/p-city_0?px=default&gx=&isSchoolJob=1#filterBox'

# 设置真正的URL，即储存职位信息的URL
# https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=1
keywordRealURL  = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city='+quote(city)+'&needAddtionalResult=false&isSchoolJob=1'