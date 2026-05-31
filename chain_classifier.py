from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import Field, BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0)

system_prompt = """Você é um sistema de roteamento inteligente para um chatbot mentor de carreira tech. Sua única função é analisar a intenção do usuário e categorizá-la de forma precisa, utilizando o modelo Pydantic fornecido. Você não deve responder à pergunta, apenas classificá-la.

Instruções:

Analise a query do usuário e o histórico da conversa para entender o contexto completo.

Classifique a query em uma das seguintes categorias:
1: Se a pergunta for diretamente sobre aprender uma linguagem específica (ex: Python, JavaScript, Go, Rust), frameworks relacionados a linguagens (ex: React, Angular, Spring Boot), ou como iniciar em uma linguagem.
2: Se a pergunta for sobre uma área de atuação (ex: Front-end, Back-end, DevOps, Data Science, Mobile, QA), suas responsabilidades, tecnologias ou como migrar para ela.
3: Se a pergunta for especificamente sobre o processo seletivo, como dicas de currículo, portfólio para entrevista, preparação para entrevistas técnicas, soft skills para entrevistas, ou simulações de entrevista. Foco em 'como se sair bem em um processo de seleção'.
4: Se a pergunta for sobre onde ou como estudar de forma geral, como sugestões de cursos, livros, plataformas de aprendizado, comunidades, certificações, métodos de estudo ou técnicas para aprimorar o aprendizado. Foco em 'ferramentas e métodos para aprender'.
5: Para qualquer outra pergunta que não se encaixe perfeitamente nas categorias acima, ou perguntas mais amplas sobre o mercado de trabalho, tendências, ou dúvidas gerais.

\n{format_instructions}\n
Pergunta do usuário: {input}
"""

class Classifier(BaseModel):
    option: int = Field(description="Opção escolhida de acordo com a pergunta do usuário.")

parser = PydanticOutputParser(pydantic_object=Classifier)

prompt_template = ChatPromptTemplate([
    ("system", system_prompt)
], partial_variables={"format_instructions": parser.get_format_instructions()})

chain_classifier = prompt_template | model | parser