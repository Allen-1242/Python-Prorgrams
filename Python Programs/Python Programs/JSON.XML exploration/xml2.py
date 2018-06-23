from xml.etree.ElementTree import parse

doc = parse('xml1.xml')
root = doc.getroot()
print(root.tag)

for child in root:
	print(child.tag, child.text, child.attrib)
