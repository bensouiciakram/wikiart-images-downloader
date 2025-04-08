# WikiArt Minimalism Paintings Scraper

A Scrapy spider that downloads high-quality images of minimalism paintings from WikiArt.org.

## 📦 Features
- Automated pagination handling
- Bulk image downloads
- JSON-based data extraction
- Organized image storage
- Auto-throttling for polite crawling

## ⚙️ Prerequisites
- Python 3.7+
- Scrapy 2.5+
- Pillow (for image processing)
- chompjs

## 🚀 Installation
1. Clone repository:
```bash
git clone https://github.com/yourusername/wikiart-scraper.git
cd wikiart-scraper
```
2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```

3.Install dependencies:
```bash
pip install -r requirements.txt
```
📸 Usage

Run the spider:
```bash
scrapy crawl wikiart
```
Downloaded images will be stored in:

```bash
/images/full/  # Full resolution images
```
🗂 Project Structure
```bash
wikiart-scraper/
├── scrapy.cfg
├── images/                  # Downloaded images (created automatically)
├── image_downloader/
│   ├── __init__.py
│   ├── items.py            # Item class definitions
│   ├── middlewares.py      # Spider middlewares
│   ├── pipelines.py        # Image processing pipeline
│   ├── settings.py         # Scrapy configuration
│   └── spiders/
│       └── wikiart.py      # Main spider implementation
```

⚙ Configuration (settings.py)

```bash
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = 'images'  # Image storage directory
ROBOTSTXT_OBEY = False   # Disable robots.txt compliance
AUTOTHROTTLE_ENABLED = True  # Enable auto-throttling
```
🌐 Spider Details (wikiart.py)

 * Targets: https://www.wikiart.org
 * Pagination: 60 items per page
 * Data extraction:
     * High-resolution image URLs
       






