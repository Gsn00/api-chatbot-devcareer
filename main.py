from chain_classifier import chain_classifier
from langchain_core.runnables import RunnableLambda, RunnableParallel
from chain_programming_language import chain_programming_language
from chain_development_area import chain_development_area
from chain_interview_preparation import chain_interview_preparation
from chain_study_resources import chain_study_resources
from chain_general_topics import chain_general_topics
from operator import itemgetter

def classify_route(input: dict):
    option = input["option"].option
    
    print(f"\n>> Pergunta do Usuário: {input["input"]}")
    match option:
        case 1:
            print(f">> Escolha Pydantic = {option} (Linguagem de Programação)\n")
            return chain_programming_language
        case 2:
            print(f">> Escolha Pydantic = {option} (Área de Desenvolvimento)\n")
            return chain_development_area
        case 3:
            print(f">> Escolha Pydantic = {option} (Preparação para Entrevista)\n")
            return chain_interview_preparation
        case 4:
            print(f">> Escolha Pydantic = {option} (Recursos de Estudo)\n")
            return chain_study_resources
        case _:
            print(f">> Escolha Pydantic = {option} (Tópicos Gerais)\n")
            return chain_general_topics
            

chain = RunnableParallel({"input": itemgetter("input"), "option": chain_classifier}) | RunnableLambda(classify_route)

result = chain.invoke({"input":"Quais assuntos estão em alta em 2026 e que serão usados nos próximos anos?"})

print(result)