import os
from typing import Union
import openai
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
apiKey = os.getenv("OPENAI_API_KEY")

@app.get("/chatgpt")
def apiModel(questiontoGpt):
    openai.api_key = apiKey
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": questiontoGpt},
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    print(result)
    return response


