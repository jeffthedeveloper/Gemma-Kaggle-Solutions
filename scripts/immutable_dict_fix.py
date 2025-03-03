# Commit: fix/immutable-dict-error
# Solução: Tentar instalar novamente e verificar a conexão de rede.

import subprocess

def install_immutabledict():
    """Tenta instalar a biblioteca immutabledict."""
    try:
        subprocess.check_call(["pip", "install", "immutabledict"])
        print("immutabledict instalado com sucesso!")
    except subprocess.CalledProcessError:
        print("Erro ao instalar immutabledict. Verifique sua conexão com a internet e se o pip está funcionando corretamente.")
    except Exception as e:
        print(f"Erro ao instalar immutabledict: {e}")
def check_internet_connection():
    """Verifica se há conexão com a internet."""
    try:
        # Tenta fazer um ping em um servidor público (ex: Google DNS)
        subprocess.check_call(["ping", "-c", "4", "8.8.8.8"])  # 4 pacotes
        print("Conexão com a internet OK.")
        return True
    except subprocess.CalledProcessError:
        print("Sem conexão com a internet.  Verifique suas configurações de rede.")
        return False
    except Exception as e:
        print("Erro ao instalar immutabledict: {e}")

if __name__ == "__main__":
    if check_internet_connection():
        install_immutabledict()