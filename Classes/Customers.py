class Customers:

    def __init__(self, CustomerID, CompanyName, ContactName, ContactTitle, Address, City,
                 Region, PostalCode, Country, Phone, Fax):
        self.CustomerID = CustomerID
        self.CompanyName= CompanyName
        self.ContactName = ContactName
        self.ContactTitle= ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country =Country
        self.Phone = Phone
        self.Fax = Fax

    def persist(self):
        pass


    @staticmethod
    def parse():
        pass

