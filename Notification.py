from Constante import *
import subprocess

class Mail:


    def consultaPowershell(self,consulta):
        comando_ps =f''' {consulta}'''
        resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
        print(resultado.stdout)
        print(resultado.stderr)
        

    def sendEmail(self,ticket):
        self.consultaPowershell(f'''
                       $SMTPServer = "{SERVER}"
                       $SMTPPort ={PORT}
                       $Username = "{EMAIL}"
                       $Password = "{PASSWORD}"
                       $From = "{EMAIL}"
                       $To = "{TO}"
                       $Subject = "Cambio de estado en el ticket {ticket}"
                       $Body = "{ticket} recibio una respuesta de un cliente"

                       # Crear las credenciales
                       $SecurePassword = ConvertTo-SecureString $Password -AsPlainText -Force
                       $Credential = New-Object System.Management.Automation.PSCredential($Username, $SecurePassword)

                       # Enviar el correo
                       Send-MailMessage -SmtpServer $SMTPServer -Port $SMTPPort -Credential $Credential -From $From -To $To -Subject $Subject -Body $Body -UseSsl
                       
                       ''')    
        
        