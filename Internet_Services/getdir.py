import ftplib

connect = ftplib.FTP("www.example.com")
connect.login("user", "pwd")
data = []
connect.dir(data.append)
connect.quit()
for line in data:
	print(line)

