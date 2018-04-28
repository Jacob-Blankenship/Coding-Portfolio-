import arcpy
import os

arcpy.env.workspace = r'E:\College\Practicum\Elevation_data'
arcpy.env.overwriteOutput = True

# Set local variables
outWorkspace = r"I:\TEMP\Porjected"

for infc in arcpy.ListDatasets():

    spatial_ref = arcpy.Describe(infc).spatialReference

    print(spatial_ref.factoryCode)

    if spatial_ref.factoryCode != 32040:

        outfc = os.path.join(outWorkspace, infc)

        # Set output coordinate system
        outCS = arcpy.SpatialReference(32040)
        print(infc)
        # run project tool
        arcpy.ProjectRaster_management(infc, outfc, outCS)
        print("Done")
        # check messages
        print(arcpy.GetMessages())

print("Done")

