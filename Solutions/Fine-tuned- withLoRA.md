2. Carregar Pesos Fine-tuned com LoRA

Commit: fix/load-lora-weights

Solução: Garantir compatibilidade entre o modelo base e os pesos finetuned antes de carregá-los.

Código:

gemma_lm = GemmaCausalLM.from_preset("gemma_2b_en")
gemma_lm.backbone.enable_lora(rank=4)
gemma_lm.load_weights(filepath)

