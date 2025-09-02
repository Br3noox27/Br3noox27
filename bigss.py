#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BIGSS - Tutor de Programação Inteligente
Um tutor que ensina a pensar como programador, não apenas corrige código
"""

import sys
import re
from typing import List, Dict, Optional

class BIGSS:
    def __init__(self):
        self.name = "BIGSS"
        self.session_history = []
        
        # Banco de perguntas orientadoras por categoria
        self.guiding_questions = {
            "syntax_error": [
                "Vamos examinar a sintaxe linha por linha. Você vê algo que parece estranho?",
                "Que símbolos você está usando nesta linha? Todos estão nos lugares corretos?",
                "Você verificou se todas as aspas, parênteses e chaves estão fechadas?",
                "Esta indentação está consistente com o resto do código?"
            ],
            "logic_error": [
                "Qual é o objetivo desta função/bloco de código?",
                "Vamos rastrear o que acontece com cada variável. Qual valor ela deveria ter aqui?",
                "O que você esperava que acontecesse neste ponto?",
                "Você pode me explicar o que esta condição está verificando?"
            ],
            "runtime_error": [
                "Que tipo de dados você está esperando nesta variável?",
                "Você verificou se esta variável tem um valor antes de usá-la?",
                "O que acontece se a entrada for diferente do esperado?",
                "Você já testou esta função com diferentes tipos de entrada?"
            ],
            "performance": [
                "Como você acha que o computador está processando este código?",
                "Quantas vezes este loop vai executar?",
                "Existe uma forma mais eficiente de fazer isso?",
                "Você conhece outras estruturas de dados que poderiam ajudar aqui?"
            ]
        }
        
        # Conceitos fundamentais para ensino
        self.concepts = {
            "variaveis": "Variáveis são como caixas que guardam informações. Cada caixa tem um nome e pode guardar diferentes tipos de dados.",
            "variáveis": "Variáveis são como caixas que guardam informações. Cada caixa tem um nome e pode guardar diferentes tipos de dados.",
            "loops": "Loops são formas de repetir código. Como fazer a mesma tarefa várias vezes sem copiar e colar.",
            "funcoes": "Funções são como receitas: você define os ingredientes (parâmetros) e os passos, e pode usar a receita quantas vezes quiser.",
            "funções": "Funções são como receitas: você define os ingredientes (parâmetros) e os passos, e pode usar a receita quantas vezes quiser.",
            "condicionais": "Condicionais são como decisões: 'se isso, então aquilo'. Permitem que o programa escolha diferentes caminhos.",
            "listas": "Listas são como uma fila de elementos. Você pode adicionar, remover e acessar elementos em diferentes posições.",
            "debugging": "Debugging é como ser um detetive: você coleta pistas (prints, logs) para descobrir o que está acontecendo no código."
        }

    def welcome(self):
        """Mensagem de boas-vindas do BIGSS"""
        return f"""
🤖 Olá! Eu sou o {self.name}, seu tutor de programação!

Minha missão é te ajudar a PENSAR como um programador, não apenas corrigir seu código.
Quando você trouxer um problema, vou fazer perguntas para te guiar até a solução.

Como posso te ajudar hoje?
1. Tenho um código com erro
2. Quero entender um conceito
3. Preciso de ajuda para resolver um problema
4. Sair

Digite o número da opção ou descreva seu problema:
"""

    def analyze_code_error(self, code: str) -> str:
        """Analisa código e gera perguntas orientadoras"""
        # Detecção simples de tipos de erro
        error_type = self._detect_error_type(code)
        questions = self.guiding_questions.get(error_type, self.guiding_questions["logic_error"])
        
        response = f"""
Interessante! Vou te ajudar a descobrir o que está acontecendo.

Primeiro, me conte:
- Qual era o resultado que você esperava?
- O que está acontecendo na prática?
- Em que momento você percebeu que algo estava errado?

Depois de me contar isso, vamos investigar juntos com estas perguntas:

"""
        for i, question in enumerate(questions[:3], 1):
            response += f"{i}. {question}\n"
            
        return response

    def _detect_error_type(self, code: str) -> str:
        """Detecta o tipo de erro mais provável baseado em padrões simples"""
        if re.search(r'["\'].*["\'].*["\']', code):  # Problemas com aspas
            return "syntax_error"
        elif re.search(r'\bfor\b|\bwhile\b', code):  # Código com loops
            return "logic_error"
        elif re.search(r'\bdef\b|\bclass\b', code):  # Funções ou classes
            return "logic_error"
        elif re.search(r'\[\]|\bNone\b', code):  # Possíveis problemas com None ou listas vazias
            return "runtime_error"
        else:
            return "logic_error"

    def explain_concept(self, concept: str) -> str:
        """Explica conceitos de forma interativa"""
        concept_input = concept.lower().strip()
        concept_key = None
        
        # Busca conceito mais próximo
        for key in self.concepts:
            if key in concept_input or concept_input in key:
                concept_key = key
                break
        
        if concept_key and concept_key in self.concepts:
            explanation = self.concepts[concept_key]
            return f"""
💡 Conceito: {concept_key.title()}

{explanation}

Agora me responda:
1. Você já usou {concept_key} em algum código?
2. Que problemas você acha que {concept_key} pode resolver?
3. Você consegue pensar em um exemplo do dia a dia que funciona como {concept_key}?

Responda essas perguntas e vamos explorar mais profundamente!
"""
        else:
            return f"""
Não encontrei "{concept}" no meu banco de conceitos, mas podemos explorar juntos!

Me conte:
1. Onde você ouviu falar sobre "{concept}"?
2. Como você acha que "{concept}" funciona?
3. Que problema você está tentando resolver com "{concept}"?

Com suas respostas, posso te guiar melhor!
"""

    def problem_solving_guide(self) -> str:
        """Guia para resolução de problemas"""
        return """
🧠 Vamos aprender a abordar problemas como um programador!

Quando você tem um problema para resolver, siga estes passos:

1. **ENTENDA o problema**
   - O que exatamente você precisa fazer?
   - Quais são as entradas? Quais são as saídas esperadas?

2. **QUEBRE em partes menores**
   - Que passos você faria manualmente?
   - Quais partes são mais simples?

3. **PLANEJE antes de codificar**
   - Que estruturas de dados você precisa?
   - Que funções ou algoritmos podem ajudar?

4. **TESTE frequentemente**
   - Teste cada parte pequena antes de juntar tudo
   - Use exemplos simples primeiro

Me conte qual problema você está tentando resolver e vamos aplicar esses passos juntos!
"""

    def interactive_session(self):
        """Sessão interativa principal do BIGSS"""
        print(self.welcome())
        
        while True:
            user_input = input("\n> ").strip()
            
            if user_input.lower() in ['sair', 'quit', 'exit', '4']:
                print(f"\n🎓 Foi um prazer te ajudar a pensar como programador!")
                print(f"Lembre-se: a melhor forma de aprender é questionando e experimentando!")
                break
                
            elif user_input in ['1']:
                print("\n📝 Cole seu código abaixo (termine com uma linha vazia):")
                code_lines = []
                while True:
                    line = input()
                    if line.strip() == "":
                        break
                    code_lines.append(line)
                
                code = "\n".join(code_lines)
                print(self.analyze_code_error(code))
                
            elif user_input in ['2']:
                concept = input("\nQual conceito você quer entender? ")
                print(self.explain_concept(concept))
                
            elif user_input in ['3']:
                print(self.problem_solving_guide())
                
            else:
                # Resposta livre - tenta categorizar e responder apropriadamente
                if "erro" in user_input.lower() or "bug" in user_input.lower():
                    print("\n🔍 Você mencionou um erro! Que tal me mostrar o código?")
                    print("Digite '1' para colar o código, ou me conte mais sobre o erro.")
                elif any(word in user_input.lower() for word in ['como', 'o que é', 'não entendo']):
                    print("\n💭 Parece que você tem uma dúvida conceitual!")
                    print("Digite '2' para explorar conceitos, ou me conte mais sobre sua dúvida.")
                else:
                    print(f"\n🤔 Interessante! Me conte mais detalhes:")
                    print("- Se é um erro de código, digite '1'")
                    print("- Se é uma dúvida conceitual, digite '2'") 
                    print("- Se precisa resolver um problema, digite '3'")

def main():
    """Função principal"""
    bigss = BIGSS()
    
    try:
        bigss.interactive_session()
    except KeyboardInterrupt:
        print(f"\n\n🎓 Tchau! Continue questionando e aprendendo! 🚀")
    except Exception as e:
        print(f"\n❌ Ops! Algo deu errado: {e}")
        print("Mas ei, isso é uma ótima oportunidade de aprender debugging! 🐛")

if __name__ == "__main__":
    main()