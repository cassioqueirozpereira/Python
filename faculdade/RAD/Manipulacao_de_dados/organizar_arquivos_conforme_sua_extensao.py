import os
import shutil

def criar_diretorios(diretorios):
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f"Diretório '{diretorio}' criado.")
            except PermissionError:
                print(f"Sem permissão para criar o diretório '{diretorio}'.")
            except Exception as erro:
                print(f"Erro inesperado ao criar '{diretorio}': {erro}")

def mover_arquivos(diretorio_origem):
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        print(f"\ndiretorio_origem: {diretorio_origem}, arquivo: {arquivo}")
        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1].lower()
            print(f"\ncaminho_arquivo: {caminho_arquivo}, extensão: {extensao}")
            if extensao in ["pdf", "txt", "jpg"]:
                diretorio_destino = os.path.join(diretorio_origem, extensao)
                try:
                    shutil.move(caminho_arquivo, diretorio_destino)
                    print(f"'{arquivo}' movido para '{diretorio_destino}'.")
                except PermissionError:
                    print(f"Sem permissão para mover '{arquivo}'.")
                except Exception as erro:
                    print(f"Erro inesperado ao mover '{arquivo}': {erro}")
            else:
                print(f"Extensão '{extensao}' de '{arquivo}' não é suportada.")


def main():
    diretorio_trabalho = "diretorio_trabalho"
    diretorios = [os.path.join(diretorio_trabalho, "pdf"),
                  os.path.join(diretorio_trabalho, "txt"),
                  os.path.join(diretorio_trabalho, "jpg")]
    
    # criar diretórios se não existirem
    criar_diretorios(diretorios)

    # mover arquivos para os diretórios correspondentes
    mover_arquivos(diretorio_trabalho)

if __name__ == "__main__":
    main()