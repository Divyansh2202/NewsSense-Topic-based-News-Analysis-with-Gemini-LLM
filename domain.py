import pandas as pd
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import os

# Set your OpenAI API key
import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def generate_text_completion(input):
    input_prompt = """
              you will recive news title and from that news title 
              you have to tell weather it is political, scocial or
              any other and aslo provide thesentiment of that
              news title sentiment only
               """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input,input_prompt])
    return response.text

df = pd.read_csv("top_news.csv")

new = []
for index, row in df.iterrows():
  # Access the entire row as a string
  news_title = row[0]
  domain = generate_text_completion(news_title)
  new.append((news_title, domain))

df1 = pd.DataFrame(new, columns=['News Title', 'Domain'])
df1.to_csv("domain_sentiment.csv")