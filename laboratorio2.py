#Laboratorio 1 Redes De Computadores
#Profesor Carlos Gonzalez
#Ayudantes Maximiliano Perez - Pablo Reyes
#Alumno Joaquin Ignacio Villagra Pacheco

import numpy as np
from numpy import linspace, arange
from scipy.io.wavfile import read, write
from scipy.fftpack import fft
from scipy.fftpack import ifft
import matplotlib.pyplot as plt

#1. Importe la señal de audio utilizando la función read de scipy.
#2. Mostrar el espectrograma de la función, explicarlo.
#3. Sobre el audio en su dominio de la frecuencia:
####a. Aplique filtro FIR, probar distintos parámetros.
####b. Calcule la transformada de fourier inversa del resultado, compare con la señal original.
####c. Mostrar espectrograma, luego de aplicar el filtro.
#4. Utilizando la función write, guarde los audios del audio filtrado.

"""
setNewRangeData FUNCTION: DETERMINA EL NUEVO CONJUNTO DE DATOS A GRAFICAR.
ENTRADA
	# channel:  data array
	# nameExit: Output file name
SALIDA: #NONE
"""
def drawSpecgram(channel, nameExit="Data Specgram"):
	Im = plt.specgram(y, NFFT=512, Fs=44100)
	plt.xlim(0, len(y) / 44100.0)
	plt.ylim(0, 22050.0)
	plt.colorbar(Im).set_label(u'Intensidad (dB)')
	plt.xlabel(u'Tiempo (s)')
	plt.ylabel(u'Frecuencia (Hz)')
	plt.savefig(nameExit+".png")
	plt.show()

#CUERPO DEL PROGRAMA
#Importando señal con función read
rate, information = read("beacon.wav")
#Mostrando Espectrograma
drawSpecgram(information)