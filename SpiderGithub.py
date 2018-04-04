# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: SpiderGithub.py 
@time: 2018/04/04 
"""

import scrapy


class SpiderGithub(scrapy.Spider):

    name = 'SpiderGithub'

    @property
    def start_urls(self):
        url_template = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url_template.format(i) for i in range(1, 5))
        return urls

    def parse(self, response):
        for source in response.css('div#user-repositories-list li'):
            yield{
                # itemprop="name codeRepository"
                'name': source.css('a::text').re_first('\S+'),
                'update_time': source.css('relative-time::attr("datetime")').extract_first()
            }
