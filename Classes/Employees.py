import mysql.connector


database_connector = mysql.connector.connect(user='codecooler', password = 'Nehezjelszo2%',
                                            host = "127.0.0.1")

cursor = database_connector.cursor()
cursor.execute("USE SANDBOX;")


class Employees:

    def __init__(self, EmployeeID, LastName, FirstName, Title, TitleOfCourtesy,
                 BirthDate, HireDate, Address, City, Region, PostalCode, Country, HomePhone, Extension, Photo,
                 Notes, ReportsTo, PhotoPath, Salary):
        self.EmployeeID = EmployeeID
        self.LastName = LastName
        self.FirstName = FirstName
        self.Title = Title
        self.TitleOfCourtesy = TitleOfCourtesy
        self.BirthDate = BirthDate
        self.HireDate = HireDate
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.HomePhone = HomePhone
        self.Extension = Extension
        self.Photo = Photo
        self.Notes = Notes
        self.ReportsTo = ReportsTo
        self.PhotoPath = PhotoPath
        self.Salary = Salary


    def persist(self):
        pass


    @staticmethod
    def parse():
        pass