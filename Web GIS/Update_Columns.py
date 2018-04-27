import arcpy

fc = r'E:\\College\\Web GIS\\All_Network_Floors_3.0\\Stairs.shp'
fields = ['OBJECTID','BldShrtNam','Building_l','FLOORKEY','SHAPE@Z']
OB = 0
Floorkey = ["a0275_1F","a0275_2F","a0275_3F","a0275_4F","a0275_5F","SHAPE@Z"]
with arcpy.da.UpdateCursor(r'E:\\College\\Web GIS\\All_Network_Floors_3.0\\Stairs.shp',fields) as cursor:
	for row in cursor:
		row[0]=OB
		row[1]="LAAH"
		row[2]="a0275"
		if (row[4] == 107.2):
			row[3]="a0275_1F"
		elif (row[4] == 115.53):
			row[3]="a0275_2F"
		elif (row[4] == 120.32):
			row[3]="a0275_3F"
		elif (row[4] == 125.12):
			row[3]="a0275_4F"
		elif (row[4] == 129.91):
			row[3]="a0275_5F"
		else:
			row[3]="Between_Levels"
		print(OB)
		OB+=1
		cursor.updateRow(row)