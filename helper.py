import argparse
from chat import chatInitiate

def main():
    
    parser = argparse.ArgumentParser(
        description="Um script de exemplo que processa uma pergunta."
    )
    
    parser.add_argument("question", help="query para o chatgpt")
    
    args = parser.parse_args()
    print(chatInitiate(args.question))
    # print(f"Processando o arquivo: {args.question}")

if __name__ == "__main__":
    main()