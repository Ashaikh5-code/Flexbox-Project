import time
from flask import Flask, render_template
from firecrawl import FirecrawlApp

app = Flask(__name__)

# Function to initiate crawl job with retry mechanism
def crawl_with_retry(url, max_retries=3, retry_interval=10):
    # Initialize FirecrawlApp
    firecrawl_app = FirecrawlApp(api_key='fc-bae3fab0078c4bde93eaa6fb9bc44571')
    
    # Counter for retry attempts
    retry_count = 0
    
    # Flag to track whether the crawl job is successful
    crawl_successful = False
    
    # Retry loop
    while retry_count < max_retries:
        try:
            # Attempt to crawl the URL
            response = firecrawl_app.crawl_url(url)
            
            # Check if the crawl job is successful
            if response.get('status') == 'success':
                crawl_successful = True
                break
            else:
                # Increment retry count
                retry_count += 1
                print(f"Crawl attempt {retry_count} failed. Retrying in {retry_interval} seconds...")
                time.sleep(retry_interval)
        except Exception as e:
            # Increment retry count
            retry_count += 1
            print(f"Error occurred during crawl attempt {retry_count}: {e}")
            print(f"Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
    
    # Return crawl response
    return response if crawl_successful else None

# Route for homepage
@app.route('/')
def index():
    # Define the URL to crawl
    url = 'https://www.legalbluebook.com/bluebook/v21/quick-style-guide'
    
    # Initiate crawl job with retry mechanism
    response = crawl_with_retry(url)
    
    # Extract the scraped data from the response
    if isinstance(response, list):
        # If response is a list, concatenate data from all items
        data = {}
        for item in response:
            data.update(item.get('data', {}))
    else:
        # If response is a dictionary, extract data directly
        data = response.get('data', {})
    
    # Render the template with scraped data
    return render_template('index.html', data=data)


# Run Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
    # Route for homepage
@app.route('/')
def index():
    # Define the URL to crawl
    url = 'https://www.legalbluebook.com/bluebook/v21/quick-style-guide'
    
    # Initiate crawl job with retry mechanism
    response = crawl_with_retry(url)
    
    # Check if the response is None
    if response is None:
        # Handle case where crawl job failed
        error_message = "Error: Crawl job failed or was stopped."
        return render_template('error.html', error_message=error_message)
    
    # Extract the scraped data from the response
    if isinstance(response, list):
        # If response is a list, concatenate data from all items
        data = {}
        for item in response:
            data.update(item.get('data', {}))
    else:
        # If response is a dictionary, extract data directly
        data = response.get('data', {})
    
    # Render the template with scraped data
    return render_template('index.html', data=data)