import arcpy
import os

# Set the workspace environment setting
arcpy.env.workspace = r"C:\ParentDirectory" # doesn't need to be a raw string using / path delimiter'

walk = arcpy.da.Walk(datatype="RasterDataset")

for dir_path, dir_names, file_names in walk:
    OutputRaster = dir_path + '.tif' # the TIFF file in the parent directory with the same name
    AllFiles     = []                # empty list
    for filename in file_names:
        print(os.path.join(dir_path, filename))
        AllFiles.append(os.path.join(dir_path, filename)) # add this one to the list
    if len(AllFiles) > 0 :  # make sure there is acutally rasters in this folder
        arcpy.MosaicToNewRaster_management(AllFiles, os.path.dirname(OutputRaster), os.path.basename(OutputRaster), "", "", "", 1)