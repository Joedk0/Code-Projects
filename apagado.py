import os

shutdown = input("apagar pc? (si / no)")

if shutdown.lower() == "no":
    print("Igual vamos a apagar la pc aj")
    os.system("shutdown /s /t 1")
    
    
else:
    os.systema("shutdown /s /t 1")
