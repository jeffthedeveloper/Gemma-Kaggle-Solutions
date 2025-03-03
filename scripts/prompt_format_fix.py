# Commit: fix/prompt-formatting
# Solução: Corrigir a formatação do prompt para corresponder ao esperado pelo modelo.

def format_prompt_gemma(prompt, history=None):
    """
    Formata o prompt para o modelo Gemma, incluindo o histórico da conversa, se houver.

    Args:
        prompt: A pergunta ou instrução atual do usuário.
        history: Uma lista opcional de tuplas (papel, mensagem) representando
                 o histórico da conversa.  `papel` deve ser "user" ou "model".

    Returns:
        Uma string formatada pronta para ser usada como entrada para o modelo Gemma.
    """

    formatted_prompt = ""

    if history:
        for role, message in history:
            if role == "user":
                formatted_prompt += f"<start_of_turn>user\n{message}<end_of_turn>\n"
            elif role == "model":
                formatted_prompt += f"<start_of_turn>model\n{message}<end_of_turn>\n"
            else:
                raise ValueError("O papel no histórico deve ser 'user' ou 'model'.")

    formatted_prompt += f"<start_of_turn>user\n{prompt}<end_of_turn>\n"
    formatted_prompt += "<start_of_turn>model\n"  # Adiciona a tag de início para a resposta do modelo

    return formatted_prompt



if __name__ == "__main__":
    # Exemplo de uso:
    user_prompt = "Quais são os benefícios da meditação?"
    conversation_history = [
        ("user", "Olá, Gemma!"),
        ("model", "Olá! Como posso ajudar?"),
    ]

    formatted_prompt1 = format_prompt_gemma(user_prompt)
    print("Prompt formatado (sem histórico):\n", formatted_prompt1)
    print("-" * 20)

    formatted_prompt2 = format_prompt_gemma(user_prompt, conversation_history)
    print("Prompt formatado (com histórico):\n", formatted_prompt2)
    #Pode ser testado com um modelo carregado
    # gemma_lm = load_gemma_local() #Usar o script load_local_model
    # if gemma_lm:
    #     generated_text = gemma_lm.generate(formatted_prompt2, max_length=150)
    #     print(generated_text)