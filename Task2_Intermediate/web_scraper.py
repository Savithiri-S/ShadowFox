import os
import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Display response status
print("Status Code:", response.status_code)

if response.status_code == 200:

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quotes and authors
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    print("Quotes found:", len(quotes))
    print("Authors found:", len(authors))
    print("\n===== Quotes Scraped Successfully =====\n")

    # Create the file path inside Task2_Intermediate
    file_path = os.path.join(os.path.dirname(__file__), "quotes.txt")

    # Open the file for writing
    with open(file_path, "w", encoding="utf-8") as file:

        # Loop through quotes and authors
        for i, (quote, author) in enumerate(zip(quotes, authors), start=1):

            # Display in terminal
            print(f"{i}. {quote.text}")
            print(f"   — {author.text}")
            print()

            # Save to file
            file.write(f"{i}. {quote.text}\n")
            file.write(f"   — {author.text}\n\n")

    print(f"Quotes saved successfully in:\n{file_path}")

else:
    print("Failed to retrieve the webpage.")