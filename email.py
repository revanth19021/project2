import smtplib
import ssl
import email


#setup port number and server name

smtp_port= 587                  # Standard secure SMTP port
smtp_server="smtp.gmail.com"    #google smtp server

email_from="revanth200319@gmail.com"
email_to="revanth200319@gmail.com"

pswd="qzquknblabtbaqdn"


#content of meesage

message="Dear friend Please help"

simple_email_context=ssl.create_default_context()

try:
    print("Connecting to server")
    TIE_server=smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from,pswd)
    print('connected to serverr')

    print()
    print(f"sending email to -{email_to}")
    TIE_server.sendmail(email_from,email_to,message)
    print(f"email successfully sent to -{email_to}")

except Exception as e:
    print(e)

finally:
    TIE_server.quit()