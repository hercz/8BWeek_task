import mysql.connector
import csv

database_connector = mysql.connector.connect(user='codecooler', password = 'Nehezjelszo2%',
                                            host = "127.0.0.1")

cursor = database_connector.cursor()
cursor.execute("USE SANDBOX;")


class Orderdetails:


    # def __init__(self, OrderID, ProductID, UnitPrice, Quantity, Discount):
    #     self.OrderID = OrderID
    #     self.ProductID = ProductID
    #     self.UnitPrice = UnitPrice
    #     self.Quantity = Quantity
    #     self.Discount = Discount



    def persist(self):
        cursor.execute("INSERT INTO Orderdetails VALUES ({},{},{},{},{});".format(self.OrderID, self.ProductID,
                                                                                            self.UnitPrice,self.Quantity,
                                                                                            self.Discount))
        database_connector.commit()


    @staticmethod
    def parse(row):
        parsed_row = row.split(";")

        orderdetails = Orderdetails()
        orderdetails.OrderID = parsed_row[0]
        orderdetails.ProductID = parsed_row[1]
        orderdetails.UnitPrice = parsed_row[2]
        orderdetails.Quantity = parsed_row[3]
        orderdetails.Discount = parsed_row[4]
        return orderdetails


    @staticmethod
    def data_reader(csv_file):
        csv_rows = []
        with open(csv_file, "r") as file:
            for row in file:
                csv_rows.append(row)
        return csv_rows

    def caller(self):
        rows = Orderdetails.data_reader("./CSV_FILES/order_details.csv")
        for i in range(1, len(rows)):
            orderdetails = Orderdetails.parse(rows[i])
            orderdetails.persist()


m = Orderdetails()
m.caller()
