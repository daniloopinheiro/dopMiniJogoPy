# 🎮 DOP Mini Jogo Python - Pedra, Papel e Tesoura

Um jogo interativo de Pedra, Papel e Tesoura desenvolvido em Python com interface colorida no terminal. Este projeto é um excelente exercício de programação que demonstra o uso de condicionais, loops e bibliotecas para criar uma experiência visual atrativa.

## 📋 Visão Geral

Este é um jogo clássico de Pedra, Papel e Tesoura (Rock, Paper, Scissors) implementado em Python, que oferece:

- 🎨 **Interface colorida no terminal** usando bibliotecas especializadas
- 🖥️ **Arte ASCII estilizada** com pyfiglet
- 🎯 **Jogo contra o computador** com escolhas aleatórias
- 📊 **Placar em tempo real** durante as partidas
- 🔄 **Sistema de loops** para múltiplas rodadas
- ⚡ **Lógica condicional** clara e educativa

### Tecnologias Utilizadas

- **Python 3.x**
- **termcolor** - Para colorir texto no terminal
- **pyfiglet** - Para criar arte ASCII estilizada
- **colorama** - Para compatibilidade de cores cross-platform

## 📦 Instalação

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema:

```bash
python --version
```

### ⚠️ IMPORTANTE: Instalação das Dependências

**ATENÇÃO:** É obrigatório instalar as bibliotecas necessárias antes de executar o jogo!

Execute um dos seguintes comandos para instalar todas as dependências:

**Opção 1 - Usando requirements.txt (Recomendado):**
```bash
pip install -r requirements.txt
```

**Opção 2 - Instalação manual:**
```bash
pip install termcolor pyfiglet colorama
```

Ou, se você estiver usando Python 3 especificamente:

```bash
pip3 install -r requirements.txt
# ou
pip3 install termcolor pyfiglet colorama
```

### Instalação Alternativa

Para instalar cada biblioteca individualmente:

```bash
# Para cores no terminal
pip install termcolor

# Para arte ASCII
pip install pyfiglet

# Para compatibilidade de cores
pip install colorama
```

## 🚀 Como Usar

### Executando o Jogo

Após instalar as dependências, execute o jogo com o comando:

```bash
python app.py
```

### Como Jogar

1. **Execute o comando** `python app.py`
2. **Escolha sua jogada** digitando:
   - `rock` ou `pedra` para Pedra 🪨
   - `paper` ou `papel` para Papel 📄
   - `scissors` ou `tesoura` para Tesoura ✂️
3. **Veja o resultado** da rodada com cores vibrantes
4. **Acompanhe o placar** atualizado em tempo real
5. **Continue jogando** ou saia quando desejar

### Exemplo de Uso

```bash
$ python app.py

🎮 BEM-VINDO AO JOGO PEDRA, PAPEL E TESOURA! 🎮

Placar Atual: Você 0 x 0 Computador

Digite sua escolha (rock/paper/scissors ou pedra/papel/tesoura):
> rock

🪨 Você escolheu: PEDRA
🤖 Computador escolheu: PAPEL

📄 PAPEL cobre PEDRA 🪨
💻 Computador venceu esta rodada!

Placar Atualizado: Você 0 x 1 Computador

Deseja jogar novamente? (s/n):
```

## 🎨 Funcionalidades

### Interface Colorida
- Textos em cores vibrantes usando `termcolor`
- Títulos estilizados com `pyfiglet`
- Compatibilidade cross-platform com `colorama`

### Lógica do Jogo
- **Condicionais** para determinar vencedor
- **Loops** para múltiplas partidas
- **Entrada do usuário** com validação
- **Geração aleatória** para jogadas do computador

### Sistema de Pontuação
- Placar em tempo real
- Histórico de vitórias
- Estatísticas da sessão

## 🛠️ Estrutura do Projeto

```
dopMiniJogoPy/
│
├── app.py              # Arquivo principal do jogo
├── requirements.txt    # Lista de dependências
└── README.md           # Documentação do projeto
```

## 🎯 Conceitos de Programação Demonstrados

Este projeto é excelente para aprender:

- **Estruturas Condicionais (if/elif/else)**
- **Loops (while/for)**
- **Funções e modularização**
- **Manipulação de strings**
- **Importação de bibliotecas**
- **Entrada e saída de dados**
- **Lógica de programação**

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError"
Se você receber um erro como `ModuleNotFoundError: No module named 'termcolor'`, significa que as dependências não estão instaladas. Execute:

```bash
pip install termcolor pyfiglet colorama
```

### Cores não aparecem no Windows
Se as cores não aparecerem no Windows, certifique-se de que `colorama` está instalado:

```bash
pip install colorama
```

### Python não encontrado
Verifique se Python está instalado e no PATH do sistema:

```bash
python --version
# ou
python3 --version
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar o código existente
- Aprimorar a documentação

## 📞 Contato

Para dúvidas, sugestões ou colaborações:

- **Autor:** Danilo Pinheiro
- **Repository:** [dopMiniJogoPy](https://github.com/daniloopinheiro/dopMiniJogoPy)
- **Issues:** Para reportar problemas ou sugerir melhorias, utilize a seção [Issues](https://github.com/daniloopinheiro/dopMiniJogoPy/issues) do GitHub

## 📄 Licença

Este projeto é open source e está disponível sob a licença MIT.

---

**🎮 Divirta-se jogando e aprendendo Python! 🐍**

> **Lembre-se:** Sempre instale as dependências antes de executar o jogo para garantir o funcionamento correto de todas as funcionalidades visuais e interativas!