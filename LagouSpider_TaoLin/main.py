def main():
    failList = []
    jobname  = input("请输入您要搜索的关键词")
    for row in listPageSpider(jobname):
        idList = row['content']['positionResult']['result']
        for id in idList:
            try:
                time.sleep(1)
                content = detailPageSpider(id['positionId'],jobname,failList)
            except:
                continue
            if content != []:
                with open('./data.csv', 'a', encoding='utf-8-sig') as f:
                    writer = csv.writer(f)
                    writer.writerow(content)
    
    # 对failList中的id进行爬取
    if failList != []:
        for id in failList:
            try:
                time.sleep(1)
                
                content = detailPageSpider(id,jobname,failList)
            except:
                continue
            if content != []:
                with open('./data.csv', 'a', encoding='utf-8-sig') as f:
                    writer = csv.writer(f)
                    writer.writerow(content)
                