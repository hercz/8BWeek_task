import mysql.connector


database_connector = mysql.connector.connect(user='codecooler', password = 'Nehezjelszo2%',
                                            host = "127.0.0.1")

cursor = database_connector.cursor()
cursor.execute("USE SANDBOX;")

class Orders:

    def persist(self):
        print(("INSERT INTO Orders VALUES ({},'{}',{},'{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}');".format(self.OrderID,
                                                                self.CustomerID, self.EmployeeID,
                                                                self.OrderDate, self.RequiredDate,
                                                                self.ShippedDate, self.ShipVia, self.Freight, self.ShipName,
                                                                self.ShipAddress, self.ShipCity, self.ShipRegion,
                                                                self.ShipPostalCode, self.ShipCountry)))


        cursor.execute("""INSERT INTO Orders (OrderID, CustomerID,EmployeeID,OrderDate,RequiredDate,ShippedDate,
                          ShipVia,Freight,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry) VALUES
                          ({},'{}',{},'{}','{}','{}',{},{},'{}','{}','{}','{}','{}',{});""".format(self.OrderID,
                                                                self.CustomerID, self.EmployeeID,
                                                                self.OrderDate, self.RequiredDate,
                                                                self.ShippedDate, self.ShipVia, self.Freight, self.ShipName,
                                                                self.ShipAddress, self.ShipCity, self.ShipRegion,
                                                                self.ShipPostalCode, self.ShipCountry))
        database_connector.commit()


    @staticmethod
    def parse(row):
        parsed_row = row.split(";")
        orders = Orders()
        orders.OrderID = parsed_row[0]
        orders.CustomerID = parsed_row[1]
        orders.EmployeeID = parsed_row[2]
        orders.ContactTitle = parsed_row[3]
        orders.OrderDate = parsed_row[4]
        orders.RequiredDate = parsed_row[5]
        orders.ShippedDate = parsed_row[6]
        orders.ShipVia = parsed_row[7]
        orders.Freight = parsed_row[8]
        orders.ShipName = parsed_row[9]
        orders.ShipAddress = parsed_row[10]
        orders.ShipCity = parsed_row[11]
        orders.ShipRegion = parsed_row[12]
        orders.ShipPostalCode = parsed_row[13]
        orders.ShipCountry = parsed_row[14]
        return orders

    @staticmethod
    def data_reader(csv_file):
        csv_rows = []
        with open(csv_file, "r", encoding="utf8") as file:
            for row in file:
                csv_rows.append(row)
        return csv_rows

    def caller(self):
        rows = Orders.data_reader("../CSV_FILES/orders.csv")
        for i in range(1, len(rows)):
            orders = Orders.parse(rows[i])
            orders.persist()


k = Orders()
k.caller()
