import scrapy
from scrapy import Request 
from scrapy.loader import ItemLoader
from image_downloader.items import ImageDownloaderItem
import chompjs
from math import ceil

class WikiartSpider(scrapy.Spider):
    """Scrapy spider for scraping minimalism painting images from WikiArt.org
    
    This spider navigates through paginated results of minimalism paintings and
    extracts high-quality image URLs. Features include:
    - Automatic pagination handling
    - JSON-based image URL extraction
    - Batch processing of 60 items per page
    - Integration with Scrapy's media pipeline for image downloads
    
    Note: Requires proper configuration of Scrapy's IMAGES_STORE setting
    """
    
    name = 'wikiart'
    allowed_domains = ['wikiart.org']
    start_urls = ['https://www.wikiart.org/en/paintings-by-style/minimalism?select=featured#!#filterName:featured,viewType:masonry']

    def __init__(self):
        """Initialize the spider with paginated URL template"""
        self.url_template = 'https://www.wikiart.org/en/paintings-by-style/minimalism?select=featured&json=2&layout=new&page={}&resultType=masonry'

    def parse(self, response):
        """Parse initial page and generate pagination requests
        
        Args:
            response (scrapy.http.Response): Response object from start URL
            
        Yields:
            scrapy.Request: Paginated API requests for painting data
        """
        initial_data = response.xpath('//div[@class="artworks-by-dictionary"]/@ng-init').get()
        data_object = chompjs.parse_js_object(initial_data, json_params={'strict': False})
        total_images = data_object['initialPortion']['itemsCount']
        for page_id in range(1, self.get_total_pages(total_images) + 1):
            yield Request(
                self.url_template.format(page_id),
                callback=self.parse_images,
                dont_filter=True
            )
    
    def parse_images(self, response):
        """Process paginated JSON response and extract image URLs
        
        Args:
            response (scrapy.http.Response): Response containing painting JSON data
            
        Yields:
            ImageDownloaderItem: Items with collected image URLs
        """
        loader = ItemLoader(ImageDownloaderItem(), response)
        loader.add_value('image_urls', [painting['image'] for painting in response.json()["Paintings"]])
        yield loader.load_item()

    def get_total_pages(self, total_images: int) -> int:
        """Calculate total number of paginated pages
        
        Args:
            total_images (int): Total number of paintings available
            
        Returns:
            int: Number of pages needed to display all results (60 items per page)
        """
        return ceil(total_images / 60)