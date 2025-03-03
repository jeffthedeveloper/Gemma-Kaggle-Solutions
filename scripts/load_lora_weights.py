# Commit: fix/load-lora-weights
# Solução: Garantir compatibilidade entre o modelo base e os pesos finetuned antes de carregá-los.

import keras_nlp
from keras_nlp.models import GemmaCausalLM

def load_lora_weights(filepath):
    """Carrega pesos LoRA em um modelo Gemma, verificando a compatibilidade."""
    try:
        gemma_lm = GemmaCausalLM.from_preset("gemma_2b_en")  # Carrega o modelo base
        gemma_lm.backbone.enable_lora(rank=4)  # Habilita o LoRA (importante para compatibilidade)
        gemma_lm.load_weights(filepath) #Carrega os pesos do lora
        print("Pesos LoRA carregados com sucesso.")
        return gemma_lm
    except Exception as e:
        print(f"Erro ao carregar os pesos LoRA: {e}")
        return None

if __name__ == "__main__":
    # Substitua 'path/to/your/lora/weights.h5' pelo caminho real dos seus pesos LoRA.
    lora_weights_path = "path/to/your/lora/weights.h5"
    gemma_model = load_lora_weights(lora_weights_path)
    if gemma_model:
        print(gemma_model.generate("teste", max_length=20))