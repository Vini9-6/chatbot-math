# chatbot_matematica.py

"""
ATIVIDADE 03 - CHATBOT POR REGRAS
Cenário 4: Chatterbot Educacional para Revisão de Matemática Básica
Componentes: [Seu Nome Aqui]
"""

import re
import ast
import operator as _operator

# --- Funções de Resposta (Módulos de Conhecimento) ---


def responder_area():
    """Explica as fórmulas de área."""
    print("\n--- Fórmulas de Área ---")
    print("A área mede a superfície de uma figura.")
    print(" - Área do Quadrado: Lado * Lado (L²)")
    print(" - Área do Triângulo: (Base * Altura) / 2")
    print(" - Área do Círculo: π * raio² (pi vezes o raio ao quadrado)")
    print("------------------------\n")


def responder_perimetro_area():
    """Explica a diferença entre perímetro e área."""
    print("\n--- Perímetro vs. Área ---")
    print(" - Perímetro: É a soma de TODOS os lados de uma figura. É o contorno.")
    print(" - Área: É a medida da superfície interna da figura.")
    print("------------------------\n")


def responder_regras_sinais():
    """Explica as regras de sinais."""
    print("\n--- Regras de Sinais (+ e -) ---")
    print("Para Multiplicação e Divisão:")
    print(" - Sinais iguais resultam em POSITIVO (+). Ex: (-) * (-) = +")
    print(" - Sinais diferentes resultam em NEGATIVO (-). Ex: (+) * (-) = -")
    print("------------------------\n")


def responder_equacao_simples():
    """Explica como resolver uma equação simples (ax+b=c)."""
    print("\n--- Resolvendo Equação Simples (ax + b = c) ---")
    print("O objetivo é isolar o 'x'.")
    print("Exemplo: 2x + 5 = 15")
    print("1. Passe o 'b' (5) para o outro lado, invertendo o sinal: 2x = 15 - 5")
    print("2. Agora você tem: 2x = 10")
    print("3. Passe o 'a' (2) que está multiplicando para o outro lado, dividindo: x = 10 / 2")
    print("4. Resultado: x = 5")
    print("------------------------\n")


def responder_tabuada(numero: int | None = None):
    """Exibe a tabuada para `numero`. Se `numero` for None, pergunta ao usuário."""
    try:
        if numero is None:
            numero_str = input("Qual número você gostaria de ver a tabuada? ")
            numero = int(numero_str)

        print(f"\n--- Tabuada do {numero} ---")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
        print("------------------------\n")
    except ValueError:
        print("\nOps! Isso não parece ser um número válido. Tente novamente.\n")


def responder_ordem_operacoes():
    """Explica a ordem das operações (PEMDAS)."""
    print("\n--- Ordem das Operações (PEMDAS) ---")
    print("A ordem correta para resolver expressões é:")
    print("1. P - Parênteses ()")
    print("2. E - Expoentes (potências) e Raízes")
    print("3. M/D - Multiplicação e Divisão (da esquerda para a direita)")
    print("4. A/S - Adição e Subtração (da esquerda para a direita)")
    print("------------------------\n")


def responder_fracao():
    """Explica o que é uma fração."""
    print("\n--- O que é uma Fração? ---")
    print("Uma fração representa uma parte de um todo. Ela tem um Numerador (em cima) e um Denominador (embaixo).")
    print("Ex: 3/4 significa 3 partes de algo que foi dividido em 4 partes iguais.")
    print("------------------------\n")


def responder_fracao_decimal():
    """Explica como converter fração em decimal."""
    print("\n--- Converter Fração em Decimal ---")
    print("Para converter, simplesmente divida o Numerador (o número de cima) pelo Denominador (o número de baixo).")
    print("Exemplo: 3/4  =>  3 ÷ 4 = 0.75")
    print("------------------------\n")


def responder_fracao_decimal_com_valor(numerador: int, denominador: int):
    """Converte a fração numerador/denominador em decimal e exibe o resultado."""
    try:
        if denominador == 0:
            print("\nErro: denominador não pode ser zero.\n")
            return
        resultado = numerador / denominador
        print(f"\n--- Conversão de Fração ---")
        print(f"A fração {numerador}/{denominador} = {resultado}")
        print("------------------------\n")
    except Exception:
        print("\nOps! Não foi possível converter a fração. Verifique os valores.\n")


def calcular_area_quadrado(lado: float):
    area = lado * lado
    print("\n--- Área do Quadrado ---")
    print(f"Lado = {lado} -> Área = {area}")
    print("------------------------\n")


def calcular_area_triangulo(base: float, altura: float):
    area = (base * altura) / 2
    print("\n--- Área do Triângulo ---")
    print(f"Base = {base}, Altura = {altura} -> Área = {area}")
    print("------------------------\n")


def calcular_area_circulo(raio: float):
    import math
    area = math.pi * (raio ** 2)
    print("\n--- Área do Círculo ---")
    print(f"Raio = {raio} -> Área = {area:.4f}")
    print("------------------------\n")


# Avaliador simples e seguro de expressões aritméticas usando ast
_OPERATORS = {
    ast.Add: _operator.add,
    ast.Sub: _operator.sub,
    ast.Mult: _operator.mul,
    ast.Div: _operator.truediv,
    ast.Pow: _operator.pow,
    ast.USub: _operator.neg,
}


def _eval_ast(node):
    if isinstance(node, ast.Constant):  # python3.8+: ast.Num replaced by Constant
        return node.value
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.BinOp):
        left = _eval_ast(node.left)
        right = _eval_ast(node.right)
        op_type = type(node.op)
        if op_type in _OPERATORS:
            return _OPERATORS[op_type](left, right)
    if isinstance(node, ast.UnaryOp):
        operand = _eval_ast(node.operand)
        op_type = type(node.op)
        if op_type in _OPERATORS:
            return _OPERATORS[op_type](operand)
    raise ValueError('Operação não permitida')


def avaliar_expressao(expr: str):
    """Avalia com segurança uma expressão aritmética simples e imprime o resultado."""
    try:
        expr_clean = expr.replace('^', '**')
        # Remove palavras como 'quanto é' para tentar avaliar só a expressão
        expr_clean = re.sub(r'[^0-9\.\+\-\*\/\^\(\) ]', '', expr_clean)
        parsed = ast.parse(expr_clean, mode='eval')
        result = _eval_ast(parsed.body)
        print(f"\n--- Avaliação de Expressão ---")
        print(f"{expr.strip()} = {result}")
        print("(Lembre-se: prioridade de operações aplicada)")
        print("------------------------\n")
    except Exception:
        print("\nNão foi possível avaliar a expressão. Use sintaxe matemática válida.\n")


def resolver_equacao_simples_com_extracao(entrada: str):
    """Tenta extrair e resolver uma equação do tipo ax + b = c onde a, b e c são inteiros."""
    # Remove espaços para facilitar a regex
    compact = entrada.replace(' ', '')
    # Regex para formas como '2x+5=15' ou '-3x-2=4'
    m = re.search(r'([+-]?\d+)x([+-]?\d+)?=([+-]?\d+)', compact)
    if not m:
        print("\nNão consegui identificar uma equação no formato ax+b=c.\n")
        return
    try:
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else 0
        c = int(m.group(3))
        x = (c - b) / a
        print("\n--- Resolvendo Equação ---")
        print(f"Equação: {a}x + ({b}) = {c}")
        print(f"Solução: x = (c - b) / a = ({c} - {b}) / {a} = {x}")
        print("------------------------\n")
    except Exception:
        print("\nErro ao resolver a equação. Verifique o formato ou os valores.\n")


def responder_desconhecido():
    """Resposta padrão para comandos não reconhecidos."""
    print("\nDesculpe, não entendi. Por favor, escolha um tópico do menu ou digite 'sair'.\n")

# --- Processamento (Roteador Lógico) ---


def processar_entrada(entrada_usuario: str):
    """
    Analisa a entrada do usuário e chama a função de resposta apropriada.
    """
    # Normaliza a entrada para facilitar a comparação
    entrada_normalizada = entrada_usuario.lower().strip()

    # Estrutura de decisão com base em palavras-chave
    # Detectar equação simples no formato ax+b=c
    if re.search(r'\d+x', entrada_normalizada) and '=' in entrada_normalizada:
        resolver_equacao_simples_com_extracao(entrada_normalizada)
        return

    # Detectar fração na forma 'a/b' e converter
    frac_match = re.search(r'(\d+)\s*/\s*(\d+)', entrada_normalizada)
    if frac_match and ("converter" in entrada_normalizada or "decimal" in entrada_normalizada or entrada_normalizada.count('/') == 1):
        numerador = int(frac_match.group(1))
        denominador = int(frac_match.group(2))
        responder_fracao_decimal_com_valor(numerador, denominador)
        return

    # Detectar expressão aritmética simples (contém dígitos e operadores)
    if re.search(r'[0-9] *[\+\-\*\/\^] *[0-9]', entrada_normalizada):
        avaliar_expressao(entrada_normalizada)
        return

    # Detectar pedidos de cálculo de área com valores: quadrado, triangulo, circulo
    # Ex: 'area quadrado 4' ou 'area do circulo 2'
    area_quad = re.search(
        r'area[^0-9]*(quadrad|quadrado)[^0-9]*(\d+(?:\.\d+)?)', entrada_normalizada)
    if area_quad:
        lado = float(area_quad.group(2))
        calcular_area_quadrado(lado)
        return
    area_tri = re.search(
        r'area[^0-9]*(triangul|triângul|triangulo)[^0-9]*(\d+(?:\.\d+)?)[^0-9]*(\d+(?:\.\d+)?)', entrada_normalizada)
    if area_tri:
        base = float(area_tri.group(2))
        altura = float(area_tri.group(3))
        calcular_area_triangulo(base, altura)
        return
    area_circ = re.search(
        r'area[^0-9]*(circul|círcul)[^0-9]*(\d+(?:\.\d+)?)', entrada_normalizada)
    if area_circ:
        raio = float(area_circ.group(2))
        calcular_area_circulo(raio)
        return

    # Estrutura de decisão com base em palavras-chave
    if "area" in entrada_normalizada or entrada_normalizada == "1":
        # Verifica se o usuário não está sendo mais específico
        if "perimetro" in entrada_normalizada:
            responder_perimetro_area()
        else:
            responder_area()
    elif "perimetro" in entrada_normalizada or entrada_normalizada == "2":
        responder_perimetro_area()
    elif "sinal" in entrada_normalizada or "sinais" in entrada_normalizada or entrada_normalizada == "3":
        responder_regras_sinais()
    elif "equacao" in entrada_normalizada or "equação" in entrada_normalizada or entrada_normalizada == "4":
        responder_equacao_simples()
    # Reconhecimento de 'tabuada' com possível número embutido (ex: 'tabuada do 5' ou 'tabuada 7')
    elif "tabuada" in entrada_normalizada or entrada_normalizada == "5":
        # Tenta extrair um número após a palavra 'tabuada'
        match = re.search(r"tabuada[^0-9\n]*(\d+)", entrada_normalizada)
        if match:
            numero_extraido = int(match.group(1))
            responder_tabuada(numero_extraido)
        else:
            responder_tabuada()
    elif "ordem" in entrada_normalizada or "operacoes" in entrada_normalizada or "operações" in entrada_normalizada or entrada_normalizada == "6":
        responder_ordem_operacoes()
    elif "document" in entrada_normalizada or "documentacao" in entrada_normalizada or entrada_normalizada == "9":
        exibir_documentacao()
    elif ("fracao" in entrada_normalizada and "decimal" in entrada_normalizada) or ("fração" in entrada_normalizada and "decimal" in entrada_normalizada) or entrada_normalizada == "8":
        responder_fracao_decimal()
    elif "fracao" in entrada_normalizada or "fração" in entrada_normalizada or entrada_normalizada == "7":
        responder_fracao()
    elif "menu" in entrada_normalizada:
        exibir_menu()
    else:
        responder_desconhecido()

# --- Estrutura Principal (Menu e Loop) ---


def exibir_menu():
    """Apresenta o menu de opções para o usuário."""
    print("\nOlá! Sou seu tutor de Matemática Básica.")
    print("Sobre o que você gostaria de aprender hoje?")
    print("\n--- TÓPICOS ---")
    print(" 1. Fórmulas de Área")
    print(" 2. Diferença entre Perímetro e Área")
    print(" 3. Regras de Sinais")
    print(" 4. Resolver Equação simples")
    print(" 5. Ver a Tabuada")
    print(" 6. Ordem das Operações (PEMDAS)")
    print(" 7. O que é uma Fração")
    print(" 8. Converter Fração em Decimal")
    print(" 9. Documentação do Sistema")
    print("\nDigite o número, uma palavra-chave (ex: 'area') ou 'sair' para terminar.")


def exibir_documentacao():
    """Exibe a documentação completa do sistema e informações da atividade."""
    print("\n=== DOCUMENTAÇÃO: Chatbot Educacional de Matemática Básica ===\n")
    print("Visão geral:")
    print("Este programa é um chatbot educacional por regras desenvolvido como ATIVIDADE AVALIATIVA para a disciplina de Inteligência Artificial.")
    print("Ele responde a consultas sobre conceitos básicos de matemática, fornece fórmulas e realiza pequenos cálculos quando valores são fornecidos.")
    print("\nIdentificação da atividade:")
    print(" - Disciplina: Inteligência Artificial")
    print(" - Curso: Engenharia da Computação")
    print(" - Professor(a): Ionara")
    print(" - Local: São Luís, MA")
    print(" - Ano: 2025")
    print(" - Tipo: Atividade Avaliativa")
    print("\nComponentes (autores):")
    print(" - Vinícius Oliveira")
    print(" - Luys Arthur Serejo")
    print(" - Henzo Lucas")
    print(" - Ryan Reis")
    print("\nComo usar o chatbot:")
    print("1. Inicie o script: python chatbot_matematica.py")
    print("2. O menu principal será exibido com tópicos numerados.")
    print("3. Você pode digitar: o número do tópico (ex: 1), uma palavra-chave (ex: 'area', 'tabuada'), ou frases naturais.")
    print("4. Exemplos de frases aceitas:")
    print("   - '1' ou 'area' -> mostra fórmulas de área")
    print("   - 'quero ver a tabuada do 5' ou 'tabuada 7' -> mostra tabuada sem pedir valor adicional")
    print("   - 'converter 3/4' ou '3/4' -> converte fração para decimal")
    print("   - '2x+5=15' -> resolve equação simples do tipo ax+b=c")
    print("   - 'quanto é 3 + 4 * 2' -> avalia expressão aritmética (respeita prioridade)")
    print("   - 'area quadrado 4' -> calcula área do quadrado com lado 4")
    print("   - 'area triangulo 3 4' -> calcula área do triângulo com base 3 e altura 4")
    print("   - 'area circulo 2' -> calcula área do círculo com raio 2")
    print("\nComportamento interativo e segurança:")
    print(" - Quando um valor estiver embutido na pergunta, o bot tenta extrair o número automaticamente e retorna a resposta sem perguntar novamente.")
    print(" - Avaliação de expressões usa um parser seguro (AST) para evitar execução arbitrária de código.")
    print(" - Caso o bot não entenda, digite 'menu' para ver as opções ou reformule a pergunta.")
    print("\nLimitações e notas técnicas:")
    print(" - O roteador usa regras e expressões regulares; entradas muito ambíguas podem não ser reconhecidas.")
    print(" - Suporte a números por extenso (ex: 'cinco') não está implementado por padrão.")
    print(" - Equações suportadas são do tipo linear simples (ax+b=c) com coeficientes inteiros.")
    print(" - Avaliador aritmético suporta +, -, *, /, ^ (potência) e parênteses.")
    print("\nSugestões de melhoria:")
    print(" - Adicionar reconhecimento de números por extenso e mais padrões de linguagem natural.")
    print(" - Integrar um pequeno modelo de NLP para intent classification, caso queira ampliar a atividade.")
    print(" - Implementar testes automatizados para as funções principais.")
    print("\nContato e autoria:")
    print("Este trabalho foi desenvolvido por Vinícius Oliveira, Luys Arthur Serejo, Henzo Lucas e Ryan Reis para a disciplina indicada.")
    print("\n================ FIM DA DOCUMENTAÇÃO ================\n")


def main():
    """Função principal que executa o chatbot."""
    exibir_menu()

    # Loop principal para manter o bot ativo
    while True:
        # Captura a entrada do usuário
        entrada = input("\n> Sua dúvida: ")

        # Condição de saída
        if entrada.lower().strip() == 'sair':
            print("\nAté a próxima! Bons estudos!")
            break

        # Processa a entrada para dar a resposta
        processar_entrada(entrada)
        print("Posso ajudar com algo mais? (Digite 'menu' para ver as opções)")


# --- Ponto de Entrada do Script ---
# Garante que a função main() só será executada quando o script for rodado diretamente
if __name__ == "__main__":
    main()
