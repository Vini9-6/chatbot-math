# Chatbot Educacional de Matemática Básica

Este repositório contém um chatbot por regras implementado em Python, desenvolvido como ATIVIDADE AVALIATIVA para a disciplina de Inteligência Artificial.

Autores
- Vinícius Oliveira
- Luys Arthur Serejo
- Henzo Lucas
- Ryan Reis

Identificação da atividade
- Disciplina: Inteligência Artificial
- Curso: Engenharia da Computação
- Professor(a): YONARA COSTA
- Local: São Luís, MA
- Ano: 2025
- Tipo: Atividade Avaliativa

Visão geral
---------
O chatbot oferece explicações e cálculos rápidos sobre conceitos básicos de matemática, tais como fórmulas de área, perímetro, regras de sinais, resolução de equações lineares simples, tabuada, frações e ordem das operações. Ele usa roteamento por regras (if/elif) e expressões regulares para extrair valores embutidos em frases do usuário.

Como usar
--------
1. Abra um terminal (PowerShell no Windows).
2. Navegue até a pasta do projeto:

```powershell
cd "c:\Users\vsouz\OneDrive\Área de Trabalho\chatbot"
```

3. Execute o chatbot:

```powershell
python chatbot_matematica.py
```

4. Exemplos de interações:
- `1` ou `area` → mostra fórmulas de área.
- `quero ver a tabuada do 5` ou `tabuada 7` → mostra a tabuada do número indicado sem pedir valor adicional.
- `converter 3/4` ou `3/4` → converte fração para decimal.
- `2x+5=15` → resolve equação simples do tipo ax+b=c.
- `quanto é 3 + 4 * 2` → avalia expressão aritmética respeitando a ordem de operações.
- `area quadrado 4` → calcula área do quadrado com lado 4.

Funcionalidades técnicas
-----------------------
- Roteador por regras usando `if/elif` e normalização de entrada.
- Extração de valores via regex (tabuada, fração, áreas, equações).
- Avaliação segura de expressões aritméticas usando `ast` (não executa código arbitrário).

Limitações
---------
- Não há suporte a números por extenso (ex: 'cinco').
- Equações suportadas apenas no formato linear simples (ax+b=c).
- O reconhecimento por regex pode falhar em entradas muito ambíguas.

Sugestões de melhoria
-------------------
- Adicionar um modelo simples de NLP para classificar intenções.
- Implementar suporte a números por extenso.
- Adicionar testes automatizados (unittest) para validar o roteador.

Licença e entrega
-----------------
Arquivo entregue como atividade acadêmica.

Contato
-------
Autores: Vinícius Oliveira, Luys Arthur Serejo, Henzo Lucas, Ryan Reis
