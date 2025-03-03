# Commit: fix/tokenizer-not-found
# Solução: Certificar-se de carregar o tokenizer antes de utilizá-lo.

import keras_nlp
from keras_nlp.models import GemmaCausalLM

def load_model_and_tokenizer(model_preset):
    """Carrega o modelo Gemma e seu tokenizer associado."""
    try:
        gemma_lm = GemmaCausalLM.from_preset(model_preset)
        tokenizer = gemma_lm.tokenizer  # Acessa o tokenizer diretamente do modelo
        print("Modelo e tokenizer carregados com sucesso.")
        return gemma_lm, tokenizer
    except Exception as e:
        print(f"Erro ao carregar o modelo ou tokenizer: {e}")
        return None, None



def use_tokenizer(tokenizer, text):
    """Exemplo de como usar o tokenizer para tokenizar texto."""
    if tokenizer:
        encoded = tokenizer.encode(text)
        print(f"Texto original: {text}")
        print(f"Texto tokenizado: {encoded}")
        decoded = tokenizer.decode(encoded)
        print(f"Texto decodificado: {decoded}")
        return encoded
    else:
        print("Tokenizer não carregado. Execute load_model_and_tokenizer primeiro.")
        return None


if __name__ == "__main__":
    model_preset = "gemma_2b_en" #exemplo de preset
    gemma_lm, tokenizer = load_model_and_tokenizer(model_preset)

    if gemma_lm and tokenizer:
      text_to_tokenize = "Olá, mundo! Este é um teste do tokenizer."
      use_tokenizer(tokenizer, text_to_tokenize)