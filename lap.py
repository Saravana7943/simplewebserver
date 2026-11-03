from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
<head>
    <title>MY LAP INFORMATION</title>
</head>

<body bgcolor="BLUE">
    <h1>SARAVANAKUMAR-26011394</h1>

    <table border="1" cellspacing="10" cellpadding="10">

        <tr bgcolor="lightgray">
            <th>S.No</th>
            <th>DEVICE NAME</th>
            <th>PROCESSOR</th>
            <th>INSTALLED RAM</th>
            <th>GRAPHICS CARD</th>
            <th>STORAGE</th>
            <th>DEVICE ID</th>
            <th>PRODUCT ID</th>
            <th>SYSTEM TYPE</th>
            <th>PEN AND TOUCH</th>
        </tr>

        <tr>
            <td>1</td>
            <td>TL15-53M-G2</td>
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
            <td>16.0 GB (15.7 GB usable)</td>
            <td>Intel(R) Graphics (128 MB)</td>
            <td>129 GB of 477 GB used</td>
            <td>12BB29E9-6984-472C-AC48-C80E1AC3CA1F</td>
            <td>12BB29E9-6984-472C-AC48-C80E1AC3CA1F</td>
            <td>64-bit operating system, x64-based processor</td>
            <td>No</td>
        </tr>

    </table>
</body>
</html>

"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running....")
httpd.serve_forever()