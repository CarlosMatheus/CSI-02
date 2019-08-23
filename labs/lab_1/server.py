from SOAPpy import SOAPServer


def convert(temperature, scale):
        if scale == "F":
                return {
                        "temperature": 9/5 * temperature + 32,
                        "scale": "C"
                }
        else:
                return {
                        "temperature": (temperature - 32) * 5/9,
                        "scale": "F"
                }


server = SOAPServer(('localhost', 8081))
server.registerFunction(convert)
server.serve_forever()
