import serial,time,random,requests

def send_sms(smsdata):
    print("started...")

    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

    def send_command(command):
        ser.write((command + '\r\n').encode('utf-8'))
        time.sleep(1)
        response = ser.read_all().decode('utf-8')
        print(f"Command: {command}\nResponse: {response}")
        return response
    send_command('ATZ')
    send_command('AT+CMGF=1')
    send_command('AT+CPMS="ME","SM","ME"')
    send_command('AT+CSCA="+998901850488"')
    send_command('AT+CMGS="%s"' % smsdata['phone'])
    send_command(smsdata['message'] + chr(26))
    time.sleep(1)  # Adjust as needed
    req=requests.delete("http://127.0.0.1:8000/api/v1/sms/?username=%2B998900500902&password=Ss20010806")
    print("finished...")
    ser.close()

while True:
    data={}
    req=requests.get("http://127.0.0.1:8000/api/v1/sms/?username=%2B998900500902&password=Ss20010806")
    data=req.json()
    if data:
        send_sms(data)
    time.sleep(3)
# bu