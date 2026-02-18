from langchain_ollama import ChatOllama
from tools import add_expense, get_monthly_expenses, get_monthly_total, delete_by_id
from langchain_core.tools import StructuredTool
from langchain_core.messages import HumanMessage, ToolMessage

llm = ChatOllama(model="llama3.1", temperature=0)

tools = [
    StructuredTool.from_function(add_expense),
    StructuredTool.from_function(get_monthly_expenses),
    StructuredTool.from_function(get_monthly_total),
    StructuredTool.from_function(delete_by_id),
]

model = llm.bind_tools(tools=tools)
