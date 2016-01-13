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