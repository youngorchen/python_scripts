import csv
from datetime import datetime,timedelta
from enum import Enum

total_products = 0
selled_products = 0
missed_type_products = 0
orders = 0


class ProductData(Enum):
    id = 0
    handle = 1
    sku = 2
    composite_handle = 3
    composite_sku = 4
    composite_quantity = 5
    name = 6
    description = 7
    type = 8
    variant_option_one_name = 9
    variant_option_one_value = 10
    variant_option_two_name = 11
    variant_option_two_value = 12
    variant_option_three_name = 13
    variant_option_three_value = 14
    tags = 15
    supply_price = 16
    retail_price = 17
    loyalty_value = 18
    loyalty_value_default = 19
    tax_name = 20
    tax_value = 21
    account_code = 22
    account_code_purchase = 23
    brand_name = 24
    supplier_name = 25
    supplier_code = 26
    active = 27
    track_inventory = 28
    inventory_Main_Outlet = 29
    reorder_point_Main_Outlet = 30
    restock_level_Main_Outlet = 31

class SalesDetailData(Enum):
    Date = 0
    Receipt_Number = 1
    Line_Type = 2
    Customer_Code = 3
    Customer_Name = 4
    Note = 5
    Quantity = 6
    Subtotal = 7
    Sales_Tax = 8
    Discount = 9
    Loyalty = 10
    Total = 11
    Paid = 12
    Details = 13
    Register = 14
    User = 15
    Status = 16
    Sku = 17
    AccountCodeSale = 18
    AccountCodePurchase = 19


file1 = 'c:/temp/product-export.csv'
file2 = 'c:/temp/sales_57465.csv'

h = {}
with open(file1,newline='',encoding='utf-8') as f:
    reader = csv.reader(f)

    types = set()
    for row in reader:
        #print(row[ProductData.name.value:ProductData.name.value+3])
        h[row[ProductData.name.value]] = row[ProductData.type.value]
        types.add(row[ProductData.type.value])

#product --> type
#for k in h:
    #print("{k}=>{v}".format(k=k,v=v))
#    print("%s=>%s"%(k,h[k]))

total_products = h.__len__()

start_date = datetime.strptime("2017-1-1","%Y-%m-%d")
#date = raw_input("enter a date")
#print(date)
#start_date = datetime.strptime(date,"%Y-%m-%d")
end_date = datetime.strptime("2018-1-1","%Y-%m-%d")

def get_type(product,h,t):
    if h.__contains__(product) and h[product] == t:
        return True
    return False


def report(start_date,end_date,t='',pro = ''):

    with open(file2,newline='',encoding='utf-8') as f:
        reader = csv.reader(f)

        s = set()
        missed_product = set()
        selled_product = set()
        sale_quantity = 0
        sale_amount = 0
        for row in reader:
            try:
                d = datetime.strptime(row[SalesDetailData.Date.value],"%Y-%m-%d %H:%M:%S")
                #print(d)
                if row[SalesDetailData.Line_Type.value] == "Sale Line" and d >= start_date and d < end_date and \
                   (
                           (t == '' and pro == '') or  \
                           (t != '' and pro == '' and get_type(row[SalesDetailData.Details.value],h,t) ) or \
                           (t == '' and pro != '' and row[SalesDetailData.Details.value] == pro)
                    ):
                    #print(row)
                    s.add(row[SalesDetailData.Receipt_Number.value])
                    selled_product.add(row[SalesDetailData.Details.value])
                    sale_quantity += int(float(row[SalesDetailData.Quantity.value]))
                    sale_amount += float(row[SalesDetailData.Total.value])

                    if not h.__contains__(row[SalesDetailData.Details.value]):
                        #print(row[SalesDetailData.Details.value])
                        #print("!!!")
                        missed_product.add(row[SalesDetailData.Details.value])
                        #exit(1)
            except ValueError as e:
                #print(e)
                pass
                #exit(0)

        #print("missed products... ")
        #for i in missed_product:
        #    print(i)

        orders = s.__len__()
        selled_products = selled_product.__len__()
        missed_type_products = missed_product.__len__()

        print("orders: (%d) sale_amount: (%.2f) sale_quantity: (%d)" % (orders, sale_amount, int(sale_quantity)))
        if orders == 0:
            orders = 1  # in case div zero
        average_sale_amount = sale_amount / orders
        average_sale_quantity = sale_quantity / orders

        print("average_sale_amount: (%.2f) average_sale_quantity: (%.2f) " % ( average_sale_amount, average_sale_quantity))

        return selled_products, missed_type_products

print("------------------------")
print("from %s to %s" %(start_date,end_date))

selled_products, missed_type_products = report(start_date,end_date)

print("total products: (%d), selled products: (%d), missed type products: (%d)" %(total_products,selled_products,missed_type_products))

count = 1
for i in types:
    print("")
    print("%d type (%s)" %(count,i))
    count += 1
    selled_products, missed_type_products = report(start_date, end_date,i,'')

    print("total products: (%d), selled products: (%d), missed type products: (%d)" % (total_products, selled_products, missed_type_products))

count = 1
for i in h.keys():
    print("")
    print("%d product (%s)" % (count,i))
    count += 1
    selled_products, missed_type_products = report(start_date, end_date, '',i)

    print("total products: (%d), selled products: (%d), missed type products: (%d)" % ( total_products, selled_products, missed_type_products))

