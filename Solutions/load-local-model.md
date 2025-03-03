1. Carregando Modelo e Pesos do Disco

Commit: fix/load-local-model

Solução: Substituir o caminho do modelo para um diretório local no Kaggle.

Código:

> gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("/kaggle/input/gemma/keras/gemma_instruct_2b_en/1/")

