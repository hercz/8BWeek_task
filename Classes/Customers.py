import mysql.connector


database_connector = mysql.connector.connect(user='codecooler', password = 'Nehezjelszo2%',
                                            host = "127.0.0.1")

cursor = database_connector.cursor()
cursor.execute("USE SANDBOX;")

class Customers:


    def persist(self):
        print("INSERT INTO customers VALUES ({},{},{},{},{},{},{},{},{},{},{});".format(self.CustomerID,
                                                                                            self.CompanyName,
                                                                          self.ContactName,self.ContactTitle,
                                                                          self.Address, self.City, self.Region,
                                                                          self.PostalCode, self.Country, self.Phone,
                                                                          self.Fax))

        cursor.execute("INSERT INTO customers VALUES ({},{},{},{},{},{},{},{},{},{},{});".format(self.CustomerID,
                                                                                                    self.CompanyName,
                                                                                  self.ContactName,self.ContactTitle,
                                                                                  self.Address, self.City, self.Region,
                                                                                  self.PostalCode, self.Country, self.Phone,
                                                                                  self.Fax))
        # database_connector.commit()

    @staticmethod
    def parse(row):
        parsed_row = row.split(";")
        customers = Customers()
        customers.CustomerID = parsed_row[0]
        customers.CompanyName= parsed_row[1]
        customers.ContactName = parsed_row[2]
        customers.ContactTitle= parsed_row[3]
        customers.Address = parsed_row[4]
        customers.City = parsed_row[5]
        customers.Region = parsed_row[6]
        customers.PostalCode = parsed_row[7]
        customers.Country =parsed_row[8]
        customers.Phone = parsed_row[9]
        customers.Fax = parsed_row[10]
        return customers

    @staticmethod
    def data_reader(csv_file):
        csv_rows = []
        with open(csv_file, "r", encoding="utf8") as file:
            for row in file:
                csv_rows.append(row)
        return csv_rows


    def caller(self):
        rows = Customers.data_reader("../CSV_FILES/customers.csv")
        for i in range(1, len(rows)):
            customers = Customers.parse(rows[i])
            customers.persist()

m = Customers()
m.caller()