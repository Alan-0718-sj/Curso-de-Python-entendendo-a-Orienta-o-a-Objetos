

# def cria_conta(numero, titular, saldo, limite):
#     conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
#     return conta

# def deposita(conta, valor):
#     conta["saldo"] += valor

# def saca(conta, valor):
#     conta["saldo"] -= valor

# def extrato(conta):
#     print("Saldo é {}".format(conta["saldo"]))

import numpy as np
import cv2
VIDEO = 'C:\\Users\\Alans\\Obs\\2023-08-10 16-37-06.mp4'
cap = cv2.VideoCapture(VIDEO)
cap