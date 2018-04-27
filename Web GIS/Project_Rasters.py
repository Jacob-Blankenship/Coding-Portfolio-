import arcpy
import os

arcpy.env.workspace = "C:\Users\TEMP\Documents\stuff"
arcpy.env.overwriteOutput = True

# Set local variables
outWorkspace = "C:\Users\TEMP\Documents\stuff\projected"

for infc in arcpy.ListDatasets():
	print(infc)
	outfc = os.path.join(outWorkspace, infc)
	# Set output coordinate system
	outCS = arcpy.SpatialReference(32140)
	# run project tool
	arcpy.ProjectRaster_management(infc, outfc, outCS)
	# check messages
	print(arcpy.GetMessages())