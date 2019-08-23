from SOAPpy import SOAPServer
from pprint import pprint


def convert(temperature, scale):
        if scale == "C":
                response = {
                        "temperature": 9.0/5.0 * temperature + 32,
                        "scale": "F"
                }
        else:
                response = {
                        "temperature": (temperature - 32) * 5.0/9.0,
                        "scale": "C"
                }
        pprint(response)
        return response


server = SOAPServer(('localhost', 8081))
server.registerFunction(convert)
server.serve_forever()
