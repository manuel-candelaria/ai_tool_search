import re
from datetime import date
import datetime

from flask import Flask, render_template, request
from pymongo import MongoClient
from helpers import get_count, get_aitools, get_count_byname, get_tools_byname

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB connection string from the environment variable
mongodb_uri = os.getenv("MONGODB_URI")

app = Flask(__name__)

client = MongoClient(mongodb_uri)
db = client['aitools']
aitools = db.aitools

# Declare arrays pricings and categories to use in later functions. In the future these should be generated automatically with 
# Values from the collection.
pricings = ["Freemium", "Free", "Free Trial", "Paid", "Deals", "Contact for Pricing"]
categories = ["3D", "art", "audio editing", "avatars", "code assistant", "copywriting", "customer support", "dating", "design assistant", "developer tools", "e-commerce", "education assistant", "email assistant", "experiments", "fashion", "finance", "fitness", "fun tools", "gaming", "general writing", "gift ideas", "healthcare", "human resources", "image editing", "image generator", "legal assistant", "life assistant", "logo generator", "low-code/no-code", "memory", "music", "paraphraser", "personalized videos", "presentations", "productivity", "prompts", "real estate", "religion", "research", "resources", "sales", "search engine", "SEO", "social media assistant", "spreadsheets", "SQL", "startup tools", "story teller", "summarizer", "text to speech", "transcriber", "travel", "video editing", "video generator"]

@app.route("/", methods=["GET", "POST"])
def ai_tool_name():

    # For GET Request: Let user submit ai_tool_name and pricing to look up matching records
    if request.method == "GET":

        return render_template("tool_search.html", pricings=pricings, categories=categories)

    # For POST Request: Return and display results
    # Get category and pricing from user
    pricing = request.form.get("pricing")
    category = request.form.get("category")
    name_or_usage = request.form.get("name_or_usage")

    # Define error message
    message = "Select a valid options for Category and Pricing Model"

    if name_or_usage == "":
        if pricing == None or category == None:
            return render_template("error.html", message=message)
        # Get number of matching tools in ai_tool_name and pricing as a list
        ai_tool_name_count = get_count(pricing, category)

        # Get a list of AI Tools matching the selected pricing and category
        recent_aitools = get_aitools(pricing, category)
        return render_template("results.html", ai_tool_name_count=ai_tool_name_count, recent_aitools=recent_aitools, pricing=pricing, category=category)
    
    else:
        ai_tool_name_count = get_count_byname(name_or_usage)
        print(ai_tool_name_count)

        recent_aitools = get_tools_byname(name_or_usage)
        print(recent_aitools)

        return render_template("results_byname.html",ai_tool_name_count=ai_tool_name_count, recent_aitools=recent_aitools, name_or_usage=name_or_usage)

if __name__ == "__main__":
    app.run()