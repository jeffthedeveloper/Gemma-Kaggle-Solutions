## Gemma Kaggle Fixes

Este repositório contém soluções e scripts para problemas comuns encontrados ao usar o modelo Gemma no Kaggle. Ele aborda erros de carregamento de modelo, pesos LoRA, caminhos de arquivos, tokenizer, formatação de prompt e muito mais.

## Estrutura do Repositório

O repositório é organizado da seguinte forma:

<ul>
  <li>gemma_kaggle_fixes/
    <ul>
      <li>scripts/  &lt;-  Scripts Python para cada solução.
        <ul>
          <li>load_local_model.py</li>
          <li>load_lora_weights.py</li>
          <li>check_model_path.py</li>
          <li>list_missing_files.py</li>
          <li>tokenizer_fix.py</li>
          <li>json_fix.py</li>
          <li>keras_nlp_fix.py</li>
          <li>immutable_dict_fix.py</li>
          <li>flax_checkpoint_fix.py</li>
          <li>prompt_format_fix.py</li>
          <li>license_acceptance_fix.py</li>
        </ul>
      </li>
      <li>docs/ &lt;- Documentação detalhada para cada problema.
        <ul>
            <li>Fine-tuned-withLoRA.md</li>
            <li>immutable-dict-error.md</li>
            <li>incomplete-flax-checkpoint.md</li>
            <li>incorrect-model-path.md</li>
            <li>json-decode-error.md</li>
            <li>keras-nlp-missing-models.md</li>
            <li>load-local-model.md</li>
            <li>missing-model-files.md</li>
            <li>prompt-formatting.md</li>
            <li>tokenizer-not-found.md</li>
            <li>license-not-accepted.md</li>
        </ul>
      </li>
      <li>README.md          &lt;-  Este arquivo.</li>
    </ul>
  </li>
</ul>

Como Usar
Clone o Repositório:

```bash
git clone <URL_do_seu_repositorio>

cd gemma_kaggle_fixes 
```
Use os Scripts:
Importe e use as funções dos scripts individuais em seus notebooks Kaggle conforme necessário.  Cada script contém um exemplo de uso na seção:

```Python

if __name__ == "__main__":.  Por exemplo:
```

# Em seu notebook Kaggle:

```Python

from scripts.load_local_model import load_gemma_local

gemma_model = load_gemma_local()
if gemma_model:
    prompt = "Escreva um poema curto sobre a natureza."
    generated_text = gemma_model.generate(prompt, max_length=100)
    print(generated_text)

# Ou, para o script de aceitação de licença:
from scripts.license_acceptance_fix import show_license_agreement
show_license_agreement() # Isso *não* aceita a licença, apenas *mostra* as instruções.
Adapte os caminhos: Certifique-se de ajustar os caminhos dos arquivos (por exemplo, o caminho para o modelo, os pesos LoRA, etc.) nos scripts para corresponder à sua configuração específica no Kaggle.

```
<br>

Consulte a Documentação (Opcional):  Se precisar de mais detalhes sobre um problema específico, consulte os arquivos .md correspondentes na pasta docs/.

<br>

**Contribuindo**

Contribuições são bem-vindas! Se você encontrar outros problemas com o Gemma no Kaggle ou tiver melhorias para as soluções existentes, sinta-se à vontade para abrir um pull request.

**Faça um fork do repositório.**

Crie uma nova branch para sua feature ou correção de bug:

```bash
git checkout -b feature/sua-feature 
git checkout -b fix/seu-bugfix
```

Faça commit das suas mudanças (git commit -am 'Adiciona feature X' ou git commit -am 'Corrige bug Y'). Use mensagens de commit claras e descritivas.
Faça push para a branch (git push origin feature/sua-feature).
Abra um pull request.

---

Licença

Copyright (c) 2025 Jefferson Firmino Mendes

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e dos arquivos de documentação associados (o "Software"), para lidar
com o Software sem restrições, incluindo, sem limitação, os direitos
de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender
cópias do Software, e para permitir que as pessoas a quem o Software é
fornecido o façam, sob as seguintes condições:   

_O aviso de copyright acima e este aviso de permissão devem ser incluídos em todas as
cópias ou partes substanciais do Software._

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO A, GARANTIAS DE COMERCIALIZAÇÃO,
ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM NENHUM CASO O
OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTROS
RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, ATO ILÍCITO OU DE OUTRA FORMA, DECORRENTE DE,
FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO
PROGRAMAS