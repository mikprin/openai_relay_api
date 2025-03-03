from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import openai
from openai import AsyncOpenAI
import asyncio
import anthropic


# Load environment variables from the .env file
load_dotenv()

# Get OpenAI API key and port from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
PORT = int(os.getenv("PORT", 8000))


class OpenAIClient:
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)

    async def create_chat_completion(
        self, messages: list[dict[str, str]], model: str
    ) -> str:
        try:
            chat = await self.client.chat.completions.create(messages=messages, model=model)
            return chat.choices[0].message.content
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# # Define OpenAI Client class
# class OpenAIClient:
#     def __init__(self, api_key: str):
#         openai.api_key = api_key

#     async def create_chat_completion(self, messages: list[dict[str, str]], model: str):
#         try:
#             # Make async OpenAI request for chat completion
#             response = await asyncio.to_thread(
#                 openai.ChatCompletion.create, model=model, messages=messages
#             )
#             return response.choices[0].message['content']
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=str(e))

# Input model for request body
class OpenAIRequest(BaseModel):
    """Version 1"""
    model_name: str
    messages: list[dict[str, str]]


class ClaudeRequest(BaseModel):
    """Version 1"""
    model_name: str
    messages: list[dict[str, str]]
    max_tokens: int = 1000
    temperature: float = 0.2

# FastAPI instance
app = FastAPI()

# Dependency to verify authorization token
def verify_token(request: Request):
    token = request.headers.get("Authorization")
    if token != AUTH_TOKEN:
        raise HTTPException(status_code=403, detail="Unauthorized")

# Route to handle OpenAI requests
@app.post("/api/open_ai_request")
async def open_ai_request(
    openai_request: OpenAIRequest, token: None = Depends(verify_token)
):
    client = OpenAIClient(api_key=OPENAI_API_KEY)
    result = await client.create_chat_completion(
        messages=openai_request.messages, model=openai_request.model_name
    )
    return {"response": result}


# Route to handle Claude requests
@app.post("/api/claude_request")
async def claude_request(
    claud_request: ClaudeRequest, token: None = Depends(verify_token)
):
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        message = client.messages.create(
            messages=claud_request.messages,
            model=claud_request.model_name,
            max_tokens=claud_request.max_tokens,
            temperature=claud_request.temperature,
        )
        return {"response": message.content[0].text}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))



# To run the app, add this if you are running manually
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)

