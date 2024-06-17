from flask import Flask, render_template
from firecrawl import FirecrawlApp

app = Flask(__name__)

# Scrape data using Firecrawl
firecrawl_app = FirecrawlApp(api_key='fc-bae3fab0078c4bde93eaa6fb9bc44571')
response = firecrawl_app.crawl_url('https://www.legalbluebook.com/bluebook/v21/quick-style-guide')

# Extract the scraped data from the response
data = response.get('data', {})

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)