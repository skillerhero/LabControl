import pymysql.cursors
import xlrd

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='analisis',
                             cursorclass=pymysql.cursors.DictCursor,
                             charset='utf8')

                             # Give the location of the file
loc = ("analisis_solos.xls")
 
# To open Workbook
wb = xlrd.open_workbook(loc,encoding_override="utf-8")
sheet = wb.sheet_by_index(0)
print(sheet.nrows)
areas={}
areas['Urianálisis/QS']=1
areas['Urianalisis/QS']=1
areas['Hematología']=2
areas['Serología/Hormonas']=3
areas['Bacteriología']=4
areas['']=5
with connection:
    with connection.cursor() as cursor:
        # Create a new record        
        for i in range(sheet.nrows):
            #consultar el area
            



            
            sql = "INSERT INTO analisis (ana_nombre, ana_costo, ana_area_id_fk) VALUES (%s, %s, %s)"
            cursor.execute(sql, (sheet.cell_value(i, 1).encode('utf8') ,sheet.cell_value(i, 2),areas[sheet.cell_value(i, 0).strip()] ))
         #   print(sheet.cell_value(i, 0))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
