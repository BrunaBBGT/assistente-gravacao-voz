# assistente-gravacao-voz
# 🎤 Assistente de Gravação de Voz com Barra de Progresso

Este projeto demonstra como:

- Gerar automaticamente um áudio dizendo **"A experiência do cliente é vida"**
- Gravar a voz do usuário
- Exibir uma barra de progresso durante a gravação
- Salvar os arquivos de áudio localmente

Tudo feito em Python, de forma simples e direta.

---

## 📦 Instalação

### 1. Clonar o repositório

Se você quiser usar este projeto localmente, basta clonar:

```bash
git clone https://github.com/BrunaBBGT/assistente-gravacao-voz.git
cd assistente-gravacao-voz
2. Instalar as dependências
pip install -r requirements.txt
Como executar
python src/main.py
Funcionalidades
✔ Geração automática de áudio com gTTS

✔ Gravação de voz com barra de progresso

✔ Código simples e fácil de entender

✔ Compatível com Windows, Linux e macOS

📁 Estrutura
src/
├── gerar_frase.py          # Gera o áudio com a frase
├── gravar_com_progresso.py # Grava áudio com barra de progresso
└── main.py                 # Arquivo principal

📜 Licença
MIT License

4. Role a página para baixo e clique em **“Commit changes”** (ou “Commit changes to main”).

Pronto: o README já está bonito no seu repositório.

---

### 2. Criar o arquivo `requirements.txt` pelo GitHub

1. No repositório, clique em **Add file** → **Create new file**.  
2. No campo de nome do arquivo, escreva: `requirements.txt`  
3. Cole isso dentro:

```txt
sounddevice
scipy
gTTS

3. Criar a pasta src e os arquivos de código
3.1. Arquivo src/gerar_frase.py
Clique em Add file → Create new file.

No nome do arquivo, escreva: src/gerar_frase.py

Cole:
from gtts import gTTS

def gerar_frase():
    texto = "A experiência do cliente é vida"
    audio = gTTS(text=texto, lang="pt", slow=False)
    audio.save("frase_cliente_vida.wav")
    print("✔️ Áudio gerado: frase_cliente_vida.wav")
3.2. Arquivo src/gravar_com_progresso.py
De novo: Add file → Create new file.

Nome: src/gravar_com_progresso.py

Cole:

python
import sounddevice as sd
from scipy.io.wavfile import write
import time
import sys

def gravar_com_progresso(arquivo="gravacao.wav", duracao=5, taxa=44100):
    print("\n🎙️ Iniciando gravação da sua voz...")

    audio = sd.rec(int(duracao * taxa), samplerate=taxa, channels=1)

    for i in range(duracao):
        barra = "█" * (i + 1) + "-" * (duracao - i - 1)
        sys.stdout.write(f"\rGravando: [{barra}] {i+1}/{duracao}s")
        sys.stdout.flush()
        time.sleep(1)

    sd.wait()
    write(arquivo, taxa, audio)

    print(f"\n✔️ Gravação concluída e salva como {arquivo}")
Clique em Commit new file.

3.3. Arquivo src/main.py
De novo: Add file → Create new file.

Nome: src/main.py

Cole:

python
from gerar_frase import gerar_frase
from gravar_com_progresso import gravar_com_progresso

def main():
    gerar_frase()
    gravar_com_progresso()

if __name__ == "__main__":
    main()
Clique em Commit new file.
