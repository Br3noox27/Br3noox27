#!/usr/bin/env python3
"""
Teste automatizado do BIGSS para validar funcionalidades principais
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from bigss import BIGSS

def test_bigss():
    """Executa testes automatizados do BIGSS"""
    tutor = BIGSS()
    
    print("🧪 TESTANDO BIGSS - Tutor de Programação")
    print("=" * 50)
    
    # Teste 1: Conceitos
    print("\n1️⃣ TESTE: Explicação de Conceitos")
    print("-" * 30)
    
    concepts_to_test = ["variáveis", "loops", "funções", "listas"]
    for concept in concepts_to_test:
        result = tutor.explain_concept(concept)
        if "💡 Conceito:" in result:
            print(f"✅ {concept}: PASSOU")
        else:
            print(f"❌ {concept}: FALHOU")
    
    # Teste 2: Análise de código
    print("\n2️⃣ TESTE: Análise de Código com Erro")
    print("-" * 30)
    
    code_samples = [
        "def test():\n    print('hello'",  # Erro de sintaxe
        "for i in range(10):\nprint(i)",   # Erro de indentação
        "def soma(a, b):\n    return a * b"  # Erro lógico
    ]
    
    for i, code in enumerate(code_samples, 1):
        result = tutor.analyze_code_error(code)
        if "Interessante!" in result and "me conte:" in result:
            print(f"✅ Código {i}: PASSOU")
        else:
            print(f"❌ Código {i}: FALHOU")
    
    # Teste 3: Guia de resolução
    print("\n3️⃣ TESTE: Guia de Resolução de Problemas")
    print("-" * 30)
    
    guide = tutor.problem_solving_guide()
    if "ENTENDA o problema" in guide and "QUEBRE em partes" in guide:
        print("✅ Guia de resolução: PASSOU")
    else:
        print("❌ Guia de resolução: FALHOU")
    
    # Teste 4: Mensagem de boas-vindas
    print("\n4️⃣ TESTE: Mensagem de Boas-vindas")
    print("-" * 30)
    
    welcome = tutor.welcome()
    if "BIGSS" in welcome and "tutor de programação" in welcome:
        print("✅ Mensagem de boas-vindas: PASSOU")
    else:
        print("❌ Mensagem de boas-vindas: FALHOU")
    
    print("\n" + "=" * 50)
    print("🎯 TESTES CONCLUÍDOS!")
    print("\nPara testar interativamente, execute: python bigss.py")

if __name__ == "__main__":
    test_bigss()