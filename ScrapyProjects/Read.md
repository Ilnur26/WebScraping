Creating a Scrapy Project

1. pip install scrapy                                # install scrapy module
2. [python -m] scrapy startproject {ProjectName}     # specify particular python version if needed
3. cd {ProjectName}                                  # move to directory



/*************
1. Create Directory {ProjectName}

2. Push scrapy.cfg file on the same level with such text:
    [settings]
    {ProjectName} = {ProjectName}.settings

    [deploy]
    project = {ProjectName}

3. Execute this in Terminal:
  $ scrapy startproject {ProjectName}

  It will generate directory {ProjectName} with needed files and spiders directory 

4. Push *.py file which contains description of Scraping Class of type "scrapy.Spider" with attribute name = {name}
  This class must have "parse" method

5. Call from Terminal to record scraped data to csv-file:
  $ python -m scrapy crawl {name} -o *.csv
*********************/
