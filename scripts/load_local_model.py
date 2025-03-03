# Commit: fix/load-local-model
# Solução: Substituir o caminho do modelo para um diretório local no Kaggle.

import keras_nlp

def load_gemma_local():
    """Carrega o modelo Gemma de um diretório local no Kaggle."""
    try:
        # Caminho LOCAL para os arquivos do modelo Gemma (ajuste conforme necessário)
        model_path = "/kaggle/input/gemma/keras/gemma_instruct_2b_en/1/"
        gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset(model_path)
        print("Modelo Gemma carregado com sucesso do diretório local.")
        return gemma_lm
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None

if __name__ == "__main__":
    gemma_model = load_gemma_local()
    if gemma_model:
        # Faça algo com o modelo, por exemplo, gere texto
        prompt = "Escreva um poema curto sobre a natureza."
        generated_text = gemma_model.generate(prompt, max_length=100)
        print(generated_text)