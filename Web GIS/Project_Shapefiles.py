import arcpy
import os

arcpy.env.workspace = "E:\College\Web GIS\All_Network_Floors_2.0"                # Put the folder of all the shapefiles here
arcpy.env.overwriteOutput = True

# Set local variables
outWorkspace = "E:\College\Web GIS\All_Network_Floors_2.0\Projected_Shapefiles"  # The location in which you want the shapefiles to go

for infc in arcpy.ListFeatureClasses():   #runs through all shapefiles in folder
	print(infc)
	outfc = os.path.join(outWorkspace, infc)
	
	# Set output coordinate system
	outCS = arcpy.SpatialReference("NAD 1983 StatePlane Texas Central FIPS 4203 (Meters)" , "NAVD88 (depth)")   #the coordnate system
	
	# run project tool
	arcpy.Project_management(infc, outfc, outCS,vertical="True")
	
	# check messages
	print(arcpy.GetMessages())
