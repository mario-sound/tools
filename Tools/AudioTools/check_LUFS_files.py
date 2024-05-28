import os
import glob
import soundfile as sf
import pyloudnorm as pyln
import csv

actual_path = os.getcwd()

def calculate_loudness_for_folder(folder_path):
    # Buscar todos los archivos WAV en la carpeta especificada
    wav_files = glob.glob(os.path.join(folder_path, "*.wav"))
    
    # Abrir archivos para escribir los resultados
    with open('files_loudness.txt', 'w') as txt_file, open('loudness_files.csv', 'w', newline='') as csv_file:
        # Configurar el escritor CSV
        csv_writer = csv.writer(csv_file)
        # Escribir el encabezado en el archivo CSV
        csv_writer.writerow(['Filename', 'Loudness (LUFS)'])
        
        # Procesar cada archivo WAV encontrado
        for wav_file in wav_files:
            data, rate = sf.read(wav_file)  # cargar el archivo de audio
            meter = pyln.Meter(rate)  # crear el medidor BS.1770
            loudness = meter.integrated_loudness(data)  # medir la loudness
            filename = os.path.basename(wav_file)
            loudness_str = f"{filename}\t{loudness:.2f} LUFS"
            
            # Escribir en el archivo .txt
            txt_file.write(loudness_str + '\n')
            
            # Escribir en el archivo .csv
            csv_writer.writerow([filename, f"{loudness:.2f}"])
            print(loudness_str)  # Opcional: imprimir en la consola

# Ejemplo de uso
folder_path = actual_path  # usar la ruta actual
calculate_loudness_for_folder(folder_path)
