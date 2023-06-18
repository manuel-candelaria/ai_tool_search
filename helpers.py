import requests

from flask import redirect, render_template, request
from pymongo import MongoClient

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB connection string from the environment variable
mongodb_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongodb_uri)

def get_count(pricing, category):
    """Count the AI Tools for that category and pricing"""

    ai_tool_name_count = client['aitools']['aitools'].aggregate([
        {
            "$match": {
                "$and": [
                    {"categories": {"$regex": category, "$options": "i"}},
                    {"pricing": pricing}
                ]
            }
        }, 
        {
            "$group": {
                "_id": None,
                "aitool_count": {"$sum": 1}
            }
        }
    ])

    result = list(ai_tool_name_count)
    
    if len(result) > 0:
        count = result[0]['aitool_count']
    else:
        print("No matching documents found.")

    return ai_tool_name_count

def get_aitools(pricing, category):
    """Gets report of AI Tools for that category and pricing"""

    recent_aitools = client['aitools']['aitools'].aggregate([
        {
            "$match": {
                "$and": [
                    {"categories": {"$regex": category, "$options": "i"}},
                    {"pricing": pricing}
                ]
            }
        }
    ])
    return recent_aitools

def get_count_byname(name_or_usage):
    """Count the AI Tools for that category and pricing"""

    byname_count = client['aitools']['aitools'].aggregate([
        {
            "$match": {
                "$or": [
                    {
                        "ai_tool_name": {
                            "$regex": name_or_usage, 
                            "$options": "i"
                        }
                    }, {
                        "types_of_use": {
                            "$regex": name_or_usage, 
                            "$options": "i"
                        }
                    }
                ]
            }    
        }, 
        {
            "$group": {
                "_id": None,
                "aitool_count": {"$sum": 1}
            }
        }
    ])
    
    result = list(byname_count)
    
    if len(result) > 0:
        count = result[0]['aitool_count']
        print("Number of matching documents:", count)
    else:
        print("No matching documents found.")

    return byname_count

def get_tools_byname(name_or_usage):
    """Gets report of AI Tools by matching on Name or Type of Usage"""
    aitools = client['aitools']['aitools'].aggregate([
        {
            "$match": {
                "$or": [
                    {
                        "ai_tool_name": {
                            "$regex": name_or_usage, 
                            "$options": "i"
                        }
                    }, {
                        "types_of_use": {
                            "$regex": name_or_usage, 
                            "$options": "i"
                        }
                    }
                ]
            }    
        }

    ])
    return aitools

count=get_count_byname("podcast")
object= get_tools_byname("podcast")
print("Count,", count)
print("result", object )

