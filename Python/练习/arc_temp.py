import arcpy
arcpy.env.workspace = "D:\����\BufferDemo"
arcpy.Buffer_analysis("point", "D:\����\BufferDemo", "10000 Feet", "FULL", "ROUND", "LIST", "Distance")
