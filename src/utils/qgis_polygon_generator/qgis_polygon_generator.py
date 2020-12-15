layer=QgsVectorLayer('Polygon','poly',"memory")#,crs=EPSG(4326))
pr = layer.dataProvider() 
poly = QgsFeature()
points=[QgsPointXY(3.71, 51.01),QgsPointXY(3.72, 51.02),QgsPointXY(3.73, 51.01)]
poly.setGeometry(QgsGeometry.fromPolygonXY([points]))
pr.addFeatures([poly])
points=[QgsPointXY(3.71, 51.00),QgsPointXY(3.72, 51.005),QgsPointXY(3.73, 51.005),QgsPointXY(3.725, 50.99)]
poly.setGeometry(QgsGeometry.fromPolygonXY([points]))
pr.addFeatures([poly])
layer.updateExtents()
QgsProject.instance().addMapLayers([layer])
QgsVectorFileWriter.writeAsVectorFormat(layer,'test.shf', 'utf-8')