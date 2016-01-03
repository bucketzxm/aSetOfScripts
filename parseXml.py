import xml.dom.minidom


node_dict = {}

def getTagText(root, tag):
	node = root.getElementsByTagName(tag)[0]
	rc = ""
	for node in node.childNodes:
		if node.nodeType in ( node.TEXT_NODE, node.CDATA_SECTION_NODE):
			rc = rc + node.data
	return rc


def parseXml( text ):
	doc = xml.dom.minidom.parseString(text)

	root = doc.documentElement
	print("root=>%s",root)
	for child in root.childNodes:
		print(child)


if __name__ == "__main__":
	pass
