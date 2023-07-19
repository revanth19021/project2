import time
from time import sleep
from sinchsms import SinchSMS

#function for sending sms
def sendsms():
    number='6281569584'
    app_key=''
    app_secret=''

    #enter the message to send

    message='hello raa'
    client=SinchSMS(app_key,app_secret)
    print("sending '%s' to '%s' "%(message,number))

    response=client.send_message(number,message)
    message_id=response['messageId']
    response=client.check_status(message_id)

    while response['status']!='successful':
        print(response['status'])
        time.sleep(1)
        response=client.check_status(message_id)
    print(response['status'])
if __name__ =="__main__":
    sendsms()
