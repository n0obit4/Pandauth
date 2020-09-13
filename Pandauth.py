import pandas,xlrd
from getpass import getpass
class auth:
    def __init__(self,username,password):
        file = pandas.read_excel('db.xls', sheet_name='Sheet1')
        self.db = file.index
        self.file = file
        self.username = username
        self.password = password

    def presentar(self):
        Username = self.file['Username']
        Password = self.file['Password']
        for i in self.db:
            if self.username == Username[i]:
                if self.password == Password[i]:
                    print("\nWelcome")
                    print(f"Username: {self.username} & Password: {self.password}")
                else:
                    print("Auth error")

if __name__ == "__main__":
    username = input("Username: ")
    password = getpass("Password: ")
    datos = auth(username,password)
    datos.presentar()
