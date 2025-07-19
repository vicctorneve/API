import re

def validar_cpf(cpf: str) -> bool:
    print("Validando cpf")
    cpf = re.sub(r'\D', '', cpf)

    print(len(cpf) != 11)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    for i in [9, 10]:
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[i]):
            return False
        
    return True