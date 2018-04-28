import arcpy

num = 1
num1 = 0
elev = [107.2, 115.53, 120.32, 125.12, 129.91]  # the height you want, stating from the first floor
while num1 < 5:  # 5 is the amount of floors you have in the building
    # this only work in you have the layers for each floor separated     that why there is .formate to change the file path per floor
    with arcpy.UpdateCursor("C:\\3D_Project\\All_Network_Floors-20180417T155721Z-001\\All_Network_Floors\\Floor_{}_R_P.shp".format(num),"SHAPE@Z", explode_to_points=True) as cursor:
        for row in cursor:
            row[0] = elev[num1]
            cursor.updateRow(row)
            print(row)
    num += 1
    num1 += 1
