#How to tell your OS to send a whatsapp message to a particular number using python code?


a=input("Enter whatsapp number:")
b=input("Enter the text:")
import os
os.system("start Chrome ""wa.me/91"+a+"/?text="+b+"")
