from tqdm import tqdm
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.ai import AIMessage
from langchain_core.messages.human import HumanMessage
import logging
import time
import os
import yaml
import streamlit as st
"""
功能:

在內部對話需要 langchain 與 streamlit 穿插

可以用2種方式問答:
json output parse
normal chat

需要有function call 來執行
以及對話時可以讀取json的output
function call:

1. planting schedule -> 存到db以及重複利用用途
2. status check -> 用來檢查狀態
3. troubleshooting -> 用來解決問題
4. harvest analysis -> 用來分析收成
5. education and training -> 用來教育


對話prompt也需要多種模式
planting schedule
Status Check
Troubleshooting
Harvest Analysis
Education and Training
"""
config = yaml.safe_load(open("./sec_config.yaml"))

llm = ChatGroq(api_key=config["api_token"]["groq"], model="llama3-70b-8192")

prompt_planting = ChatPromptTemplate.from_messages([
        ('system', "You are an Agricultural Specialist assisting a user in developing a planting schedule for their hydroponic farm."), 
    ])

prompt_status = ChatPromptTemplate.from_messages([('system', "You are an Agricultural Specialist. Provide a detailed report on the current status of the hydroponic systems.")])

prompt_troubleshooting = ChatPromptTemplate.from_messages([('system', "You are a Technical Specialist. Help the user diagnose and fix issues with their hydroponic system.")])

prompt_harvest = ChatPromptTemplate.from_messages([('system', "You are an Agricultural Analyst. Analyze the harvest data and provide insights on how to improve future yields.")])

prompt_education = ChatPromptTemplate.from_messages([('system', "You are an Educator in Hydroponic Farming. Provide a basic training session for new hydroponic farmers.")])

prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)