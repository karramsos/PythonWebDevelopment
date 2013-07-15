import ftplib
import sys

filename = sys.argv[1]
connect = ftplib.FTP("www.example.com")
connect.login("user", "pwd")
file = open(filename, "rb")
connect.storbinary("STOR " + filename, file)
connect.quit()
