# Commit: fix/incomplete-flax-checkpoint
# Solução: Copiar os arquivos do checkpoint para um diretório local antes de carregá-los.


import os
import shutil

def copy_flax_checkpoint(source_dir, destination_dir):
    """Copia arquivos de checkpoint Flax de um diretório para outro."""
    try:
        # Cria o diretório de destino, se ele não existir
        os.makedirs(destination_dir, exist_ok=True)

        # Lista todos os arquivos no diretório de origem
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            destination_path = os.path.join(destination_dir, filename)

            # Verifica se é um arquivo (e não um subdiretório)
            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)  # Copia, preservando metadados
                print(f"Arquivo copiado: {filename}")

        print(f"Checkpoint Flax copiado para: {destination_dir}")
        return destination_dir

    except FileNotFoundError:
        print(f"Erro: O diretório de origem '{source_dir}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao copiar o checkpoint: {e}")
        return None


if __name__ == "__main__":
    # Exemplo de uso:
    source_directory = "/kaggle/input/gemma/flax/jemma-2b-it/1"  # Substitua pelo caminho correto
    destination_directory = "/kaggle/working/flax_checkpoint" #Diretorio local

    copied_checkpoint_path = copy_flax_checkpoint(source_directory, destination_directory)

    if copied_checkpoint_path:
        # Agora você pode carregar o checkpoint a partir de `copied_checkpoint_path`
        # Exemplo (usando jax/flax):
        #   import jax
        #   import flax
        #   ...
        #   restored_params = flax.serialization.from_bytes(target=..., data=open(copied_checkpoint_path, "rb").read())
        print("Utilize o caminho:", copied_checkpoint_path, "para carregar o checkpoint")
    else:
        print("Falha na cópia")