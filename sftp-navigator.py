import paramiko

class FTP():

    # Initialize variables
    def __init__(self):
        self.sftp_host = ''
        self.sftp_port = 22
        self.sftp_user = ''
        self.sftp_password = ''
       
       
    def sftp_connect(self):

        sftp_client = paramiko.SSHClient()

        sftp_client.load_system_host_keys()


        # Attempt to build a transport

        try:


            sftp_transport = paramiko.Transport((self.sftp_host, int(self.sftp_port)))


        except Exception as e:


            return logging.error(e)

        

        # Attempt connection to sftp

        try:

            sftp_transport.connect(username=self.sftp_user, password=self.sftp_password)

            print("sFTP Connection Established")

        except Exception as e:

            return e

    
        ftp_connection = paramiko.SFTPClient.from_transport(sftp_transport)


        return ftp_connection


    def get_current_dir(self, ftp_connection):

        try: 

            current_directory = ftp_connection.getcwd()

            return current_directory

        except Exception as e:

            return e

    def list_directories(self, ftp_connection):

        try: 

            directories = ftp_connection.listdir()

            return directories

        except Exception as e:

            return e

    def change_directory(self, ftp_connection, directory):
    
        try: 

            new_directory = ftp_connection.chdir(directory)

            return new_directory

        except Exception as e:

            return e

    def list_all(self, ftp_connection):

        try:

            all_files = ftp_connection.listdir()

            return all_files

        except Exception as e:

            return e
