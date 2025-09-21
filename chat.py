from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from os import path

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
        
    """
)

def chatInitiate(query: str) -> str:
    # model = ChatOpenAI(model=os.getenv("OPENAI_MODEL_CHAT"),  temperature=1)
    model = ChatOpenAI(model="gpt-5-nano",  temperature=1)

    chain = template | model
    result = chain.invoke({"question": query})

    return result.content