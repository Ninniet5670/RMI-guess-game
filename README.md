# Jogo de Adivinhação Multiusuário
**Objetivo do Jogo:** O objetivo é adivinhar um número secreto gerado
aleatoriamente pelo servidor. Este número está entre 1 e 100, inclusive.
**Como Jogar:**

- O servidor gera um número aleatório entre 1 e 100 no início de cada novo jogo.
- Os jogadores, através de seus clientes, tentam adivinhar o número enviando um palpite para o servidor.
- O servidor responde com "Alto" se o palpite for maior que o número secreto, "Baixo" se o palpite for menor que o número secreto, e "Correto" se o palpite for igual ao número secreto.
- Quando um jogador acerta o número, o servidor automaticamente inicia
- um novo jogo gerando um novo número secreto.

**Regras:**

1. Cada jogador pode fazer uma tentativa de adivinhação por vez, enviando
um número entre 1 e 100.
2. Não há limite de tentativas, mas os jogadores são encorajados a usar o
mínimo possível de tentativas para adivinhar o número.
3. O jogo suporta múltiplos jogadores simultaneamente. Cada jogador
compete para ser o primeiro a adivinhar o número correto.
4. Assim que o número é adivinhado corretamente, o servidor informa todos
os jogadores que o jogo terminou e um novo número é gerado para
começar outro jogo.
5. O jogador que acertar o número é anunciado vencedor daquela rodada.
6. Jogadores podem entrar ou sair do jogo a qualquer momento.

**Finalização:**
• Os jogadores podem sair do jogo a qualquer momento digitando um
comando específico (por exemplo, "-1").
• O servidor continua em execução, aguardando novas conexões ou jogadas
até ser manualmente encerrado.
Considerações Técnicas:
• Utilize RMI para implementar a comunicação entre o cliente e o servidor.
• O servidor deve ser capaz de manejar múltiplas conexões de cliente
simultaneamente sem interrupção.
• Garanta que o servidor trate exceções apropriadamente para evitar que ele
se torne inacessível.

<hr>

Para rodar, basta:
```
python -m venv venv
./venv/Scripts/activate.ps1
!pip install Pyro4
python -m Pyro4.naming
python server.py
python client.py
```