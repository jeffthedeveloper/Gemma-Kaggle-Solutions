# Commit: fix/license-not-accepted
# Solução: Garantir que a licença do modelo foi aceita antes de tentar usá-lo no Kaggle.

def show_license_agreement():
    """Exibe instruções sobre como aceitar a licença do modelo Gemma no Kaggle."""

    print("-" * 50)
    print("                   Aceitação da Licença do Modelo Gemma")
    print("-" * 50)
    print("\nPara usar o modelo Gemma no Kaggle, você precisa aceitar os termos de licença.")
    print("\nSiga os seguintes passos:")
    print("\n1. **Vá para a página do modelo Gemma no Kaggle:**")
    print("   -  Normalmente, você encontra o modelo Gemma na seção 'Models' do Kaggle,")
    print("      ou através de um link direto fornecido na competição ou dataset que usa o Gemma.")
    print("      Exemplo:  https://www.kaggle.com/models/google/gemma (Este é um link geral,")
    print("                substitua pelo link *específico* do modelo que você está usando.)")
    print("\n2. **Leia os Termos e Condições:**")
    print("   -  Na página do modelo, procure por uma seção de termos de licença,")
    print("      termos e condições, ou um acordo de uso.")
    print("   -  Leia atentamente os termos antes de prosseguir.")
    print("\n3. **Aceite a Licença:**")
    print("   -  Se você concordar com os termos, geralmente haverá um botão, checkbox,")
    print("      ou outro mecanismo para indicar sua aceitação.")
    print("   -  Clique ou marque a opção para aceitar a licença.  O texto exato pode variar")
    print("      (ex: 'I agree', 'Accept License', 'Acknowledge Terms', etc.).")

    print("\n4. **Verifique se a Aceitação foi Registrada (Importante):**")
    print("    -  Após aceitar, a página do modelo *deve* mostrar claramente que você")
    print("       aceitou a licença.  Pode haver uma mensagem de confirmação, uma mudança")
    print("       no status, ou a remoção do aviso de licença.")
    print("    -  Se você *não* vir uma confirmação clara, tente o seguinte:")
    print("        -  Atualize a página (F5 ou Ctrl+R / Cmd+R).")
    print("        -  Limpe o cache do seu navegador.")
    print("        -  Tente um navegador diferente.")
    print("        -  Verifique se você está logado na conta Kaggle correta.")
    print("        -  Se o problema persistir, entre em contato com o suporte do Kaggle.")

    print("\n5. **(Opcional) Reinicie o Kernel do Kaggle:**")
    print("   -  Em alguns casos raros, pode ser necessário reiniciar o kernel do seu")
    print("      notebook Kaggle para que a aceitação da licença seja reconhecida.")
    print("      Isso normalmente *não* é necessário, mas é uma etapa de solução de")
    print("      problemas caso você ainda encontre erros relacionados à licença.")

    print("-" * 50)
    print("IMPORTANTE: Este script *não* pode aceitar a licença automaticamente.")
    print("             A aceitação da licença é um processo *manual* que deve ser")
    print("             feito *diretamente* no site do Kaggle.")
    print("-" * 50)
    print("\n")

if __name__ == "__main__":
    show_license_agreement()