'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-05-13 11:02:01
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-05-14 12:25:04
FilePath: \llm-ag-farmer\src\simple_demo\st_demo.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_core.messages.human import HumanMessage
from langchain_core.messages.system import SystemMessage
import os
import yaml
import streamlit as st

st.title("Hydroponic Farming Assistant")

def init_chat_history() -> ChatPromptTemplate:
    if 'chat_history' not in st.session_state:
        template = ChatPromptTemplate.from_messages([
            ('system', "You are an Agricultural Specialist assisting a user in developing a planting schedule for their hydroponic farm."),
        ])
        st.session_state['chat_history'] = template
    else:
        template = st.session_state['chat_history']
    return template

chat_tmp = init_chat_history()
llm = ChatOllama(model="llama2")
user_input = st.chat_input("Say something")
chain = chat_tmp | llm | StrOutputParser()

if user_input:
    with st.status("Thinking..."):
        chat_tmp.append(HumanMessage(user_input))
        response = chain.invoke({})
        chat_tmp.append(AIMessage(response))
        st.session_state['chat_history'] = chat_tmp

for message in st.session_state['chat_history'].messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)
    