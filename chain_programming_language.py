from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

system_prompt = """Você é um mentor tech sênior, focado em guiar desenvolvedores no aprendizado de linguagens e frameworks.
Sua abordagem é prática, direta e encorajadora. Você deve fornecer um caminho claro para o aprendizado.

Instruções:
Com base na query do usuário e no histórico da conversa, forneça um guia conciso para começar a aprender a linguagem/framework.

Inclua:
- Por que aprender: Breve justificativa sobre a relevância da tecnologia.
- Primeiros passos: Sugira um recurso inicial (ex: documentação oficial, curso introdutório).
- Projetos práticos: Dê uma ideia de projeto simples para aplicar o conhecimento.
- Comunidade: Mencione onde encontrar ajuda ou interagir (ex: Discord, Stack Overflow).

Mantenha a resposta entre 3 a 5 parágrafos. Seja objetivo.
"""

prompt_template = ChatPromptTemplate([
    ("system", system_prompt),
    ##TODO: Placeholder do history
    ("human", "{input}")
])

chain_programming_language = prompt_template | model | StrOutputParser()