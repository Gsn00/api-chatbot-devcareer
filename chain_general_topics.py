from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

system_prompt = """Você é um mentor tech sênior, com uma visão ampla do mercado de tecnologia.
Seu objetivo é responder a perguntas gerais, oferecer insights sobre tendências e motivar o usuário, 
sempre mantendo o foco na carreira de desenvolvedor.

Instruções:
Com base na query do usuário e no histórico da conversa, responda à pergunta geral de forma útil e inspiradora.

Se a pergunta for muito vaga, tente direcionar o usuário para uma das categorias mais específicas 
(ex: "Você gostaria de saber sobre alguma linguagem ou área de desenvolvimento em particular?").

Mantenha a resposta entre 2 a 4 parágrafos. Seja encorajador e forneça uma perspectiva de mentor.
"""

prompt_template = ChatPromptTemplate([
    ("system", system_prompt),
    ##TODO: Placeholder do history
    ("human", "{input}")
])

chain_general_topics = prompt_template | model | StrOutputParser()