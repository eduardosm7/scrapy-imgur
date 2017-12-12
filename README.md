# scrapy-imgur
Using Python's Scrapy to scrape images from imgur.com

 * [Scrapy](https://scrapy.org/)
 * [Imgur](https://imgur.com)
 
# Setup

 * `pip install Scrapy`

# Works like the following
 - There is a `scrapy_integrate.py` file, with a `search_image` function implemented.
 - Call this funtion passing the search string
 - It will run a terminal command that will scrape imgur.com
 - The first thumbnail image resulting from the search will be downloaded
 - Then the `search_image` function will return the name of the file stored at /images/full
 
