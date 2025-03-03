# Commit: fix/incorrect-model-path
# Solução: Adicionar manualmente o modelo como entrada no notebook e verificar o caminho correto.

import os

def check_model_path(model_path):
    """Verifica se o caminho do modelo fornecido existe e lista seu conteúdo."""
    if os.path.exists(model_path):
        print(f"O caminho do modelo '{model_path}' existe.")
        print("Conteúdo do diretório:")
        for item in os.listdir(model_path):
            print(f"- {item}")
    else:
        print(f"O caminho do modelo '{model_path}' NÃO existe. Verifique se você adicionou o modelo corretamente como entrada.")

if __name__ == "__main__":
    # Exemplo de uso:  Substitua pelo caminho que você quer verificar
    path_to_check = "/kaggle/input/gemma/keras/gemma_instruct_2b_en/1/"
    check_model_path(path_to_check)