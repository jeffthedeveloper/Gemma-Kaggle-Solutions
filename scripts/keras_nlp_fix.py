# Commit: fix/keras-nlp-missing-models
# Solução: Verificar a versão correta da biblioteca keras_nlp e atualizá-la se necessário.

import subprocess
import pkg_resources

def check_keras_nlp_version():
    """Verifica a versão instalada do keras-nlp e sugere atualização se for antiga."""
    try:
        installed_version = pkg_resources.get_distribution("keras-nlp").version
        print(f"Versão do keras-nlp instalada: {installed_version}")

        #Verifica se a versão é antiga (exemplo: anterior a 0.8.0) e sugere atualização
        if int(installed_version.split(".")[1]) < 8:
            print("Sua versão do keras-nlp pode estar desatualizada.")
            resposta = input("Deseja atualizar o keras-nlp? (s/n): ").strip().lower()
            if resposta == 's':
                update_keras_nlp()
            else:
                print("Atualização cancelada.")
                print("Se você tiver problemas, pode atualizar o keras-nlp utilizando a função update_keras_nlp()")

    except pkg_resources.DistributionNotFound:
        print("keras-nlp não está instalado. Instale-o usando: pip install keras-nlp")
    except Exception as e:
        print(f"Erro ao verificar a versão do keras-nlp: {e}")


def update_keras_nlp():
    """Atualiza a biblioteca keras-nlp."""
    try:
        subprocess.check_call(["pip", "install", "--upgrade", "keras-nlp"])
        print("keras-nlp atualizado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao atualizar keras-nlp: {e}")
    except Exception as e:
         print(f"Erro ao atualizar keras-nlp: {e}")

if __name__ == "__main__":
    check_keras_nlp_version()