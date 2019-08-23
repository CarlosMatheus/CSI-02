from SOAPpy import SOAPProxy

server = SOAPProxy('http://localhost:8081/')

while True:
    temperature = int(raw_input('Temperature: '))
    scale = raw_input('F or C: ')
    new_temperature = server.convert(temperature, scale)
    print("Response: " + str(new_temperature.temperature) + " " + new_temperature.scale)
