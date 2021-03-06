# python-ftp-navigator
A tool to run through the FTP server throught CLI


Usage in CLI. 

>>>from sftp-navigator import FTP
>>>ftp = FTP()
>>>client = ftp.sftp_connect()
# Navigation
>>>ftp.get_current_dir(client)
>>>ftp.change_directory(client, 'Your Folder')
