import streamlit as st
from langchain_core.messages import HumanMessage, ToolMessage
from agent import model
from tools import add_expense, get_monthly_expenses, delete_by_id

st.set_page_config(page_title="AI Expense Tracker")
st.title("💰 AI Expense Tracker")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Enter your expense or ask for report...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to model
    response = model.invoke([HumanMessage(content=user_input)])

    final_output = ""

    if response.tool_calls:
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            if tool_name == "add_expense":
                result = add_expense(**tool_args)

            elif tool_name == "get_monthly_expenses":
                result = get_monthly_expenses(**tool_args)

            elif tool_name == "delete_by_id":
                result = delete_by_id(**tool_args)

            tool_message = ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )

            final_response = model.invoke(
                [HumanMessage(content=user_input), response, tool_message]
            )

            final_output = final_response.content

    else:
        final_output = response.content

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": final_output})
    with st.chat_message("assistant"):
        st.markdown(final_output)
