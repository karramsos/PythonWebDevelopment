import ftplib
import sys

filename = sys.argv[1]
connect = ftplib.FTP("www.example.com")
connect.login("user", "pwd")
connect.retrlines("RETR " + filename)
connect.quit()
