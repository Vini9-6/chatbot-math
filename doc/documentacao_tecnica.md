# Documentação Técnica — Chatbot Educacional de Matemática Básica

Autor(es): Vinícius Oliveira, Luys Arthur Serejo, Henzo Lucas, Ryan Reis
Disciplina: Inteligência Artificial — Engenharia da Computação
Professor(a): Ionara — São Luís, MA — 2025

---

## Resumo

Este documento descreve, de forma técnica, o desenvolvimento, a arquitetura e o funcionamento do "Chatbot Educacional de Matemática Básica" — um sistema baseado em regras criado para a revisão de conceitos matemáticos elementares. O objetivo é servir tanto como documento de apoio para avaliação quanto como material de apresentação da atividade.

## Objetivos do sistema

- Fornecer explicações didáticas sobre temas de matemática básica (área, perímetro, regras de sinais, frações, equações lineares simples, tabuada, ordem das operações).
- Permitir interação por texto em console, aceitando tanto comandos simples (números do menu) quanto frases naturais que contenham valores e expressões.
- Demonstrar técnicas elementares de processamento de linguagem natural por regras (normalização e regex) e avaliação segura de expressões aritméticas.

## Arquitetura geral

O sistema é implementado em um único arquivo Python `chatbot_matematica.py`, organizado em blocos funcionais:

1. Módulos de conhecimento — funções de resposta que contêm explicações ou cálculos.
2. Processamento (roteador) — função `processar_entrada` que normaliza a entrada e utiliza uma sequência de checagens (regex + palavras-chave) para decidir qual módulo invocar.
3. Estrutura principal — interface de console (`exibir_menu`, `main`) que roda um loop `while True` recebendo entradas via `input()`.
4. Utilitários — avaliador de expressões seguro (baseado em `ast`) e funções de extração para frações, equações e áreas.

A escolha por arquitetura monolítica em um arquivo se justifica pelo escopo de atividade acadêmica e pela necessidade de simplicidade para demonstração em sala.

## Fluxo de execução

1. Ao executar o script, `main()` chama `exibir_menu()` e entra em loop aguardando entradas do usuário.
2. Cada entrada é passada para `processar_entrada`, que aplica as seguintes etapas:
   - Normalização (lowercase e strip).
   - Detecta padrões com prioridade (equações, frações com valores, expressões aritméticas, pedidos de área com valores, tabuada com número embutido).
   - Se nenhum padrão específico é detectado, realiza verificação por palavras-chave (ex.: "area", "tabuada", "fracao", "menu").
   - Chama a função de resposta correspondente.
3. A função de resposta imprime a explicação/cálculo no console.
4. O loop continua até o usuário digitar `sair`.

## Módulos e componentes principais

### 1) Funções de resposta
- `responder_area()`, `responder_perimetro_area()`, `responder_regras_sinais()`, `responder_equacao_simples()`, `responder_tabuada(numero=None)`, `responder_ordem_operacoes()`, `responder_fracao()`, `responder_fracao_decimal()`.
- Versões auxiliares: `responder_fracao_decimal_com_valor(numerador, denominador)` para conversão direta quando a fração está embutida na entrada.

### 2) Roteador: `processar_entrada(entrada_usuario)`
- Usa `re` para identificar padrões:
  - Equações do tipo `ax+b=c` (regex simplificada: `([+-]?\d+)x([+-]?\d+)?=([+-]?\d+)`).
  - Frações `a/b` (regex: `(\d+)\s*/\s*(\d+)`).
  - Expressões aritméticas simples (detecta operadores entre dígitos).
  - Pedidos de áreas com valores (quadrado, triângulo, círculo) com captura de números.
  - Tabuada com número embutido (`tabuada[^0-9]*(\d+)`).
- Chamadas às funções de resposta conforme correspondência.

### 3) Avaliador seguro de expressões
- Implementado com `ast.parse(..., mode='eval')` e uma função recursiva `_eval_ast` que só aceita nós AST seguros: `BinOp`, `UnaryOp`, `Num`/`Constant` e operadores aritméticos básicos (+, -, *, /, pow).
- O avaliador rejeita execução arbitrária (não chama `eval` nem executa código proveniente do usuário).

## Design de regex e decisões de correspondência

- As regex foram mantidas propositadamente simples para cobrir casos didáticos. Exemplo: para equações assumimos coeficientes inteiros e formato próximo a `2x+5=15`.
- Para áreas, são aceitos padrões como "area quadrado 4", "area triangulo 3 4" (base e altura) e "area circulo 2".
- A detecção de expressões aritméticas busca por operação entre dígitos; entradas muito verbosas podem ser filtradas antes de avaliação (o sistema remove caracteres não numéricos/operadores para tentar extrair uma expressão).

## Segurança

- A principal preocupação é evitar execução arbitrária de código. Por isso:
  - A avaliação de expressões usa `ast` com whitelist de operadores.
  - Não há execução de funções do sistema com base em entrada do usuário.

## Limitações conhecidas

- Reconhecimento limitado a padrões simples; frases ambíguas podem não ser interpretadas corretamente.
- Não há tratamento sofisticado de linguagem natural (tokenização, stemming, análise semântica).
- Números por extenso ("cinco") não são reconhecidos.
- Equações aceitas têm formato simples; não há suporte para equações com parênteses, denominadores ou variáveis diferentes de `x`.

## Testes e validação

- Recomenda-se testes manuais interativos (exemplos no `README.md`) para validar fluxos de uso.
- Para testes automatizados, sugerimos criar uma suíte `unittest` que invoque `processar_entrada` com entradas não interativas (mockando `input()` quando necessário) e verifique saídas (capturando `stdout`).

## Roteiro para apresentação (sugestão)

1. Introdução rápida (30s): propósito e contexto acadêmico da atividade.
2. Arquitetura (1min): explicar organização em módulos e o fluxo `main` → `processar_entrada` → funções de resposta.
3. Demonstração (3-5min): executar o script e mostrar exemplos:
   - Mostrar menu.
   - `quero ver a tabuada do 5` → sem prompt adicional.
   - `converter 3/4` → conversão direta.
   - `2x+5=15` → resolução da equação.
   - `quanto é 3 + 4 * 2` → avaliação com prioridade correta.
4. Segurança e limitações (1min): explicar uso de `ast` e restrições das regex.
5. Encerramento e melhorias futuras (30s).

## Possíveis melhorias futuras

- Integrar uma biblioteca de NLP leve (spaCy, Rasa ou similar) para classificação de intenções e melhor extração de entidades.
- Suporte a números por extenso e pluralizações/variações linguísticas.
- Modularizar em pacotes: separar roteador, módulos de conhecimento e utilitários em arquivos separados para facilitar testes.
- Criar testes unitários e pipeline CI.

---

**Fim da documentação técnica**
