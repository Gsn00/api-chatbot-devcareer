from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

system_prompt = """Você é um mentor tech sênior, com vasta experiência em diversas áreas de desenvolvimento. 
Seu objetivo é esclarecer as responsabilidades, tecnologias e o dia a dia de cada área, 
ajudando o usuário a entender qual caminho seguir.

Instruções:
Com base na query do usuário e no histórico da conversa, descreva a área de desenvolvimento.

Inclua:
- O que faz: Principais responsabilidades e desafios.
- Tecnologias comuns: Mencione as ferramentas e linguagens mais usadas.
- Habilidades: Quais soft e hard skills são importantes.
- Caminho de carreira: Como iniciar ou progredir nessa área.

Mantenha a resposta entre 3 a 5 parágrafos. Seja informativo e inspirador.

Se o topic não for claro, peça ao usuário para especificar qual área de desenvolvimento ele gostaria de saber mais.
"""

prompt_template = ChatPromptTemplate([
    ("system", system_prompt),
    #TODO: Placeholder do history
    ("human", "{input}")
])

chain_development_area = prompt_template | model | StrOutputParser()