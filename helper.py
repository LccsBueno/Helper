import argparse
from chat import chatInitiate
import time

def main():
    inicio = time.time()
    
    print(f"Tempo: {inicio - inicio}")
    
    parser = argparse.ArgumentParser(
        description="Um script de exemplo que processa uma pergunta."
    )
    
    parser.add_argument("question", help="query para o chatgpt")
    
    args = parser.parse_args()
    
    chatInitiate(args.question, inicio)
    # print("\n"+chatInitiate(args.question))
    # print(f"Processando o arquivo: {args.question}")

if __name__ == "__main__":
    main()