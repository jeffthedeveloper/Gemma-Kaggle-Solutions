# Commit: fix/json-decode-error
# Solução: Garantir que a saída do modelo esteja formatada corretamente como JSON antes de ser processada.

import json
import re

def safe_json_loads(json_string):
    """
    Tenta carregar uma string JSON, lidando com possíveis erros de formatação.
    Inclui limpeza básica para remover caracteres inválidos comuns.
    """
    try:
        # Tenta carregar o JSON diretamente
        return json.loads(json_string)
    except json.JSONDecodeError:
        try:
            # Limpeza 1: Remover vírgulas extras no final de objetos/arrays
            cleaned_string = re.sub(r',\s*}', '}', json_string)
            cleaned_string = re.sub(r',\s*]', ']', cleaned_string)

            # Limpeza 2: Escapar aspas duplas dentro de strings
            cleaned_string = re.sub(r'(?<!\\)"', r'\\"', cleaned_string)
            return json.loads(cleaned_string)


        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            print(f"String original: {json_string}")
            return None

def process_model_output(model_output):
     safe_json = safe_json_loads(model_output)
     if safe_json:
        print("JSON processado com sucesso")
        return safe_json
     else:
        print("Não foi possível processar")
        return None


if __name__ == "__main__":
    # Exemplos de uso
    malformed_json = '{"key": "value", "invalid": "json",}'  # Virgula extra
    slightly_malformed_json = '{"key": "value", "another": "test",'
    good_json = '{"key": "value", "another": "test"}'


    result1 = process_model_output(malformed_json)  # Deve imprimir o erro
    result2 = process_model_output(slightly_malformed_json)
    result3 = process_model_output(good_json)
    print(result3)