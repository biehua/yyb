from scrapy import cmdline

# cmdline.execute(['scrapy', 'crawl', 'yyb_spider'])
cmdline.execute("scrapy crawl yyb_spider -o info.csv -t csv".split())