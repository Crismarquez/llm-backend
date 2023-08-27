import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import openai
from langchain import SQLDatabase

from assistant.approach import Approach
from assistant.sqlagents import SQLAssistant, SQLGenerator
from schemas.conversation import WppConversation
from config.database import engine
from config.config import ENV_VARIABLES

app = FastAPI()
app.title = "LLM API"
app.version = "0.0.1"

openai.api_key = ENV_VARIABLES["OPENAI_API_KEY"]

personal_copilot = Approach(chatgpt_deployment = "gpt-3.5-turbo")
sql_assistant = SQLAssistant(gpt_deployment = "gpt-3.5-turbo")
sql_generator = SQLGenerator(gpt_deployment = "gpt-4")


@app.get("/")
async def root():
    return HTMLResponse('<h1>Your LLM API is running</h1>')

@app.post("/wppcopilot")
async def copilot(conversation: WppConversation):
    number = conversation.celphone
    # TODO: get name  user according to celphone
    # name = ""
    response = personal_copilot.run(conversation.history)
    return response

@app.post("/sqlchatbot")
async def sqlchatbot(conversation: WppConversation):
    db = SQLDatabase(engine)
    response = sql_assistant.run(conversation.history, db)
    return response

@app.post("/sqlgenerator")
async def sqlgenerator(conversation: WppConversation):
    response = sql_generator.run(conversation.history)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app:app', host="0.0.0.0", port=5000)