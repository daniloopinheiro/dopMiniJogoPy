# dopMiniJogoPy Game

Jogo interativo de pedra, papel e tesoura desenvolvido em Python com interface colorida no terminal.  
Um bom exercício para praticar decisões condicionais, iterações e uso de módulos Python.

## 📑 Índice

1. [Visão Geral](#visão-geral)
2. [Instalação](#instalação)
3. [Como Usar](#como-usar)
4. [Configuração](#configuração)
5. [Contribuições](#contribuições)
6. [Artigos & Conteúdos](#artigos--conteúdos)
7. [Licença](#licença)
8. [Contato](#contato)

---

## Visão Geral

O jogo de pedra, papel e tesoura é um jogo manual no qual cada jogador escolhe um dos três itens. Do ponto de vista da programação, esse desafio é um bom exercício para praticar decisões condicionais, iterações e uso de módulos do Python.

**Funcionalidades principais:**
- Interface colorida com ASCII art
- Placar em tempo real
- Validação de entrada do usuário
- Opção de jogar múltiplas rodadas

**Regras do jogo:**
- Pedra vence Tesoura
- Tesoura vence Papel  
- Papel vence Pedra

---

## Instalação

### Pré-requisitos
- Python 3.6 ou superior

### Clonando o repositório
```bash
$ git clone https://github.com/seu-usuario/rock-paper-scissors-game.git
$ cd rock-paper-scissors-game
```

### Instalação das dependências
**IMPORTANTE**: Instale as bibliotecas necessárias antes de executar o jogo:

```bash
$ pip install termcolor pyfiglet colorama
```

Ou usando requirements.txt (se disponível):
```bash
$ pip install -r requirements.txt
```

---

## Como Usar

Execute o arquivo principal para iniciar o jogo:

```bash
$ python app.py
```

**Como jogar:**
1. O jogo será iniciado com uma apresentação colorida
2. Digite sua escolha: `rock`, `paper` ou `scissors`
3. O computador fará sua escolha automaticamente
4. O resultado da rodada será exibido com o placar atual
5. Escolha se deseja continuar jogando (`yes`) ou sair (`no`)

**Exemplo de execução:**
```
Rock Paper Scissors

Welcome to the Rock, Paper, Scissors game!
You will be playing against the computer.

Enter your choice (rock, paper, scissors): rock
Computer chose: scissors
You win this round!
Score - You: 1 | Computer: 0

Do you want to play again? (yes/no): yes
```

---

## Configuração

O jogo funciona diretamente após a instalação das dependências. Não requer configurações adicionais.

**Dependências utilizadas:**
- `random`: Para escolha aleatória do computador (built-in)
- `sys`: Para saída do programa (built-in)
- `time`: Para delays na apresentação (built-in)
- `os`: Para limpeza da tela (built-in)
- `termcolor`: Para cores no texto
- `pyfiglet`: Para ASCII art
- `colorama`: Para compatibilidade de cores no Windows

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs através das Issues
- Sugerir novas funcionalidades
- Enviar Pull Requests com melhorias
- Melhorar a documentação

**Como contribuir:**
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## Artigos & Conteúdos

* 💼 [LinkedIn](https://www.linkedin.com/in/daniloopinheiro)
* ✍️ [Medium](https://medium.com/@daniloopinheiro)
* 💻 [Dev.to](https://dev.to/daniloopinheiro)

---

## Licença

MIT License © 2025 [dopme.io](https://dopme.io) — por [Danilo O. Pinheiro](https://www.linkedin.com/in/daniloopinheiro/)

---

## Contato

### 💬 Suporte Técnico
Para questões técnicas, problemas ou sugestões:
- **Issues**: [GitHub Issues](https://github.com/daniloopinheiro/rock-paper-scissors-game/issues)
- **Discussions**: [GitHub Discussions](https://github.com/daniloopinheiro/rock-paper-scissors-game/discussions)

### 👨‍💻 Autor
**Danilo O. Pinheiro**  
Especialista em .NET, Clean Architecture e Interoperabilidade em Saúde

- **Email Pessoal**: [daniloopro@gmail.com](mailto:daniloopro@gmail.com)
- **Email Empresarial**: [devsfree@devsfree.com.br](mailto:devsfree@devsfree.com.br)
- **Consultoria**: [contato@dopme.io](mailto:contato@dopme.io)
- **LinkedIn**: [Danilo O. Pinheiro](https://www.linkedin.com/in/daniloopinheiro/)

### 🏢 Empresas
- **[DevsFree](https://devsfree.com.br)**: Desenvolvimento de Software
- **[dopme.io](https://dopme.io)**: Consultoria e Soluções Tecnológicas

---

<div align="center">

**⭐ Se este projeto foi útil, deixe uma estrela no GitHub! ⭐**

<p>
Feito com ❤️ por <strong>Danilo O. Pinheiro</strong><br/>  
<a href="https://devsfree.com.br" target="_blank">DevsFree</a> • <a href="https://dopme.io" target="_blank">dopme.io</a>  
</p>

</div>
