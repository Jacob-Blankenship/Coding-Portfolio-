import arcpy
import os

arcpy.env.workspace = "E:\College\Web GIS\Old_Network\All_Network_Floors_2.0\All_Network_Floors_2.0"  # Put the folder of all the shapefiles here
arcpy.env.overwriteOutput = True

# Set local variables
outWorkspace = "E:\College\Web GIS\Old_Network\All_Network_Floors_2.0"  # The location in which you want the shapefiles to go

for infc in arcpy.ListFeatureClasses():  # runs through all shapefiles in folder
    print(infc)
    spatial_ref = arcpy.Describe(infc).spatialReference


    print(spatial_ref.factoryCode)
    print(spatial_ref.VCS.factoryCode)



    if spatial_ref.factoryCode != 32139 or spatial_ref.VCS.factoryCode != 6357:
        outfc = os.path.join(outWorkspace, infc)
        # Set output coordinate system
        outCS = arcpy.SpatialReference(32139, 6357)  # the coordinate system

        # run project tool
        arcpy.Project_management(infc, outfc, outCS, vertical="True")

        # check messages
        print(arcpy.GetMessages())
