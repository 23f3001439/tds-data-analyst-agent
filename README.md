# tds-data-analyst-agent
TDS Data Analyst Agent
This is a Data Analyst Agent API for the Tools in Data Science (TDS) project at IITM. It processes data analysis tasks via POST requests, handling web scraping and visualization tasks.
Setup

Clone the repo:git clone https://github.com/23f3001439/tds-data-analyst-agent.git


Install dependencies:pip install -r requirements.txt


Run the API:uvicorn main:app --host 0.0.0.0 --port 8000



API Endpoint

URL: https://tds-data-analyst-agent-23f3001439.onrender.com/api/
Method: POST
Body: Upload a question.txt file with task descriptions.
Response: JSON array with answers, including base64-encoded scatterplots.

Example Request
curl -X POST -F "file=@question.txt" https://tds-data-analyst-agent-23f3001439.onrender.com/api/

Deployment
Deployed on Render.com.
License
MIT License
