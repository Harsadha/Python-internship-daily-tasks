import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from .tools import (
    get_employee_count,
    get_average_salary,
    list_departments
)

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

tools = [
    get_employee_count,
    get_average_salary,
    list_departments
]

agent = create_react_agent(
    model=llm,
    tools=tools
)

def ask_hr_agent(question: str):
    response = agent.invoke({"messages": [{"role": "user","content": question}]})
    return response["messages"][-1].content