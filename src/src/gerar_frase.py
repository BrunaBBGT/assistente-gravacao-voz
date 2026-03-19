📌 Arquivo 1 — src/gerar_frase.py
Add file → Create new file

Nome: src/gerar_frase.py

from gtts import gTTS

def gerar_frase():
    texto = "A experiência do cliente é vida"
    audio = gTTS(text=texto, lang="pt", slow=False)
    audio.save("frase_cliente_vida.wav")
    print("✔️ Áudio gerado: frase_cliente_vida.wav")
