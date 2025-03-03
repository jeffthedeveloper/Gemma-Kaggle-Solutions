# Commit: fix/missing-model-files
# Solução: Listar arquivos no diretório para verificar a presença dos arquivos necessários.

import os

def list_files_in_directory(directory):
    """Lista todos os arquivos e subdiretórios em um determinado diretório."""
    try:
        print(f"Listando arquivos em: {directory}")
        for root, dirs, files in os.walk(directory):
            for file in files:
                print(os.path.join(root, file))
            for dir in dirs:
                 print(os.path.join(root, dir))


    except FileNotFoundError:
        print(f"O diretório '{directory}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Substitua pelo caminho do diretório que você quer verificar.
    directory_to_list = "/kaggle/input/gemma/transformers/7b-it/2"
    list_files_in_directory(directory_to_list)