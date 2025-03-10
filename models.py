"""
Módulo Models - Router Agent Framework

Este módulo configura os diferentes modelos de linguagem utilizados pelos agentes.
Cada modelo é especializado em um tipo específico de tarefa:
- llm_router: Modelo para decisão de roteamento (Gemini)
- llm_code: Modelo especializado em geração de código (Claude)
- llm_thinking: Modelo para raciocínio complexo (Claude com tokens estendidos)
- llm_basic: Modelo para respostas simples (DeepSeek)
"""

from langchain_anthropic import ChatAnthropic
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

# Definição do modelo base Claude para tarefas complexas
model = "claude-3-7-sonnet-latest"

# Modelo Gemini otimizado para decisões rápidas de roteamento
llm_router= ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                  temperature=0)

# Modelo Claude especializado em geração de código
llm_code = ChatAnthropic(model=model, temperature=0.7)

# Modelo Claude configurado para raciocínio profundo com tokens estendidos
llm_thinking = init_chat_model(
    model=model,
    max_tokens=20000,
    thinking={
        "type": "enabled",
        "budget_tokens": 16000
    })

# Modelo DeepSeek para respostas conversacionais simples
llm_basic = ChatOpenAI(model="deepseek-chat",
                       base_url="https://api.deepseek.com",
                       api_key=os.getenv("DEEP_SEEK_API_KEY"),
                       temperature=0.9)
