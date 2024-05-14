
from asyncio import LimitOverrunError

from imageio import imiter

''' VOZ DE APRESENTAÇÃO '''

'''
import psutil
import pandas as pd
import os
import pyautogui as al
import time
from selenium import webdriver # O navegador
from selenium.webdriver.common.by import By # Achar elementos
from selenium.webdriver.common.keys import Keys # Para digitar no teclado

import pyautogui
#31012023
from selenium.common.exceptions import NoSuchElementException

# para obter o dia da semana atual em português
from datetime import datetime

dias = {0: "Segunda-feira", 1: "Terça-feira", 2: "Quarta-feira", 3: "Quinta-feira", 4: "Sexta-feira", 5: "Sábado", 6: "Domingo"}

dia_semana = datetime.now().weekday()

import speech_recognition as sr
import datetime

def greet():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 13:
        return "Bom dia!"
    elif hour >= 13 and hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

# print(greet())
voz = (greet())

# Ler os dados e repoduz
from datetime import datetime
import pyttsx3


def ler_data_hora():
    agora = datetime.now()
    dia_da_semana = agora.strftime("%A")
    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M:%S")
    mensagem = f"Olá!!! Meu nome é Tatá. {voz}. Estimo que esteja tudo bem contigo, e a sua família. Hoje é {dias[dia_semana]}, {data}, e são {hora} horas. Irei da acesso a sua conta no Alura Bank."
    engine = pyttsx3.init()
    engine.say(mensagem)
    engine.runAndWait()
    
ler_data_hora()
'''


class Conta:

    def pen(msg):
        tam = len(msg) + 4
        print('%' * tam)
        print(f'  {msg}')
        print('%' * tam)

    pen('BEM VINDO(A)! ALURA-BANK')
    print("TIT".center(28, "$"))

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # self.__codigo_banco = "001" # Apagar

    def extrato(self):
        print("saldo de R$ {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor R$ {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def eh_inadimplente(self, cliente):
        cliente

    # def get_saldo(self):
    #     return self.__saldo

    # def get_titular(self):
    #     return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'Nubank':'260', 'BB':'001', 'Caixa':'104', 'Bradesco':'237', 'Itaú':'341'}



# conta = Conta(123, "Nan", 55.5, 1000.0)
# conta2 = Conta2(321, "Marco", 100.0, 1000.0)
# conta3 = Conta(412, "Pedro", 10000.0, 70000.0)