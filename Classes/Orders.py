class Orders:


    def __init__(self, OrderID, CustomerID, EmployeeID, ContactTitle, OrderDate, RequiredDate, ShippedDate, ShipVia,
                 Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID =  EmployeeID
        self.ContactTitle = ContactTitle
        self.OrderDate = OrderDate
        self.RequiredDate = RequiredDate
        self.ShippedDate = ShippedDate
        self.ShipVia = ShipVia
        self.Freight = Freight
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion
        self.ShipPostalCode = ShipPostalCode
        self.ShipCountry = ShipCountry


    def persist(self):
        pass


    @staticmethod
    def parse():
        pass