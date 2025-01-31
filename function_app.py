import azure.functions as func
import json
import re

def is_valid_cpf(cpf: str) -> bool:
    """Valida um CPF brasileiro"""
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos

    if len(cpf) != 11 or cpf == cpf[0] * 11:  # Verifica se tem 11 dígitos e se não são repetidos
        return False

    def calc_dv(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        dv = (soma * 10) % 11
        return dv if dv < 10 else 0

    return int(cpf[9]) == calc_dv(cpf, 10) and int(cpf[10]) == calc_dv(cpf, 11)

def main(req: func.HttpRequest) -> func.HttpResponse:
    """Função principal da Azure Function"""
    try:
        req_body = req.get_json()
        cpf = req_body.get("cpf")

        if not cpf:
            return func.HttpResponse(json.dumps({"error": "CPF é obrigatório"}), status_code=400)

        valid = is_valid_cpf(cpf)
        return func.HttpResponse(json.dumps({"cpf": cpf, "valid": valid}), mimetype="application/json")
    
    except ValueError:
        return func.HttpResponse(json.dumps({"error": "Requisição inválida"}), status_code=400)

