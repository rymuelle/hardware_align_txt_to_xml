import xml.etree.ElementTree as ET

geometry_xml = ET.ElementTree(file="hw_tb_mix.xml")

root = geometry_xml.getroot()

with open('AfterFit-PGLike_MB1234chambers__8234_6d_123_PG2008_20170422_NOFIT.txt','r') as f:
	for x in f:
		values = x.split()
		print values[0], values[1], values[2], values[3], values[5], values[7], values[9], values[11],values[13]
		for child in root.findall("./operation/*[@wheel='{}'][@station='{}'][@sector='{}']/../setposition".format(values[0],values[1],values[2])):
			#print child.attrib['x']
			child.set('x', values[3])
			child.set('y', values[5])
			child.set('z', values[7])
			child.set('phix', values[9])
			child.set('phiy', values[11])
			child.set('phiz', values[13])
	

geometry_xml.write('hw_tb_mix2.xml')
