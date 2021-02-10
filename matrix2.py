# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matrix.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
import tkcalendar
#from tkinter.tkk import *
import psycopg2
import warnings
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog, QInputDialog, QWidget, QFormLayout, QPushButton, QLineEdit, QComboBox, QRadioButton, QButtonGroup, QCalendarWidget

root=Tk()
root.title("Herramienta para la introducción de datos en la DB de las Matrix - For LandBased use only")

# Introducción de los datos
def save_new_monster(self, id, pais, nom_regulador, data_vigor, data_derogada, reglament, mtr_software, mtr_hard, mtr_rollover, mtr_longitud, play_autoplay, play_duració, play_free_games, mny_currency, mny_tokens, hw_defined, hw_interrupcions, rng_confidence_level, rng_criptogràficament_segur, rng_aprovat_previament, sign_sha1, sign_md5, sign_crc16, sign_crc32, sign_checksum, sign_hmac_sha1, sign_altres, min_bet, max_bet, math_min_rtp, math_max_rtp, math_inclos_jackpot, jp_standalone, jp_lap, jp_wap, jp_mystery, jp_max_win, jp_aportació, aw_idioma, aw_limitacions, aw_moneda, aw_etiquetes, cms_casino, cms_jurisdiccional, cms_protocol, cms_comptadors, specs_comentaris):
    conn=psycopg2.connect(dbname="Matrix_DB", user="wiki", password="wiki", host="192.168.1.16", port="5432")
    cursor=conn.cursor()
    query='''INSERT INTO monster(id, pais, nom_regulador, data_vigor, data_derogada, reglament, mtr_software, mtr_hard, mtr_rollover, mtr_longitud, play_autoplay, play_duració, play_free_games, mny_currency, mny_tokens, hw_defined, hw_interrupcions, rng_confidence_level, rng_criptogràficament_segur, rng_aprovat_previament, sign_sha1, sign_md5, sign_crc16, sign_crc32, sign_checksum, sign_hmac_sha1, sign_altres, min_bet, max_bet, math_min_rtp, math_max_rtp, math_inclos_jackpot, jp_standalone, jp_lap, jp_wap, jp_mystery, jp_max_win, jp_aportació, aw_idioma, aw_limitacions, aw_moneda, aw_etiquetes, cms_casino, cms_jurisdiccional, cms_protocol, cms_comptadors, specs_comentaris) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(query, (id, pais, nom_regulador, data_vigor, data_derogada, reglament, mtr_software, mtr_hard, mtr_rollover, mtr_longitud, play_autoplay, play_duració, play_free_games, mny_currency, mny_tokens, hw_defined, hw_interrupcions, rng_confidence_level, rng_criptogràficament_segur, rng_aprovat_previament, sign_sha1, sign_md5, sign_crc16, sign_crc32, sign_checksum, sign_hmac_sha1, sign_altres, min_bet, max_bet, math_min_rtp, math_max_rtp, math_inclos_jackpot, jp_standalone, jp_lap, jp_wap, jp_mystery, jp_max_win, jp_aportació, aw_idioma, aw_limitacions, aw_moneda, aw_etiquetes, cms_casino, cms_jurisdiccional, cms_protocol, cms_comptadors, specs_comentaris))
    QMessageBox.about(self, "Éxito", "Datos introducidos correctamente")
    clear(self)
    conn.commit()
    conn.close()

def update_monster(self, id, pais, nom_regulador, data_vigor, data_derogada, reglament, mtr_software, mtr_hard, mtr_rollover, mtr_longitud, play_autoplay, play_duració, play_free_games, mny_currency, mny_tokens, hw_defined, hw_interrupcions, rng_confidence_level, rng_criptogràficament_segur, rng_aprovat_previament, sign_sha1, sign_md5, sign_crc16, sign_crc32, sign_checksum, sign_hmac_sha1, sign_altres, min_bet, max_bet, math_min_rtp, math_max_rtp, math_inclos_jackpot, jp_standalone, jp_lap, jp_wap, jp_mystery, jp_max_win, jp_aportació, aw_idioma, aw_limitacions, aw_moneda, aw_etiquetes, cms_casino, cms_jurisdiccional, cms_protocol, cms_comptadors, specs_comentaris):
    conn=psycopg2.connect(dbname="Matrix_DB", user="wiki", password="wiki", host="192.168.1.16", port="5432")
    cursor=conn.cursor()
    query='''UPDATE monster SET pais = %s, nom_regulador = %s, data_vigor = %s, data_derogada = %s, reglament = %s, mtr_software = %s, mtr_hard = %s, mtr_rollover = %s, mtr_longitud = %s, play_autoplay = %s, play_duració = %s, play_free_games = %s, mny_currency = %s, mny_tokens = %s, hw_defined = %s, hw_interrupcions = %s, rng_confidence_level = %s, rng_criptogràficament_segur = %s, rng_aprovat_previament = %s, sign_sha1 = %s, sign_md5 = %s, sign_crc16 = %s, sign_crc32 = %s, sign_checksum = %s, sign_hmac_sha1 = %s, sign_altres = %s, min_bet = %s, max_bet = %s, math_min_rtp = %s, math_max_rtp = %s, math_inclos_jackpot = %s, jp_standalone = %s, jp_lap = %s, jp_wap = %s, jp_mystery = %s, jp_max_win = %s, jp_aportació = %s, aw_idioma = %s, aw_limitacions = %s, aw_moneda = %s, aw_etiquetes = %s, cms_casino = %s, cms_jurisdiccional = %s, cms_protocol = %s, cms_comptadors = %s, specs_comentaris = %s WHERE id=%s'''
    cursor.execute(query, (pais, nom_regulador, data_vigor, data_derogada, reglament, mtr_software, mtr_hard, mtr_rollover, mtr_longitud, play_autoplay, play_duració, play_free_games, mny_currency, mny_tokens, hw_defined, hw_interrupcions, rng_confidence_level, rng_criptogràficament_segur, rng_aprovat_previament, sign_sha1, sign_md5, sign_crc16, sign_crc32, sign_checksum, sign_hmac_sha1, sign_altres, min_bet, max_bet, math_min_rtp, math_max_rtp, math_inclos_jackpot, jp_standalone, jp_lap, jp_wap, jp_mystery, jp_max_win, jp_aportació, aw_idioma, aw_limitacions, aw_moneda, aw_etiquetes, cms_casino, cms_jurisdiccional, cms_protocol, cms_comptadors, specs_comentaris, id))
    QMessageBox.about(self, "Éxito", "Datos actualizados correctamente")
    clear(self)
    conn.commit()
    conn.close()

def get_jurisdictions(): #Devuelve todos los datos en la BBDD
    conn=psycopg2.connect(dbname="Matrix_DB", user="wiki", password="wiki", host="192.168.1.16", port="5432")
    cursor=conn.cursor()
    query='''SELECT * FROM monster ORDER BY pais ASC'''
    cursor.execute(query)
    latest = cursor.fetchall()
    conn.close()
    return latest

def get_id(): #Busca la ID con el numero más alto y devuelve esa ID
    conn=psycopg2.connect(dbname="Matrix_DB", user="wiki", password="wiki", host="192.168.1.16", port="5432")
    cursor=conn.cursor()
    query='''SELECT MAX(id) FROM monster'''
    cursor.execute(query)
    numero = cursor.fetchall()
    conn.close()
    return numero[0][0]

def get_id_country(country, reglament): #Devuelve la ID buscando por país y reglamento
    conn=psycopg2.connect(dbname="Matrix_DB", user="wiki", password="wiki", host="192.168.1.16", port="5432")
    cursor=conn.cursor()
    query='''SELECT id FROM monster WHERE pais = %s AND reglament = %s'''
    cursor.execute(query, (country, reglament))
    jur = cursor.fetchall()
    conn.close
    if jur:
        return jur[0][0]
    else:
        return False    
    
def get_data(num): #Devuelve el país asociado a una ID (num)
    conn=psycopg2.connect(dbname="Matrix_DB", user="wiki", password="wiki", host="192.168.1.16", port="5432")
    cursor=conn.cursor()
    query='''SELECT pais FROM monster WHERE id = %s'''
    cursor.execute(query, [num])
    country = cursor.fetchall()
    conn.close()
    if country:
        return country[0][0]
    else:
        return False

def get_info(pais, reglament): #Devuelve toda la información buscando por país y reglamento
    conn=psycopg2.connect(dbname="Matrix_DB", user="wiki", password="wiki", host="192.168.1.16", port="5432")
    cursor=conn.cursor()
    cursor.execute('''SELECT * FROM monster WHERE pais = %s AND reglament = %s''', (pais, reglament))
    info = cursor.fetchall()
    conn.close()
    if info:
        return info
    else:
        return False
  
def set_combo_box(entry, text): #Pone a un combo box el (text) que se le pase si es que tiene esa opcion
    index = entry.findText(text, QtCore.Qt.MatchExactly)
    if index >= 0:
        entry.setCurrentIndex(index)

def clear(self): #Clear de todos los campos
    self.pais.setText("")
    self.nom_regulador.setText("")
    self.data_vigor.setDate(QtCore.QDate.currentDate())
    self.data_derogada.setText("")
    self.reglament.setCurrentIndex(0)
    self.mtr_software.setCurrentIndex(0)
    self.mtr_hard.setCurrentIndex(0)
    self.mtr_rollover.setText("")
    self.mtr_longitud.setText("")
    self.play_autoplay.setText("")
    self.play_duracio.setText("")
    self.play_free_games.setText("")
    self.mny_currency.setText("")
    self.mny_tokens.setText("")
    self.hw_defined.setCurrentIndex(0)
    self.hw_interrupcions.setText("")
    self.rng_confidence_level.setText("")
    self.rng_criptograficament_segur.setCurrentIndex(0)
    self.rng_aprovat_previament.setCurrentIndex(0)
    self.sign_sha1.setCurrentIndex(0)
    self.sign_md5.setCurrentIndex(0)
    self.sign_crc16.setCurrentIndex(0)
    self.sign_crc32.setCurrentIndex(0)
    self.sign_checksum.setCurrentIndex(0)
    self.sign_hmac_sha1.setCurrentIndex(0)
    self.sign_altres.setCurrentIndex(0)
    self.max_bet.setText("")
    self.min_bet.setText("")
    self.math_min_rtp.setText("")
    self.math_max_rtp.setText("")
    self.math_inclos_jackpot.setText("")
    self.jp_standalone.setCurrentIndex(0)
    self.jp_lap.setCurrentIndex(0)
    self.jp_wap.setCurrentIndex(0)
    self.jp_mystery.setCurrentIndex(0)
    self.jp_max_win.setText("")
    self.jp_aportacio.setText("")
    self.aw_idioma.setText("")
    self.aw_limitacions.setText("")
    self.aw_moneda.setText("")
    self.aw_etiquetes.setText("")
    self.cms_casino.setText("")
    self.cms_jurisdiccional.setText("")
    self.cms_protocol.setText("")
    self.cms_contadors.setText("")
    self.specs_comentaris.setText("")
    self.lista.selectionModel().clear()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(872, 592)
        self.buttonAccept = QPushButton(self.tr("Submit"))
        #buttonAccept.setDefault(true)
        #self.buttonReject = QPushButton(self.tr("Reject"))
        #buttonReject.setDefault(true)
        self.buttonSearch = QPushButton(self.tr("Load"))
        self.buttonClear = QPushButton(self.tr("Clear"))
        self.buttonHelp = QPushButton(self.tr("Help"))
        self.buttonBox = QtWidgets.QDialogButtonBox(QtCore.Qt.Horizontal)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(520, 550, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        # self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.addButton(self.buttonAccept, QtWidgets.QDialogButtonBox.ActionRole)
        #self.buttonBox.addButton(self.buttonReject, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.buttonClear, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.buttonSearch, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.buttonHelp, QtWidgets.QDialogButtonBox.ActionRole)
               
    #Regulación
        self.Insert = QtWidgets.QTabWidget(Dialog)
        self.Insert.setGeometry(QtCore.QRect(10, 30, 851, 281))
        self.Insert.setObjectName("Insert")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pais = QtWidgets.QLineEdit(self.tab)
        self.pais.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.pais.setObjectName("pais")
        self.nom_regulador = QtWidgets.QLineEdit(self.tab)
        self.nom_regulador.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.nom_regulador.setObjectName("nom_regulador")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.label_5.setObjectName("label_5")
        self.reglament = QtWidgets.QComboBox(self.tab)
        self.reglament.setGeometry(QtCore.QRect(170, 140, 111, 22))
        self.reglament.setObjectName("reglament")
        self.reglament.addItem("")
        self.reglament.addItem("")
        self.reglament.addItem("")
        self.reglament.addItem("")
        
        ######################
        #self.cal = QCalendarWidget(self.tab)
        #self.cal.move(20,20)
        #self.cal.setGridVisible(True)
        #self.cal.setSelectedDate()
        
        
        #self.data_vigor = QtWidgets.QLabel(self.tab)
        #self.cal.clicked[QtCore.QDate].connect(self.data_vigor.setText(self.cal.selectedDate().toString()))
        
        #date = self.cal.selectedDate()
        #self.data_vigor.setText(date.toString())
        #self.data_vigor.move(20,200)
        
        #self.data_vigor.setGeometry(100,100,300,300)
        #self.setObjectName("data_vigor")
        #############################
        
        self.data_vigor = QtWidgets.QDateEdit(self.tab)
        self.data_vigor.setDate(QtCore.QDate.currentDate())
        self.data_vigor.setGeometry(QtCore.QRect(170, 80, 111, 22))
        self.data_vigor.setObjectName("data_vigor")
        self.data_derogada = QtWidgets.QLineEdit(self.tab)
        self.data_derogada.setMaxLength(8)
        self.data_derogada.setGeometry(QtCore.QRect(170, 110, 113, 20))
        self.data_derogada.setObjectName("data_derogada")
        
    #List View
        self.label_47 = QtWidgets.QLabel(Dialog)
        self.label_47.setGeometry(570, 70, 101, 16)
        self.label_47.setObjectName("label_47")
        self.lista = QtWidgets.QListWidget(Dialog)
        self.lista.setGeometry(570, 100, 256, 192)
        
    #Contadores   
        self.Insert.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 131, 16))
        self.label_9.setObjectName("label_9")
        self.mtr_software = QtWidgets.QComboBox(self.tab_2)
        self.mtr_software.setGeometry(QtCore.QRect(170, 20, 69, 22))
        self.mtr_software.setObjectName("mtr_software")
        self.mtr_software.addItem("")
        self.mtr_software.addItem("")
        self.mtr_software.addItem("")
        self.mtr_hard = QtWidgets.QComboBox(self.tab_2)
        self.mtr_hard.setGeometry(QtCore.QRect(170, 50, 69, 22))
        self.mtr_hard.setObjectName("mtr_hard")
        self.mtr_hard.addItem("")
        self.mtr_hard.addItem("")
        self.mtr_hard.addItem("")
        self.mtr_rollover = QtWidgets.QLineEdit(self.tab_2)
        self.mtr_rollover.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.mtr_rollover.setObjectName("mtr_rollover")
        self.mtr_longitud = QtWidgets.QLineEdit(self.tab_2)
        self.mtr_longitud.setGeometry(QtCore.QRect(170, 110, 113, 20))
        self.mtr_longitud.setObjectName("mtr_longitud")
        self.Insert.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_13.setObjectName("label_13")
        
    #Partidas
        self.play_autoplay = QtWidgets.QLineEdit(self.tab_3)
        self.play_autoplay.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.play_autoplay.setObjectName("play_autoplay")
        self.play_free_games = QtWidgets.QLineEdit(self.tab_3)
        self.play_free_games.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.play_free_games.setObjectName("play_free_games")
        self.play_duracio = QtWidgets.QLineEdit(self.tab_3)
        self.play_duracio.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.play_duracio.setObjectName("play_duracio")
        self.Insert.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_14.setObjectName("label_14")
       
    #Créditos
        self.mny_currency = QtWidgets.QLineEdit(self.tab_4)
        self.mny_currency.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.mny_currency.setObjectName("mny_currency")
        self.mny_tokens = QtWidgets.QLineEdit(self.tab_4)
        self.mny_tokens.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.mny_tokens.setObjectName("mny_tokens")
        self.Insert.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_16.setObjectName("label_16")
        
    #Hardware
        self.hw_interrupcions = QtWidgets.QLineEdit(self.tab_5)
        self.hw_interrupcions.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.hw_interrupcions.setObjectName("hw_interrupcions")
        self.hw_defined = QtWidgets.QComboBox(self.tab_5)
        self.hw_defined.setGeometry(QtCore.QRect(170, 20, 69, 22))
        self.hw_defined.setObjectName("hw_defined")
        self.hw_defined.addItem("")
        self.hw_defined.addItem("")
        self.Insert.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_17 = QtWidgets.QLabel(self.tab_6)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setGeometry(QtCore.QRect(10, 50, 141, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_6)
        self.label_19.setGeometry(QtCore.QRect(10, 80, 141, 16))
        self.label_19.setObjectName("label_19")
        
    #RNG
        self.rng_confidence_level = QtWidgets.QLineEdit(self.tab_6)
        self.rng_confidence_level.setMaxLength(6)
        self.rng_confidence_level.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.rng_confidence_level.setObjectName("rng_confidence_level")
        self.rng_criptograficament_segur = QtWidgets.QComboBox(self.tab_6)
        self.rng_criptograficament_segur.setGeometry(QtCore.QRect(170, 50, 69, 22))
        self.rng_criptograficament_segur.setObjectName("rng_criptograficament_segur")
        self.rng_criptograficament_segur.addItem("")
        self.rng_criptograficament_segur.addItem("")
        self.rng_criptograficament_segur.addItem("")
        self.rng_aprovat_previament = QtWidgets.QComboBox(self.tab_6)
        self.rng_aprovat_previament.setGeometry(QtCore.QRect(170, 80, 69, 22))
        self.rng_aprovat_previament.setObjectName("rng_aprovat_previament")
        self.rng_aprovat_previament.addItem("")
        self.rng_aprovat_previament.addItem("")
        self.rng_aprovat_previament.addItem("")
        self.Insert.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_20 = QtWidgets.QLabel(self.tab_7)
        self.label_20.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_7)
        self.label_21.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_21.setObjectName("label_21")
        
    #Apuestas
        self.max_bet = QtWidgets.QLineEdit(self.tab_7)
        self.max_bet.setMaxLength(10)
        self.max_bet.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.max_bet.setObjectName("max_bet")
        self.min_bet = QtWidgets.QLineEdit(self.tab_7)
        self.min_bet.setMaxLength(10)
        self.min_bet.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.min_bet.setObjectName("min_bet")
        self.Insert.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_22 = QtWidgets.QLabel(self.tab_8)
        self.label_22.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_8)
        self.label_23.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_8)
        self.label_24.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_24.setObjectName("label_24")
        
    #Mates
        self.math_min_rtp = QtWidgets.QLineEdit(self.tab_8)
        self.math_min_rtp.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.math_min_rtp.setObjectName("math_min_rtp")
        self.math_max_rtp = QtWidgets.QLineEdit(self.tab_8)
        self.math_max_rtp.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.math_max_rtp.setObjectName("math_max_rtp")
        self.math_inclos_jackpot = QtWidgets.QLineEdit(self.tab_8)
        self.math_inclos_jackpot.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.math_inclos_jackpot.setObjectName("math_inclos_jackpot")
        self.Insert.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.label_25 = QtWidgets.QLabel(self.tab_9)
        self.label_25.setGeometry(QtCore.QRect(10, 170, 91, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_9)
        self.label_26.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_9)
        self.label_27.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_9)
        self.label_28.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_9)
        self.label_29.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_9)
        self.label_30.setGeometry(QtCore.QRect(10, 140, 130, 13))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_9)
        self.label_31.setGeometry(QtCore.QRect(10, 200, 71, 16))
        self.label_31.setObjectName("label_31")
        
    #Firmas
        self.sign_sha1 = QtWidgets.QComboBox(self.tab_9)
        self.sign_sha1.setGeometry(QtCore.QRect(170, 20, 90, 22))
        self.sign_sha1.setObjectName("sign_sha1")
        self.sign_sha1.addItem("")
        self.sign_sha1.addItem("")
        self.sign_sha1.addItem("")
        self.sign_md5 = QtWidgets.QComboBox(self.tab_9)
        self.sign_md5.setGeometry(QtCore.QRect(170, 50, 90, 22))
        self.sign_md5.setObjectName("sign_md5")
        self.sign_md5.addItem("")
        self.sign_md5.addItem("")
        self.sign_md5.addItem("")
        self.sign_crc16 = QtWidgets.QComboBox(self.tab_9)
        self.sign_crc16.setGeometry(QtCore.QRect(170, 80, 90, 22))
        self.sign_crc16.setObjectName("sign_crc16")
        self.sign_crc16.addItem("")
        self.sign_crc16.addItem("")
        self.sign_crc16.addItem("")
        self.sign_crc32 = QtWidgets.QComboBox(self.tab_9)
        self.sign_crc32.setGeometry(QtCore.QRect(170, 110, 90, 22))
        self.sign_crc32.setObjectName("sign_crc32")
        self.sign_crc32.addItem("")
        self.sign_crc32.addItem("")
        self.sign_crc32.addItem("")
        self.sign_checksum = QtWidgets.QComboBox(self.tab_9)
        self.sign_checksum.setGeometry(QtCore.QRect(170, 140, 90, 22))
        self.sign_checksum.setObjectName("sign_checksum")
        self.sign_checksum.addItem("")
        self.sign_checksum.addItem("")
        self.sign_checksum.addItem("")
        self.sign_hmac_sha1 = QtWidgets.QComboBox(self.tab_9)
        self.sign_hmac_sha1.setGeometry(QtCore.QRect(170, 170, 90, 22))
        self.sign_hmac_sha1.setObjectName("sign_hmac_sha1")
        self.sign_hmac_sha1.addItem("")
        self.sign_hmac_sha1.addItem("")
        self.sign_hmac_sha1.addItem("")
        self.sign_altres = QtWidgets.QComboBox(self.tab_9)
        self.sign_altres.setGeometry(QtCore.QRect(170, 200, 90, 22))
        self.sign_altres.setObjectName("sign_altres")
        self.sign_altres.addItem("")
        self.sign_altres.addItem("")
        self.sign_altres.addItem("")
        self.Insert.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.label_32 = QtWidgets.QLabel(self.tab_10)
        self.label_32.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_10)
        self.label_33.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab_10)
        self.label_34.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab_10)
        self.label_35.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_10)
        self.label_36.setGeometry(QtCore.QRect(10, 140, 91, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab_10)
        self.label_37.setGeometry(QtCore.QRect(10, 170, 131, 16))
        self.label_37.setObjectName("label_37")
        
    #Jackpots
        self.jp_standalone = QtWidgets.QComboBox(self.tab_10)
        self.jp_standalone.setGeometry(QtCore.QRect(170, 20, 90, 22))
        self.jp_standalone.setObjectName("jp_standalone")
        self.jp_standalone.addItem("")
        self.jp_standalone.addItem("")
        self.jp_standalone.addItem("")
        self.jp_lap = QtWidgets.QComboBox(self.tab_10)
        self.jp_lap.setGeometry(QtCore.QRect(170, 50, 90, 22))
        self.jp_lap.setObjectName("jp_lap")
        self.jp_lap.addItem("")
        self.jp_lap.addItem("")
        self.jp_lap.addItem("")
        self.jp_wap = QtWidgets.QComboBox(self.tab_10)
        self.jp_wap.setGeometry(QtCore.QRect(170, 80, 90, 22))
        self.jp_wap.setObjectName("jp_wap")
        self.jp_wap.addItem("")
        self.jp_wap.addItem("")
        self.jp_wap.addItem("")
        self.jp_mystery = QtWidgets.QComboBox(self.tab_10)
        self.jp_mystery.setGeometry(QtCore.QRect(170, 110, 90, 22))
        self.jp_mystery.setObjectName("jp_mystery")
        self.jp_mystery.addItem("")
        self.jp_mystery.addItem("")
        self.jp_mystery.addItem("")
        self.jp_max_win = QtWidgets.QLineEdit(self.tab_10)
        self.jp_max_win.setMaxLength(10)
        self.jp_max_win.setGeometry(QtCore.QRect(170, 140, 113, 20))
        self.jp_max_win.setObjectName("jp_max_win")
        self.jp_aportacio = QtWidgets.QLineEdit(self.tab_10)
        self.jp_aportacio.setMaxLength(10)
        self.jp_aportacio.setGeometry(QtCore.QRect(170, 170, 113, 20))
        self.jp_aportacio.setObjectName("jp_aportacio")
        self.Insert.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.label_38 = QtWidgets.QLabel(self.tab_11)
        self.label_38.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.tab_11)
        self.label_39.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.tab_11)
        self.label_40.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.tab_11)
        self.label_41.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_41.setObjectName("label_41")
        
    #Artwork
        self.aw_idioma = QtWidgets.QLineEdit(self.tab_11)
        self.aw_idioma.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.aw_idioma.setObjectName("aw_idioma")
        self.aw_limitacions = QtWidgets.QLineEdit(self.tab_11)
        self.aw_limitacions.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.aw_limitacions.setObjectName("aw_limitacions")
        self.aw_moneda = QtWidgets.QLineEdit(self.tab_11)
        self.aw_moneda.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.aw_moneda.setObjectName("aw_moneda")
        self.aw_etiquetes = QtWidgets.QLineEdit(self.tab_11)
        self.aw_etiquetes.setGeometry(QtCore.QRect(170, 110, 113, 20))
        self.aw_etiquetes.setObjectName("aw_etiquetes")
        self.Insert.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.label_42 = QtWidgets.QLabel(self.tab_12)
        self.label_42.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.tab_12)
        self.label_43.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.tab_12)
        self.label_44.setGeometry(QtCore.QRect(10, 80, 131, 16))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.tab_12)
        self.label_45.setGeometry(QtCore.QRect(10, 110, 131, 16))
        self.label_45.setObjectName("label_45")
        
    #CMS
        self.cms_casino = QtWidgets.QLineEdit(self.tab_12)
        self.cms_casino.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.cms_casino.setObjectName("cms_casino")
        self.cms_jurisdiccional = QtWidgets.QLineEdit(self.tab_12)
        self.cms_jurisdiccional.setGeometry(QtCore.QRect(170, 50, 113, 20))
        self.cms_jurisdiccional.setObjectName("cms_jurisdiccional")
        self.cms_protocol = QtWidgets.QLineEdit(self.tab_12)
        self.cms_protocol.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.cms_protocol.setObjectName("cms_protocol")
        self.cms_contadors = QtWidgets.QLineEdit(self.tab_12)
        self.cms_contadors.setGeometry(QtCore.QRect(170, 110, 113, 20))
        self.cms_contadors.setObjectName("cms_contadors")
        self.Insert.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.label_46 = QtWidgets.QLabel(self.tab_13)
        self.label_46.setGeometry(QtCore.QRect(10, 20, 241, 16))
        self.label_46.setObjectName("label_46")
        
    #Específicos
        self.specs_comentaris = QtWidgets.QTextEdit(self.tab_13)
        self.specs_comentaris.setGeometry(QtCore.QRect(10, 40, 271, 211))
        self.specs_comentaris.setObjectName("specs_comentaris")
        self.Insert.addTab(self.tab_13, "")
        self.Show_matrix = QtWidgets.QTableWidget(Dialog)
        self.Show_matrix.setGeometry(QtCore.QRect(20, 320, 831, 231))
        self.Show_matrix.setObjectName("Show_matrix")
        self.Show_matrix.setColumnCount(0)
        self.Show_matrix.setRowCount(0)

        self.retranslateUi(Dialog)
        self.Insert.setCurrentIndex(12)
        #self.buttonBox.accepted.connect(Dialog.accept)
        #self.buttonBox.rejected.connect(Dialog.reject)
        self.pushButton = QPushButton("Accept")
        #self.pushButton2.clicked.connect()
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Insert.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Herramienta para la introducción de datos en la DB de las Matrix  - For LandBased use only"))
        
    #Regulación
        self.label.setText(_translate("Dialog", "Pais"))
        self.label_2.setText(_translate("Dialog", "Nombre del Regulador"))
        self.label_3.setText(_translate("Dialog", "Fecha de entrada en vigor"))
        self.label_4.setText(_translate("Dialog", "Fecha de derogación"))
        self.label_5.setText(_translate("Dialog", "Reglamento"))
        #Desplegable
        self.reglament.setItemText(0, _translate("Dialog", "Casino"))
        self.reglament.setItemText(1, _translate("Dialog", "VLT"))
        self.reglament.setItemText(2, _translate("Dialog", "Bingo (class II)"))
        self.reglament.setItemText(3, _translate("Dialog", "AWP (máquina B)"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab), _translate("Dialog", "Regulación"))
        self.label_47.setText(_translate("Dialod", "Available Data"))
        
    #Contadores
        self.label_6.setText(_translate("Dialog", "Contadores por Software"))
        self.label_7.setText(_translate("Dialog", "Contadores por Hardware"))
        self.label_8.setText(_translate("Dialog", "Rollover"))
        self.label_9.setText(_translate("Dialog", "Longitud de los contadores"))
        self.mtr_software.setItemText(0, _translate("Dialog", "Si"))
        self.mtr_software.setItemText(1, _translate("Dialog", "No"))
        self.mtr_software.setItemText(2, _translate("Dialog", "Sin definir"))
        self.mtr_hard.setItemText(0, _translate("Dialog", "Si"))
        self.mtr_hard.setItemText(1, _translate("Dialog", "No"))
        self.mtr_hard.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_2), _translate("Dialog", "Contadores"))
        
    #Partidas
        self.label_10.setText(_translate("Dialog", "Autoplay"))
        self.label_11.setText(_translate("Dialog", "Duración de las partidas"))
        self.label_13.setText(_translate("Dialog", "Free Games"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_3), _translate("Dialog", "Partidas"))
        
    #Créditos
        self.label_12.setText(_translate("Dialog", "Moneda de curso legal"))
        self.label_14.setText(_translate("Dialog", "Tokens (tickets inckuídos)"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_4), _translate("Dialog", "Créditos"))
    
    #Hardware
        self.label_15.setText(_translate("Dialog", "Se menciona en el reglamento"))
        self.label_16.setText(_translate("Dialog", "Interrupciones requeridas"))
        self.hw_defined.setItemText(0, _translate("Dialog", "Si"))
        self.hw_defined.setItemText(1, _translate("Dialog", "No"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_5), _translate("Dialog", "Hardware"))
        
    #RNG
        self.label_17.setText(_translate("Dialog", "Confidence Level"))
        self.label_18.setText(_translate("Dialog", "Criptográficamente seguro?"))
        self.label_19.setText(_translate("Dialog", "RNG aprovado previamente?"))
        self.rng_criptograficament_segur.setItemText(0, _translate("Dialog", "Si"))
        self.rng_criptograficament_segur.setItemText(1, _translate("Dialog", "No"))
        self.rng_criptograficament_segur.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.rng_aprovat_previament.setItemText(0, _translate("Dialog", "Si"))
        self.rng_aprovat_previament.setItemText(1, _translate("Dialog", "No"))
        self.rng_aprovat_previament.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_6), _translate("Dialog", "RNG"))
        
    #Apuestas
        self.label_20.setText(_translate("Dialog", "Max Bet"))
        self.label_21.setText(_translate("Dialog", "Min Bet"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_7), _translate("Dialog", "Apuestas"))
        
    #Mates
        self.label_22.setText(_translate("Dialog", "RTP Mínimo"))
        self.label_23.setText(_translate("Dialog", "RTP Máximo"))
        self.label_24.setText(_translate("Dialog", "Incluye Jackpots"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_8), _translate("Dialog", "Mates"))
        
    #Firmas
        self.label_25.setText(_translate("Dialog", "HMAC-SHA1"))
        self.label_26.setText(_translate("Dialog", "SHA1"))
        self.label_27.setText(_translate("Dialog", "MD5"))
        self.label_28.setText(_translate("Dialog", "CRC16"))
        self.label_29.setText(_translate("Dialog", "CRC32"))
        self.label_30.setText(_translate("Dialog", "Checksum"))
        self.label_31.setText(_translate("Dialog", "Otras firmas"))
        self.sign_sha1.setItemText(0, _translate("Dialog", "Si"))
        self.sign_sha1.setItemText(1, _translate("Dialog", "No"))
        self.sign_sha1.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.sign_md5.setItemText(0, _translate("Dialog", "Si"))
        self.sign_md5.setItemText(1, _translate("Dialog", "No"))
        self.sign_md5.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.sign_crc16.setItemText(0, _translate("Dialog", "Si"))
        self.sign_crc16.setItemText(1, _translate("Dialog", "No"))
        self.sign_crc16.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.sign_crc32.setItemText(0, _translate("Dialog", "Si"))
        self.sign_crc32.setItemText(1, _translate("Dialog", "No"))
        self.sign_crc32.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.sign_checksum.setItemText(0, _translate("Dialog", "Si"))
        self.sign_checksum.setItemText(1, _translate("Dialog", "No"))
        self.sign_checksum.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.sign_hmac_sha1.setItemText(0, _translate("Dialog", "Si"))
        self.sign_hmac_sha1.setItemText(1, _translate("Dialog", "No"))
        self.sign_hmac_sha1.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.sign_altres.setItemText(0, _translate("Dialog", "Si"))
        self.sign_altres.setItemText(1, _translate("Dialog", "No"))
        self.sign_altres.setItemText(2, _translate("Dialog", "Sin Definir"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_9), _translate("Dialog", "Firmas"))
        
    #Jackpots
        self.label_32.setText(_translate("Dialog", "Jackpot Standalone"))
        self.label_33.setText(_translate("Dialog", "LAP"))
        self.label_34.setText(_translate("Dialog", "WAP"))
        self.label_35.setText(_translate("Dialog", "Mystery"))
        self.label_36.setText(_translate("Dialog", "Premio máximo"))
        self.label_37.setText(_translate("Dialog", "Porcentaje de aportación"))
        self.jp_standalone.setItemText(0, _translate("Dialog", "Si"))
        self.jp_standalone.setItemText(1, _translate("Dialog", "No"))
        self.jp_standalone.setItemText(2, _translate("Dialog", "Sin Def."))
        self.jp_lap.setItemText(0, _translate("Dialog", "Si"))
        self.jp_lap.setItemText(1, _translate("Dialog", "No"))
        self.jp_lap.setItemText(2, _translate("Dialog", "Sin Def."))
        self.jp_wap.setItemText(0, _translate("Dialog", "Si"))
        self.jp_wap.setItemText(1, _translate("Dialog", "No"))
        self.jp_wap.setItemText(2, _translate("Dialog", "Sin Def."))
        self.jp_mystery.setItemText(0, _translate("Dialog", "Si"))
        self.jp_mystery.setItemText(1, _translate("Dialog", "No"))
        self.jp_mystery.setItemText(2, _translate("Dialog", "Sin Def."))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_10), _translate("Dialog", "Jackpots"))
        
    #Artwork
        self.label_38.setText(_translate("Dialog", "Idioma del Artwork"))
        self.label_39.setText(_translate("Dialog", "Limitaciones"))
        self.label_40.setText(_translate("Dialog", "Moneda en el HUD"))
        self.label_41.setText(_translate("Dialog", "Etiquetas"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_11), _translate("Dialog", "Artwork"))
        
    #CMS
        self.label_42.setText(_translate("Dialog", "CMS Própio del casino?"))
        self.label_43.setText(_translate("Dialog", "CMS Jurisdiccional"))
        self.label_44.setText(_translate("Dialog", "Protocolos del CMS"))
        self.label_45.setText(_translate("Dialog", "Contadores a pasar al CMS"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_12), _translate("Dialog", "CMS"))
        
    #Específicos
        self.label_46.setText(_translate("Dialog", "Comentarios y otros datos a tener en cuenta"))
        self.Insert.setTabText(self.Insert.indexOf(self.tab_13), _translate("Dialog", "Específicos"))

class MyApp(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Dialog.__init__(self)    
        self.setupUi(self)
        self.show_jurisdictions()
        self.buttonAccept.clicked.connect(self.wasowski)
        self.buttonSearch.clicked.connect(self.buscar_info)
        self.buttonClear.clicked.connect(self.full_clear)
        self.buttonHelp.clicked.connect(self.ayuda)
        
    def wasowski(self): #Mira en BBDD si ya existe el país con ese reglamento, si es así lo actualiza sino crea una nueva entrada
        if get_id_country(self.pais.text(), self.reglament.currentText()): 
            reply = QMessageBox.question(self, "Alerta", "¿Estas seguro que quieres sobreescribir los datos en la base de datos?", QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                update_monster(self, get_id_country(self.pais.text(), self.reglament.currentText()), self.pais.text(), self.nom_regulador.text(), self.data_vigor.text(), self.data_derogada.text(), self.reglament.currentText(), self.mtr_software.currentText(), self.mtr_hard.currentText(), self.mtr_rollover.text(), self.mtr_longitud.text(), self.play_autoplay.text(), self.play_duracio.text(), self.play_free_games.text(), self.mny_currency.text(), self.mny_tokens.text(), self.hw_defined.currentText(), self.hw_interrupcions.text(), self.rng_confidence_level.text(), self.rng_criptograficament_segur.currentText(), self.rng_aprovat_previament.currentText(), self.sign_sha1.currentText(), self.sign_md5.currentText(), self.sign_crc16.currentText(), self.sign_crc32.currentText(), self.sign_checksum.currentText(), self.sign_hmac_sha1.currentText(), self.sign_altres.currentText(), self.min_bet.text(), self.max_bet.text(), self.math_min_rtp.text(), self.math_max_rtp.text(), self.math_inclos_jackpot.text(), self.jp_standalone.currentText(), self.jp_lap.currentText(), self.jp_wap.currentText(), self.jp_mystery.currentText(), self.jp_max_win.text(), self.jp_aportacio.text(), self.aw_idioma.text(), self.aw_limitacions.text(), self.aw_moneda.text(), self.aw_etiquetes.text(), self.cms_casino.text(), self.cms_jurisdiccional.text(), self.cms_protocol.text(), self.cms_contadors.text(), self.specs_comentaris.toPlainText())
        else:
            save_new_monster(self, get_id()+1, self.pais.text(),self.nom_regulador.text(), self.data_vigor.text(), self.data_derogada.text(), self.reglament.currentText(), self.mtr_software.currentText(), self.mtr_hard.currentText(), self.mtr_rollover.text(), self.mtr_longitud.text(), self.play_autoplay.text(), self.play_duracio.text(), self.play_free_games.text(), self.mny_currency.text(), self.mny_tokens.text(), self.hw_defined.currentText(), self.hw_interrupcions.text(), self.rng_confidence_level.text(), self.rng_criptograficament_segur.currentText(), self.rng_aprovat_previament.currentText(), self.sign_sha1.currentText(), self.sign_md5.currentText(), self.sign_crc16.currentText(), self.sign_crc32.currentText(), self.sign_checksum.currentText(), self.sign_hmac_sha1.currentText(), self.sign_altres.currentText(), self.min_bet.text(), self.max_bet.text(), self.math_min_rtp.text(), self.math_max_rtp.text(), self.math_inclos_jackpot.text(), self.jp_standalone.currentText(), self.jp_lap.currentText(), self.jp_wap.currentText(), self.jp_mystery.currentText(), self.jp_max_win.text(), self.jp_aportacio.text(), self.aw_idioma.text(), self.aw_limitacions.text(), self.aw_moneda.text(), self.aw_etiquetes.text(), self.cms_casino.text(), self.cms_jurisdiccional.text(), self.cms_protocol.text(), self.cms_contadors.text(), self.specs_comentaris.toPlainText())
        self.show_jurisdictions()
        
    def buscar_info(self): #Busca en la BBDD la jurisdiccion que se haya puesto en el campo País y el reglamento tambien. A continuacion introduce toda la información en sus respectivos campos
        if self.lista.currentItem() != None: #Si se ha seleccionado algo de la lista de jurisdicciones la carga, sino busca por lo introducido en país
            tmp_text = self.lista.currentItem().text().split("-")
            tmp_text[0] = tmp_text[0][:-1]
            tmp_text[1] = tmp_text[1][1:]
            pais_text = tmp_text[0]
            reg_text = tmp_text[1]
        else:
            pais_text = self.pais.text()
            reg_text = self.reglament.currentText()
        if get_info(pais_text, reg_text):
            info = get_info(pais_text, reg_text)
            self.pais.setText(info[0][1])
            self.nom_regulador.setText(info[0][2])
            self.data_vigor.setDate(info[0][3])
            self.data_derogada.setText(info[0][4])
            set_combo_box(self.reglament, info[0][5])
            set_combo_box(self.mtr_software, info[0][6])
            set_combo_box(self.mtr_hard, info[0][7])
            self.mtr_rollover.setText(info[0][8])
            self.mtr_longitud.setText(info[0][9])
            self.play_autoplay.setText(info[0][10])
            self.play_duracio.setText(info[0][11])
            self.play_free_games.setText(info[0][12])
            self.mny_currency.setText(info[0][13])
            self.mny_tokens.setText(info[0][14])
            set_combo_box(self.hw_defined, info[0][15])
            self.hw_interrupcions.setText(info[0][16])
            self.rng_confidence_level.setText(info[0][17])
            set_combo_box(self.rng_criptograficament_segur, info[0][18])
            set_combo_box(self.rng_aprovat_previament, info[0][19])
            set_combo_box(self.sign_sha1, info[0][20])
            set_combo_box(self.sign_md5, info[0][21])
            set_combo_box(self.sign_crc16, info[0][22])
            set_combo_box(self.sign_crc32, info[0][23])
            set_combo_box(self.sign_checksum, info[0][24])
            set_combo_box(self.sign_hmac_sha1, info[0][25])
            set_combo_box(self.sign_altres, info[0][26])
            self.min_bet.setText(info[0][27])
            self.max_bet.setText(info[0][28])
            self.math_min_rtp.setText(info[0][29])
            self.math_max_rtp.setText(info[0][30])
            self.math_inclos_jackpot.setText(info[0][31])
            set_combo_box(self.jp_standalone, info[0][32])
            set_combo_box(self.jp_lap, info[0][33])
            set_combo_box(self.jp_wap, info[0][34])
            set_combo_box(self.jp_mystery, info[0][35])
            self.jp_max_win.setText(info[0][36])
            self.jp_aportacio.setText(info[0][37])
            self.aw_idioma.setText(info[0][38])
            self.aw_limitacions.setText(info[0][39])
            self.aw_moneda.setText(info[0][40])
            self.aw_etiquetes.setText(info[0][41])
            self.cms_casino.setText(info[0][42])
            self.cms_jurisdiccional.setText(info[0][43])
            self.cms_protocol.setText(info[0][44])
            self.cms_contadors.setText(info[0][45])
            self.specs_comentaris.setText(info[0][46])
        else:
            QMessageBox.about(self, "Error", "Jurisdicción no encontrada")          
    
    def full_clear(self): #Pone todos los campos vacios (o en default)
        reply = QMessageBox.question(self, "Alerta", "¿Estas seguro que quieres limpiar todos los campos?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            clear(self)
    
    def show_jurisdictions(self): #Añade a la lista las ultimas entradas actualizadas
        self.lista.clear()
        info = get_jurisdictions()
        for i in info:
            item = QtWidgets.QListWidgetItem(i[1] + " - " + i[5])
            self.lista.addItem(item)
    
    def ayuda(self): #Muestra pantalla de ayuda
        QMessageBox.about(self, "Help", '''
--------------------[[ Cómo introducir/actualizar datos ]]--------------------
Rellenar todos los campos de los que se tengan datos y pulsar "Submit"

Recomendación: Si lo que se quiere es actualizar información, es recomendable hacer 
un "Load" primero para obtener los datos que tiene la base de datos.

---------------------------------[[ Clear ]]-----------------------------------
Vacía todos los campos o los pone en default si son desplegables. También quita la 
seleccion de la lista.

    - Si la has liado mucho piensa: ¿Que haria Jesus? Y recuerda que matarlos a 
        todos para empezar de zero es una opción.

----------------------------[[ Cómo cargar datos ]]-----------------------------
Para cargar una jurisdiccion se debe seleccionar en la lista de datos la jurisdiccion 
deseada o escribir el Pais y seleccionar el Reglamento deseados, a continuacion pulsar "Load".
        
        
        
                                    Para más información contactar con: 
                                        - nicolas.riquelme@bmm.com
                                        - marti.salvador@bmm.com
                                    
                                    Y para todo lo demás, MasterCard.
        ''')
    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()  
    #timer = QTimer()
    #timer.timeout.connect(window.updateTime)
    #timer.start(10000)
    window.show()
    sys.exit(app.exec_())
