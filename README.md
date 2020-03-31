This project will check the author, price and price of amazon books using python scrapy lib:
https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011

Example run:

(venv) vicdongs-MacBook-Pro:spider vicdong$ **scrapy crawl amazon**

[...debug msg...]

2020-03-27 20:21:52 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011> (referer: None)
2020-03-27 20:21:52 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011>


{'**author**': [Glennon Doyle and Glennon Doyle Melton,
              Hilary Mantel,
              Wizards RPG Team,
              Matthew Mercer,
              Rebecca Serle,
              Carrie Underwood,
              Harlan Coben,
              Steven Weber,
              et al,
              Katherine Schwarzenegger Pratt,
              Sarah J. Maas,
              Tui T. Sutherland,
              Anne Glenconner,
              Andy Greene,
              Charlie Kirk,
              Kate Elizabeth Russell,
              C. J. Box,
              Louise Erdrich]}
												
												
 '**price**': ['16',
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
           '14'],**
											
											
 '**title**': ['Untamed',
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
           'The Night Watchman']}**
