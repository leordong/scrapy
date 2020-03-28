# scrapy

Example run:
(venv) vicdongs-MacBook-Pro:spider vicdong$ scrapy crawl amazon
2020-03-27 20:21:50 [scrapy.utils.log] INFO: Scrapy 2.0.1 started (bot: spider)
2020-03-27 20:21:50 [scrapy.utils.log] INFO: Versions: lxml 4.5.0.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.5.2, w3lib 1.21.0, Twisted 20.3.0, Python 3.7.5 (default, Nov  1 2019, 02:16:32) - [Clang 11.0.0 (clang-1100.0.33.8)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Darwin-19.3.0-x86_64-i386-64bit
2020-03-27 20:21:50 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2020-03-27 20:21:50 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'spider',
 'NEWSPIDER_MODULE': 'spider.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['spider.spiders']}
2020-03-27 20:21:50 [scrapy.extensions.telnet] INFO: Telnet Password: d1cf7539a5399b66
2020-03-27 20:21:50 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2020-03-27 20:21:50 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-03-27 20:21:50 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-03-27 20:21:50 [scrapy.middleware] INFO: Enabled item pipelines:
['spider.pipelines.SpiderPipeline']
2020-03-27 20:21:50 [scrapy.core.engine] INFO: Spider opened
2020-03-27 20:21:50 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-03-27 20:21:50 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-03-27 20:21:51 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.com/robots.txt> (referer: None)
2020-03-27 20:21:51 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011> from <GET https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1585354544&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0>
2020-03-27 20:21:52 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011> (referer: None)
2020-03-27 20:21:52 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011>
{'author': ['\n'
            '    \n'
            '        \n'
            '        \n'
            '            Glennon Doyle\n'
            '        \n'
            '    \n',
            ' and ',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Glennon Doyle Melton\n'
            '        \n'
            '    \n',
            'A high quality digital reading experience.',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Hilary Mantel\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Wizards RPG Team\n'
            '        \n'
            '    \n',
            ' and ',
            'Matthew Mercer',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Rebecca Serle\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Carrie Underwood\n'
            '        \n'
            '    \n',
            'Harlan Coben',
            ', ',
            'Steven Weber',
            ', et al.',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Katherine Schwarzenegger Pratt\n'
            '        \n'
            '    \n',
            'A high quality digital reading experience.',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Sarah J. Maas\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Tui T. Sutherland\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Anne Glenconner\n'
            '        \n'
            '    \n',
            'A high quality digital reading experience.',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Andy Greene\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Charlie Kirk\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Kate Elizabeth Russell\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            C. J. Box\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Lily King\n'
            '        \n'
            '    \n',
            '\n'
            '    \n'
            '        \n'
            '        \n'
            '            Louise Erdrich\n'
            '        \n'
            '    \n'],
 'price': ['16',
           '18',
           '29',
           '12',
           '17',
           '0',
           '13',
           '13',
           '12',
           '18',
           '17',
           '18',
           '14',
           '14',
           '12',
           '14'],
 'title': ['Untamed',
           'The Mirror & the Light (Wolf Hall Trilogy)',
           "Explorer's Guide to Wildemount (D&D Campaign Setting and Adventure "
           'Book) (Dungeons & Dragons)',
           'In Five Years: A Novel',
           'Find Your Path: Honor Your Body, Fuel Your Soul, and Get Strong '
           'with the Fit52 Life',
           'The Boy from the Woods',
           'The Gift of Forgiveness: Inspiring Stories from Those Who Have '
           'Overcome the Unforgivable',
           'House of Earth and Blood (Crescent City Book 1)',
           'Dragonslayer (Wings of Fire: Legends)',
           'Lady in Waiting: My Extraordinary Life in the Shadow of the Crown',
           'The Office: The Untold Story of the Greatest Sitcom of the 2000s: '
           'An Oral History',
           'The MAGA Doctrine: The Only Ideas That Will Win the Future',
           'My Dark Vanessa: A Novel',
           'Long Range (A Joe Pickett Novel Book 20)',
           'Writers & Lovers: A Novel',
           'The Night Watchman']}
2020-03-27 20:21:52 [scrapy.core.engine] INFO: Closing spider (finished)
2020-03-27 20:21:52 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 871,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 77370,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/301': 1,
 'elapsed_time_seconds': 1.766373,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 3, 28, 1, 21, 52, 676887),
 'item_scraped_count': 1,
 'log_count/DEBUG': 4,
 'log_count/INFO': 10,
 'memusage/max': 52809728,
 'memusage/startup': 52809728,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 3, 28, 1, 21, 50, 910514)}
2020-03-27 20:21:52 [scrapy.core.engine] INFO: Spider closed (finished)
