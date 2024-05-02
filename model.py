import pandas as pd
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env
import os
import google.generativeai as genai
# Set your Google Cloud Generative AI API key (replace with your actual key)
API_KEY = os.getenv("GOOGLE_API_KEY")

# Check for API key availability
if not API_KEY:
    print("Error: Please set your Google Cloud Generative AI API key in the .env file.")
    exit(1)

# Initialize Generative AI with your API key
genai.configure(api_key=API_KEY)


## Function to load model and generate responses

def generate_text_completion(news_title):
    # Simplify and format the prompt
    prompt = f"""Analyze the news title: "{news_title}" and determine:
                * Category (politics, social, or other)
                * Sentiment (positive, negative, or neutral)
                """

    model = genai.GenerativeModel('gemini-pro')
    try:
        response = model.generate_content([news_title, prompt])
        return response.text
    except Exception as e:
        print(f"Error generating text completion: {e}")
        return None


df = pd.read_csv("top_news.csv")

data = []
for index, row in df.iterrows():
    news_title = row[0]
    domain = generate_text_completion(news_title)
    if domain:
        data.append((news_title, domain))

df1 = pd.DataFrame(data, columns=['News Title', 'Domain'])
df1.to_csv("domain_sentiment.csv")
