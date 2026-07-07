# DAILY TASK- WEEK 5- DAY 4
'''
✓ AI Agent = LLM + tools + reasoning loop
✓ LangChain: LLM + Tool + initialize_agent
✓ ReAct pattern (Reasoning + Acting)
✓ Tool 1: get_employee_count(dept) → DB query
✓ Tool 2: get_avg_salary(dept) → DB query'''

from fastapi import FastAPI
from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from .schemas import QuestionRequest
from .tools import get_emp_count
from .tools import get_avg_salary

load_dotenv()

app = FastAPI()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

tools = [get_emp_count, get_avg_salary]
agent = create_react_agent(model=llm,tools=tools)

@app.get("/")
def home():
    return {"message": "LangChain Agent with Gemini"}

@app.post("/ai/ask")
async def ask(data: QuestionRequest):
    response = agent.invoke({"messages": [{"role": "user","content": data.question}]})
    answer = response["messages"][-1].content
    return {
        "question": data.question,
        "answer": answer
    }