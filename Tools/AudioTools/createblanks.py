import soundfile as sf
import numpy as np

def create_silence_files(namebase="BLANK_AudioFile.wav", number_of_files=0, samplerate=48000, duracion=1, channels=1, format=".wav", num_digits=1):
    silence = np.zeros(((samplerate * duracion), channels))
    # crea un archivo en silencio de {duracion} segundos, {channels} canales y con {samplerate} de freq de muestreo
    if number_of_files == 0:
        counter = ""
        name = f"{namebase}{counter}{format}"
        sf.write(name, silence, samplerate)
    else:
        for counter in range(1, number_of_files + 1):
            print("counter", counter)
            counter_str = str(counter).zfill(num_digits)
            name = f"{namebase}{counter_str}{format}"
            sf.write(name, silence, samplerate)

# Ejemplo de uso
create_silence_files("BLANK_", 3, 48000, 2, 1, ".wav",num_digits=4)
