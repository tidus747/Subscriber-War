<img width="320" src="https://www.raspberrypi.org/app/uploads/2017/06/Powered-by-Raspberry-Pi-Logo_Outline-Colour-Screen-500x153.png" align="right" />

Subscriber War Pi
===
Subscriber War Pi es un contador de suscriptores e *YouTube* en tiempo real escrito en Python.

Para hacer que funcione, asegurate de que tienes instalado en tu Raspberry Pi Python y además una [API key registrada para Youtube](https://developers.google.com/youtube/android/player/register), coloca dicha clave en un fichero llamado "apiKey.txt" e introduce el siguiente comando en un terminal:  
```
./subWar.py
```  

Cambiar de usuario para realizar el seguimiento es simple, simplemente usa la función:  
```
addUser(<NAME TO DISPLAY>,<CHANNEL ID>)
```

## Referencias

- [Aplicación original Subscriber War](https://github.com/faissaloo/Subscriber-War)
- [Utilidades para Raspberry Pi](https://github.com/tidus747/Utilidades_RaspberryPi)
