#Laboratorio 2 Redes De Computadores
#Profesor Carlos Gonzalez
#Ayudantes Maximiliano Perez - Pablo Reyes
#Alumno Joaquin Ignacio Villagra Pacheco

import scipy.signal as signal
from numpy import arange, linspace, argmax
from scipy import fft, ifft, real
from scipy.io.wavfile import read, write #importamos las bibliotecas
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

"""
readData FUNCTION: OBTIENE LA INFORMACIÓN DEL ARCHIVO DE AUDIO INDICADO.
IN:
	# filename:  name of audio file
OUT: 
	# frecuency: 
	# signal: Information of signal read
"""
def readData(filename="beacon.wav"):
	frecuency, signal = read(filename)
	print("File readed with succes")
	return frecuency, signal

"""
drawSpectrogram VOID FUNCTION: OBTIENE EL ESPECTROGRAMA DEL ARREGLO DE DATOS QUE REPRESENTA LA SEÑAL INGRESADA.
IN:
	# channel:  data array
	# nameExit: Output file name
OUT: 
	#NONE
"""
def drawSpectrogram(signal, frecuency, title="Spectrogram Graphic", nameExit="Origin Data Specgram"):
	plt.specgram(signal, Fs=frecuency)
	plt.title(title)
	plt.xlabel('Time [s]')
	plt.ylabel('Frecuency')
	plt.savefig(nameExit+".png")
	plt.show()

"""
filterFIR FUNCTION: OBTIENE EL ESPECTRO DEL FILTRO FIR, EL QUE LUEGO SERÁ APLICADO A LA SEÑAL A TRABAJAR.
IN:
	# channel:  data array
	# nameExit: Output file name
OUT: 
	#bandFilter: generate band filter
"""
def filterFIR(frecuency):
	n = 60000 					#Filter generate order
	fs = frecuency 				#Audio frecuency
	lowcut = 1889 				#Frecuency Low
	highcut = 1960 				#Frecuency Top
	nyq = 0.5*fs
	low = lowcut/nyq
	high = highcut/nyq
	#A step filter is obtained under
	lowChannel = signal.firwin(n, cutoff = low, window = 'blackmanharris')
	#It yields a high-pass filter
	highChannel = - signal.firwin(n, cutoff = high, window = 'blackmanharris'); 
	#a partir de los filtros paso bajo data_y paso alto se obtiene el filtro paso banda
	highChannel[n/2] = highChannel[n/2] + 1
	bandFilter = - (lowChannel+b)
	bandFilter[n/2] = bandFilter[n/2] + 1
	return bandFilter

"""
audioFilter FUNCTION: FILTRA LA SEÑAL UTILIZANDO EL FILTRO FIR GENERADO ANTERIORMENTE.
					  DIBUJA EL ESPECTROGRAMA DE LA SEÑAL FILTRADA.
IN:
	# signal: dataset of origin signal
	# bandFilter: Filter FIr generate previously 
	# frecuency: frecuency of signal
OUT: 
	#data_y: array data of filtered channel
"""
def audioFilter(signal, bandFilter, frecuency):
	#Filtered of signal
	data_y = lfilter(bandFilter, [1.0],  signal)
	#the total time is obtained
	time = len(signal)/float(frecuency)
	#generate vector of time
	data_x = arange(0,time,1.0/frecuency)
	#draw graphic
	graficar(data_x, data_y,"Filter function graphic",'time [s]', 'Amplitude [dB]')
	#drawSpectrogram
	drawSpectrogram(data_y, frecuency, "Funtion filter Spectrogram")
	return data_y

"""
drawGraphics VOID FUNCTION: GENERA GRAFICA ACORDE A LOS DATOS DE LOS EJES INGRESADOS.
IN:
	# data_x: dataset of axis X
	# data_y: dataset of axis y
	# titlex: title of axis x
	# titley: title of axis y
	# title: title of graphic
OUT: 
	#NONE
"""
def drawGraphics(data_x, data_y, title, titlex, titley):
	#se genera el grafico
	plt.plot(data_x,data_y,"--")
	plt.title(title)
	plt.xlabel(titlex)
	plt.ylabel(titley)
	plt.show()

"""
audioSave VOID FUNCTION: GENERA ARCHIVO DE AUDIO A PARTIR DEL ARREGLO DE DATOS DE LA SEÑAL INGRESADA.
IN:
	# name: file name 
	# data_y:  data array
	# signal: data of signal
	# frecuency: Output file name
OUT: 
	#NONE
"""
def audioSave(name, data_y, signal, frecuency):
	signal[:,0] = data_y
	signal[:,1] = data_y
	write(name, frecuency, signal)

"""
MAIN OF PROGRAM
"""
frecuency, signal = readData()
#generar el espectrograma de funcion no fitrada
drawSpectrogram(signal[:,0], frecuency, "Spectrogram no filtered function")
#create filter FIR
filtro = filterFIR(frecuency)
#the FIR filter is applied to the signal entered
audioFiltered = audioFilter(signal[:,0], filtro, frecuency)
#save filtered out audio
audioSave("audioFiltered.wav", audioFiltered, signal, frecuency)
#save origin audio
audioSave("audioOrigin.wav", signal[:,0], signal, frecuency)


