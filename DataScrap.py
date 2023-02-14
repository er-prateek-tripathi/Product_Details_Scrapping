import requests
from bs4 import BeautifulSoup

# Define the search query entered by the user
search_query = "iphone 12"

# Define the URL for Amazon
amazon_url = f"https://www.amazon.in/s?field-keywords={search_query}"

# Define the URL for Flipkart
flipkart_url = f"https://www.flipkart.com/search?q={search_query}"

# Send an HTTP request to Amazon and retrieve the HTML content
amazon_response = requests.get(amazon_url)
amazon_content = amazon_response.content

# Send an HTTP request to Flipkart and retrieve the HTML content
flipkart_response = requests.get(flipkart_url)
flipkart_content = flipkart_response.content

# Create a BeautifulSoup object for Amazon
amazon_soup = BeautifulSoup(amazon_content, "html.parser")

# Create a BeautifulSoup object for Flipkart
flipkart_soup = BeautifulSoup(flipkart_content, "html.parser")

# Extract the product information from Amazon
amazon_products = []
amazon_product_containers = amazon_soup.find_all("div", class_="s-result-item")
for container in amazon_product_containers:
    product = {"name": container.find("span", class_="a-size-medium").text,
               "price": container.find("span", class_="a-offscreen").text,
               "url": container.find("a", class_="a-link-normal")["href"]}
    amazon_products.append(product)

# Extract the product information from Flipkart
flipkart_products = []
flipkart_product_containers = flipkart_soup.find_all("div", class_="_3O0U0u")
for container in flipkart_product_containers:
    product = {"name": container.find("div", class_="_3wU53n").text,
               "price": container.find("div", class_="_1vC4OE_2rQ-NK").text,
               "url": container.find("a", class_="_31qSD5")["href"]}
    flipkart_products.append(product)

# Print the extracted product information for Amazon
print("Amazon products:")
for product in amazon_products:
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"URL: {product['url']}")
    print("---")

# Print the extracted product information for Flipkart
print("Flipkart products:")
for product in flipkart_products:
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"URL: {product['url']}")
    print("---")
