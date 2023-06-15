# AI Tool Finder

#### Description:
This is full-stack web application built with Python, Flask, and MongoDB Atlas along with HTML (with the help of Bootstrap) and CSS as markup languages. This app allows you to look up AI Tools in a [publicly available dataset](https://www.kaggle.com/datasets/shahriarrahman009/futureidea-ai-tools-dataset) loaded to Atlas. 

#### Dependencies
* The web program is written in Python 3 with the Flask framework.
* Some code depends on the Flask library:
    * app.py
    * helpers.py
* Some code depends on the requests library:
    * app.py
    * helpers.py
* Some code depends on Python re library:
    * app.py
* Some code depends on the Python date library:
    * app.py
* Some code depends on the pymongo library:
    * app.py
    * helpers.py
* HTML and CSS are used as markup langauges.

Create a virtual environment for your code with: python -m venv .venv; ./.venv/bin/activate; pip install -r requirements.txt; python app.py

#### Files

#### HTML and CSS Files

| File | Description|
| --- | --- |
|main.css| This file includes the basic styling for classes used across different html files. 
|ai_tool_name.html| Displays a form for the user to submit a U.S. ai_tool_name and pricing and get statistics on UFO sightings in the area as well as the 10 most recent sightings in the database. |
|error.html| Displays a message to the user if they have input information in an incorrect format (with special characters in a ai_tool_name name, for example). |
|layout.html| An html template page that is used throughout the other html pages with Jinja. Provides the content for the navbar. |
|results.html| Based on the ai_tool_name and pricing submitted by the user in ai_tool_name.html, this page displays the total number of UFO sightings in that pricing and in that ai_tool_name as well as a list of the UFO sightings available. |


#### Python Files

| File | Description|
| --- | --- |
|app.py| This file connects to the MongoDB Atlas database and contains two functions. The ai_tool_name() function handles both GET and POST requests. A GET request to this function displays the tool_search.html page and allows the user to enter their category and pricing via a form. A POST request takes the information submitted by the user and then calls other functions to get the AI Tools in that pricing and category, the number of AI Tools in that category and that pricing, and a list of the AI Toolsavailable in the database. |
|helpers.py| This file connects to the MongoDB Atlas database and contains two helper functions. One counts the number of AI Tools for the category and pricing submitted by the user using the MongoDB Query API. The other looks up documents for AI Tools for that category and pricing, also using MongoDB Query API syntax. |
