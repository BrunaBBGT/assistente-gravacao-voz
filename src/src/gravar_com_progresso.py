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
