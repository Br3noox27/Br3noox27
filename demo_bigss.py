#!/usr/bin/env python3
"""
Demonstração do BIGSS - Simula interações típicas para mostrar a funcionalidade
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from bigss import BIGSS

def demonstrar_bigss():
    """Demonstra funcionalidades do BIGSS através de simulações"""
    tutor = BIGSS()
    
    print("🎭 DEMONSTRAÇÃO DO BIGSS")
    print("Esta demonstração simula interações típicas com o tutor")
    print("=" * 60)
    
    # Demonstração 1: Boas-vindas
    print("\n📋 CENÁRIO 1: Primeira interação")
    print("-" * 40)
    print(">>> Estudante abre o BIGSS")
    print(tutor.welcome())
    
    # Demonstração 2: Explicação de conceito
    print("\n📋 CENÁRIO 2: Estudante quer entender 'variáveis'")
    print("-" * 40)
    print(">>> Estudante: 'Não entendo o que são variáveis'")
    print(tutor.explain_concept("variáveis"))
    
    # Demonstração 3: Código com erro
    print("\n📋 CENÁRIO 3: Estudante tem código com erro")
    print("-" * 40)
    print(">>> Estudante cola este código:")
    code_with_error = """def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma + nota  # Erro aqui!
    return soma / len(notas)"""
    print(code_with_error)
    print("\n>>> BIGSS responde:")
    print(tutor.analyze_code_error(code_with_error))
    
    # Demonstração 4: Resolução de problemas
    print("\n📋 CENÁRIO 4: Estudante precisa resolver um problema")
    print("-" * 40)
    print(">>> Estudante: 'Como faço um programa que encontra o maior número?'")
    print(tutor.problem_solving_guide())
    
    print("\n" + "=" * 60)
    print("🚀 FIM DA DEMONSTRAÇÃO")
    print("\nPara usar interativamente: python bigss.py")
    print("Para ver mais exemplos: cat exemplos.md")

if __name__ == "__main__":
    demonstrar_bigss()