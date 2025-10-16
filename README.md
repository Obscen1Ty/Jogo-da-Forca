# Jogo da Forca em Python 🎮

Este é um jogo da forca simples, desenvolvido em Python.  
O objetivo do jogo é adivinhar a palavra secreta letra por letra antes de completar o boneco da forca.

---

## 📝 Como jogar

1. Execute o arquivo `forca.py` com Python 3:

   ```bash```
   python forca.py


Digite uma letra por vez quando solicitado.

O jogo irá mostrar:

O progresso da palavra com letras acertadas e _ para as não acertadas.

Quantas tentativas restam.

Quais letras já foram tentadas.

O desenho da forca atualizado conforme erros.

Você vence se adivinhar todas as letras antes que as tentativas acabem.

Você perde se errar todas as tentativas e o boneco da forca for completo.

💡 Funcionalidades

Escolhe palavras aleatórias de uma lista.

Mostra o boneco da forca em ASCII.

Valida entrada do usuário (apenas letras válidas).

Mostra letras já tentadas.

Mensagens de vitória e derrota com informações claras.

Limpa a tela a cada rodada para melhor visualização.

🖥️ Exemplo de execução
Bem vindo ao Jogo da Forca

Palavra: _ _ _ _ _ _
Letras já tentadas: 
Tentativas restantes: 6

Digite uma letra: p
✅ Boa! Você acertou uma letra!

⚙️ Tecnologias

Python 3.x

Terminal/Console

📌 Autor

Luiz Farias


---

### **Como adicionar ao GitHub**

1. Salve o arquivo como `README.md` na pasta do projeto.
2. No VS Code, vá em Source Control e faça **Stage + Commit**:
   ```bash
   git add README.md
   git commit -m "Adiciona README do Jogo da Forca"
   git push
