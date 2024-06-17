# Install with pip install firecrawl-py
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key='fc-bae3fab0078c4bde93eaa6fb9bc44571')
response = app.crawl_url('https://www.legalbluebook.com/bluebook/v21/quick-style-guide')
print(response)