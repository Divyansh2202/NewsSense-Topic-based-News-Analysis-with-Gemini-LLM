import requests
from bs4 import BeautifulSoup
import csv

def fetch_news_for_topic(topic):
    url = f'https://news.google.com/rss/search?q={topic}&hl=en-US&gl=US&ceid=US:en'
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'xml')
        items = soup.find_all('item')[:10]  # Limit to top 10 news
        
        news_list = []
        for item in items:
            title = item.title.text
            news_list.append([title])

        return news_list
    except Exception as e:
        print("An error occurred:", str(e))
        return []

def save_to_csv(news_list, filename):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(news_list)

if __name__ == "__main__":
    num_topics = int(input("Enter the number of topics you want to search: "))
    topics = []
    for i in range(num_topics):
        topics.append(input(f"Enter topic {i+1}: "))
    
    filename = "top_news.csv"
    for topic in topics:
        news_list = fetch_news_for_topic(topic)
        if news_list:
            save_to_csv(news_list, filename)
            print(f"Top 10 news articles on '{topic}' have been saved to '{filename}'.")
        else:
            print(f"No news articles found for the topic '{topic}'.")
