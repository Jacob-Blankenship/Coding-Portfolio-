import arcpy

num = 0
num1 = 0
# the list of heights that you want you points to be at   This code inserts the heights into the points in the same order in which you made them in arcmap
elev = [107.2, 109.97, 109.97, 112.75, 112.75, 115.53, 115.53, 117.925, 117.925, 120.32, 120.32, 122.75, 122.75, 125.12,
        125.12, 126.71, 126.71, 128.31, 128.31, 129.91]
elev2 = [111.365, 111.365, 120.32, 107.2, 120.32, 122.75, 122.75, 125.12]
# just change the file path to whatever you have your points
with arcpy.UpdateCursor(r'C:\Users\Jdb-2019\Documents\All_Network_Floors-20180418T234415Z-001\All_Network_Floors\Stairs.shp', "SHAPE@Z",explode_to_points=True) as cursor:
    for row in cursor:
        if num1 >= 28:
            row[0] = elev[num]
            cursor.updateRow(row)
            num += 1
            print(row[0])
        num1 += 1
