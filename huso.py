import os
import sys
import time
import random
from selenium import webdriver
from tkinter import *

#GUI für Wortauswahl
def button_action():
    global v
    global v2
    global wort
    global alter
    global worteingabe

    if v2.get() == "Jedes Mal zufällig": alter = 1
    elif v2.get() == "10 bis 15": alter = 2
    elif v2.get() == "16 bis 20": alter = 3
    elif v2.get() == "21 bis 30": alter = 4
    elif v2.get() == "31+": alter = 5

    if v.get() == 1: wort = "Zensurensohn"
    elif v.get() == 2: wort = "Schabernack"
    elif v.get() == 3: wort = "Hussarones"
    elif v.get() == 4: wort = "Masterdebattieren"
    elif v.get() == 6: wort = worteingabe.get()

    if v.get() == 6 and wort == '':
        wortlabel.config(text="Schreibe ein Wort in das Eingabefenster")
    else:
        fenster.destroy()

def close():
    sys.exit()

fenster = Tk()
fenster.title("Wähle ein Wort")
fenster.geometry('300x320')
v = IntVar()
v2 = StringVar()
alter = 1
wort = "Zensurensohn"
wörter = [
    ("Zensurensohn", 1),
    ("Schabernack", 2),
    ("Hussarones", 3),
    ("Masterdebattieren", 4),
    ("Eigenes Wort:", 6)
]
alterlist = [
    "Jedes Mal zufällig",
    "10 bis 15",
    "16 bis 20",
    "21 bis 30",
    "31+"
]

alterslabel = Label(fenster, text="Welches Alter soll angegeben werden?")
alterslabel.pack()
alter_menu = OptionMenu(fenster, v2, *alterlist)
alter_menu.pack()
wortlabel = Label(fenster, text="Welches Wort soll angegeben werden?")
wortlabel.pack()
for txt, val in wörter:
    Radiobutton(fenster, text=txt, padx=20, variable=v, value=val).pack()
worteingabe = Entry(fenster)
worteingabe.pack()
ok_btn = Button(fenster, text="Ok", command=button_action, padx=10)
ok_btn.pack(pady=10)
Button(fenster, text="Programm beenden", command=close).pack()
mainloop()

#setup - lädt die Orte für Browser und Eingabefenster
chromedriver_location = os.path.dirname(os.path.abspath(__file__))+'\chromedriver.exe'
chromedriver_location = chromedriver_location.replace('\\', '/')
driver = webdriver.Chrome(chromedriver_location)
alter_field = '//*[@id="463803414"]/option['
wort_field = '463803684'
datenschutz_field = '//*[@id="question-field-483089934"]/fieldset/div/div/div/div/label/span[1]'
submit_field = '//*[@id="patas"]/main/article/section/form/div[2]/button'

#Spammt das Wort in die Umfrage
while True:
    driver.get('https://www.surveymonkey.com/r/7JZRVLJ')
    if alter == 1:
        rand = random.randint(2, 5)
        driver.find_element_by_xpath(alter_field + str(rand) + ']').click()
    else:
        driver.find_element_by_xpath(alter_field + str(alter) + ']').click()
    driver.find_element_by_id(wort_field).send_keys(wort)
    driver.find_element_by_xpath(datenschutz_field).click()
    driver.find_element_by_xpath(submit_field).click()