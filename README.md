
# Web Crawler App

## Application Design

The web crawler project is responsible for scraping and extracting data from three websites where many types of tech products are sold.
Furthermore, the crawler leverages the scrapy pipeline and item processing to clean and transform the extracted data before storing it.

Due to the long time of extracting data,I limited the crawlers to only extracting information about phones.This long time is due to the fact that these sites have many products for sale .
Another fact is that on one of the 3 sites (vexio.ro) I received a ban on a webcrawler robot and I had to find a method to bypass the site's proxy.
![image](https://github.com/LiviuBana/web-crawler-app/assets/92376799/b42a2ff1-2808-4ef6-b94a-df9329819cfe)

The Web Crawler[1] consists of three spider classes : VexioCrawler , RombizCrawler and DwynCrawler.
Each spider class is responsible for crawling a specific web page and extracting relevant data. 
It manages the flow of URLs to be crawled and coordinates the other components.
The Downloader component is responsible for retrieving web pages by making HTTP requests. 
It handles downloading the HTML content and other associated resources. It also interacts with the network layer to send HTTP requests and receive the web page responses.
It handles headers, cookies, redirects, and other aspects of the HTTP protocol.
The Queue manages the list of URLs to be crawled.
It maintains a queue or priority queue of URLs and provides new URLs to the Fetcher component. 
The Parser component processes the downloaded web pages.
It extracts relevant data, such as links, text, images, and other metadata, from the HTML content.
The Database component is responsible for storing the crawled data after it has been processed.
The architecture allows for parallel processing, where multiple instances of the Downloader, Parser, and Data Store components can work simultaneously to increase the crawling speed.


