import os
import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import math

TotalPromedio=0
def PIBSIB():
	global TotalPromedio
	
	
	kernelUsado=3
	cropping = False
	x_start, y_start, x_end, y_end = 0, 0, 0, 0
	from tkinter.filedialog import askopenfilename
	filename = askopenfilename()
	archivo=filename
	gelAnalisar=archivo
	im_in = cv2.imread(gelAnalisar, cv2.IMREAD_GRAYSCALE)
	im_in=cv2.bitwise_not(im_in)
	original=im_in
	dimensiones=im_in.shape
	altura=im_in.shape[0]
	base=im_in.shape[1]
	noequ=im_in
	equ = cv2.equalizeHist(im_in)  
	im_in=equ
	ValorKernel=kernelUsado
	kernel = np.ones((ValorKernel,ValorKernel),np.uint8)
	GelInvertido = cv2.bitwise_not(im_in)
	GelInvertidoNoEqu=cv2.bitwise_not(noequ)
	im_in=GelInvertido
	noequ=GelInvertidoNoEqu
	erosion=cv.erode(im_in,kernel,iterations=1)
	erosionNoEqu=cv.erode(noequ,kernel,iterations=1) 
	im_in=erosion
	noequ=erosionNoEqu
	thresh5=im_in
	thresh5NoEqu=noequ
	imgMascara=thresh5 
	imgMascaraNoEqu=thresh5NoEqu
	imgMascaraNoEqu2=thresh5NoEqu
	grafix=[]
	datosPromedio=[]
	datosPromedio.append(0)
	grafix.append(0)  
	grafixNoEqu=[]
	grafixNoEqu.append(0)
	grafixNoEqu2=[]
	grafixNoEqu2.append(0)
	sumaPromedio=0
	contadorPromedio=0
	TamanoMaxGel=base 
	for i in range(TamanoMaxGel):
		maskNoEqu=np.zeros(imgMascaraNoEqu.shape[:2], np.uint8)
		maskNoEqu2=np.zeros(imgMascaraNoEqu2.shape[:2], np.uint8)
		mask = np.zeros(imgMascara.shape[:2], np.uint8) 
		X0=i 
		X0=int(X0)
		X1=X0+1
		for x in range(X0,X1):
			contadorPromedio=contadorPromedio+1
			X0=x
			X1=x+1
			maskNoEqu[0:426, X0:X1] = 255
			maskNoEqu2[0:426, X0:X1] = 255
				
			mask[0:426, X0:X1] = 255 

			masked_imgNoEqu=cv2.bitwise_and(imgMascaraNoEqu,imgMascaraNoEqu,mask=maskNoEqu)
			masked_imgNoEqu2=cv2.bitwise_and(imgMascaraNoEqu2,imgMascaraNoEqu2,mask=maskNoEqu2)
				
			masked_img = cv2.bitwise_and(imgMascara,imgMascara,mask = mask)
			
			hist_fullNoEqu=cv2.calcHist([imgMascaraNoEqu],[0],None,[256],[0,256])
			hist_fullNoEqu2=cv2.calcHist([imgMascaraNoEqu2],[0],None,[256],[0,256])
				
			hist_full = cv2.calcHist([imgMascara],[0],None,[256],[0,256])

			ret2,imgMascaraNoEqu=cv2.threshold(imgMascaraNoEqu,0,255,cv2.THRESH_OTSU)
			ret2,imgMascaraNoEqu2=cv2.threshold(imgMascaraNoEqu2,0,255,cv2.THRESH_OTSU)

			ret2,imgMascara = cv2.threshold(imgMascara,0,255,cv2.THRESH_OTSU)
			hist_maskNoEqu = cv2.calcHist([imgMascaraNoEqu],[0],maskNoEqu,[256],[0,256])
			hist_maskNoEqu2 = cv2.calcHist([imgMascaraNoEqu2],[0],maskNoEqu2,[256],[0,256])
			hist_mask = cv2.calcHist([imgMascara],[0],mask,[256],[0,256])

			grafixNoEqu.append(0)
			grafixNoEqu2.append(0)
			valores=np.empty([1], dtype=float)
			valores=hist_maskNoEqu2[255]

			grafix.append(hist_mask[255])

			sumaPromedio=sumaPromedio+hist_mask[255]
	grafixNoEqu[20]=sumaPromedio/contadorPromedio
	TotalPromedio=sumaPromedio/contadorPromedio
	entry.delete(0,'end')
	entry.insert(0,TotalPromedio)

from tkinter import *
ventana=Tk()
ventana.title("Método")
ventana.geometry("420x100")
lbl=Label(ventana,text="Perfil de Imágenes Basado en Segmentación de Imágenes Binarizadas (PIBSIB)")
lbl.pack()
btn=Button(ventana,text="Imagen", command=PIBSIB)
btn.place(x=50,y=50)
entry=Entry()
entry.place(x=120,y=50)

ventana.mainloop()
