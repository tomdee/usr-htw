import socket
import sys 
import subprocess
TCP_ADDR = sys.argv[1]
TCP_PORT = 8899
 
PACK_LEN = 11
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(30)
s.connect((TCP_ADDR, TCP_PORT))
 
bytes_data = [0] * PACK_LEN 

while True:
      str_data = s.recv(PACK_LEN) 
      hex_data = str_data.encode('hex')
   
      for n in range(0,PACK_LEN): 
          lower = 2*n
          upper = lower + 2
          bytes_data[n] = int(hex_data[lower:upper],16)
   
 
      humidity = (((bytes_data[6])<<8)+(bytes_data[7]))/10.0
      temp = (((((bytes_data[8])&0x7F)<<8)+(bytes_data[9]))/10.0)
      
      #invert temp if sign bit is set
      if int(bytes_data[8]) & 0x80: 
          temp = -1.0* temp
      
      print("Temp: %s Humidity: %s" % (temp, humidity))
      subprocess.call("curl -sS -i -XPOST 'http://influxdb:8086/write?db=tomdee' --data-binary 'temperature,room=bedroom,location=vicksburg value=%s'" % temp, shell=True)
      subprocess.call("curl -sS -i -XPOST 'http://influxdb:8086/write?db=tomdee' --data-binary 'humidity,room=bedroom,location=vicksburg value=%s'" % humidity, shell=True)
