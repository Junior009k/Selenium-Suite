def cifrado_cesar_personalizado(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        elif caracter.isdigit():
            # Cifrado de números del 0 al 9
            resultado += chr((ord(caracter) - ord('0') + desplazamiento) % 10 + ord('0'))
        elif caracter == '+':
            # Cifrado del asterisco: lo cambia por otro carácter específico (ejemplo simple)
            resultado +="*"
        else:
            # Mantener cualquier otro carácter igual
            resultado += caracter

    return resultado

def desencriptar(texto_encriptado, clave):
    # Inverso para números y letras; el asterisco se maneja con inversión de los signos también
    return cifrado_cesar_personalizado(texto_encriptado, -clave)

# Ejemplo de uso
mensaje = "Sydesys*2025$"
clave = 4

#mensaje_encriptado = encriptar(mensaje, clave)
mensaje_desencriptado = desencriptar("Wchiwcw+6469$", clave)

print("Mensaje desencriptado:", mensaje_desencriptado)
