from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from os import path

import time

load_dotenv()

template = PromptTemplate(
    input_variables=["question"],
    template=
    """
    Persona: Assuma a identidade de um Desenvolvedor Sênior e mentor técnico, com vasta experiência prática em múltiplas linguagens, arquiteturas e frameworks.
    Diretrizes da Resposta:
    Objetividade: Responda diretamente à pergunta de maneira breve, sem introduções desnecessárias e com poucas palavras.
    Didática: Explique conceitos complexos de forma simples e clara, como se estivesse ensinando um colega com menos experiência.
    Honestidade Intelectual: Se não souber a resposta ou se o tópico for muito novo ou volátil, admita abertamente. Não invente informações.
    Idioma: Responda exclusivamente em português do Brasil.

    Pergunta: {question}
    Resposta: Somente mostre a resposta, sem nenhuma outra anotação.
    """
)

def chatInitiate(query: str, tempoInicio) -> str:

    tempo_agr = time.time()
    print(f"\nTempo: {tempo_agr - tempoInicio}")

    # model = ChatOpenAI(model=os.getenv("OPENAI_MODEL_CHAT"),  temperature=1)
    model = ChatOpenAI(model="gpt-3.5-turbo",  temperature=1)

    tempo_agr = time.time()
    print(f"\nTempo: {tempo_agr - tempoInicio}")
    
    chain = template | model
    # result = chain.invoke({"question": query})
    
    tempo_agr = time.time()
    print(f"\nTempo: {tempo_agr - tempoInicio}")
    print("\n")
    for chunk in chain.stream({"question": query}):
        if hasattr(chunk, 'content'):
            print(chunk.content, end="", flush=True)

    tempo_agr = time.time()
    print(f"\nTempo: {tempo_agr - tempoInicio}")
    print()
    # return result.content