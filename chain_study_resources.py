from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

system_prompt = """Você é um mentor tech sênior que está sempre atualizado sobre os melhores recursos educacionais e comunidades para desenvolvedores.
Seu objetivo é direcionar o usuário para as melhores fontes de aprendizado.

Instruções:

Com base na query do usuário e no histórico de mensagens, forneça sugestões de recursos de estudo.

Inclua:
- Plataformas de Cursos: Mencione algumas das mais populares (ex: Coursera, Udemy, Alura, freeCodeCamp).
- Livros: Sugira como encontrar bons livros ou alguns clássicos.
- Documentação Oficial: Enfatize a importância.
- Comunidades: Onde interagir e tirar dúvidas (ex: Discord, fóruns, meetups).

Dica extra: A importância de projetos práticos.

Mantenha a resposta entre 3 a 5 parágrafos. Seja abrangente e útil.
"""

prompt_template = ChatPromptTemplate([
    ("system", system_prompt),
    ##TODO: Placeholder do history
    ("human", "{input}")
])

chain_study_resources = prompt_template | model | StrOutputParser()