import arcpy, os
from arcpy import env
env.workspace = r"C:\ParentDirectory"
walk = arcpy.da.Walk(env.workspace, topdown=True, datatype="RasterDataset")
for dirpath, dirnames, filenames in walk:
	print(dirpath)
	rasterList = []
	for file in filenames:
		raster = os.path.join(dirpath, file)
		rasterList.append(raster) #no clue what this does.
	try:
		arcpy.MosaicToNewRaster_management(rasterList, dirpath, "Mosaic.tif", "", "", "", 3) # Mosaic to New Raster function in arcPy. Refer to ArcGIS Desktop web help for details.
	except:
		pass

# This only runs on Python 2.7 since ArcPy relies on this version of Python - if you have different versions of Python installed on the same computer, 
# rename one of the executable files OR change directory to the 2.7 version of Python and execute from there.
# Pay close attention to arcpy.MosaicToNewRaster management, since there are various datasets containing different number of bands, projections, data types and so on. If it's executing a bit too quickly, then chances are there are problems with your code, mostly with MosaicToNewRaster_management line (12). Run "mosaic_folders2.py" to diagnose the issue.