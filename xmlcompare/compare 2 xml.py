import xml.etree.ElementTree as ET

class XmlTree():
    def xml_compare(self, x1, x2, excludes=[]):
        """
        Compares two xml etrees
        x1: the first tree
        x2: the second tree
        excludes: list of string of attributes to exclude from comparison
        True if both files match
        """

        if x1.tag != x2.tag:
            print('Tags do not match: %s and %s' % (x1.tag, x2.tag))
            return False
        for name, value in x1.attrib.items():
            if not name in excludes:
                if x2.attrib.get(name) != value:
                    print('Attributes do not match: %s=%r, %s=%r'
                          % (name, value, name, x2.attrib.get(name)))
                    return False
        for name in x2.attrib.keys():
            if not name in excludes:
                if name not in x1.attrib:
                    print('x2 has an attribute x1 is missing: %s'
                          % name)
                    return False
        if not self.text_compare(x1.text, x2.text):
            print('text: %r != %r' % (x1.text, x2.text))
            return False
        if not self.text_compare(x1.tail, x2.tail):
            print('tail: %r != %r' % (x1.tail, x2.tail))
            return False
        cl1 = x1.getchildren()
        cl2 = x2.getchildren()
        if len(cl1) != len(cl2):
            print('children length differs, %i != %i'
                  % (len(cl1), len(cl2)))
            return False
        i = 0
        for c1, c2 in zip(cl1, cl2):
            i += 1
            if not c1.tag in excludes:
                if not self.xml_compare(c1, c2, excludes):
                    print('children %i do not match: %s'
                          % (i, c1.tag))
                    return False
        return True

    def text_compare(self, t1, t2):
        """
        Compare two text strings
        t1: text one
        t2: text two
        True if a match
        """
        if not t1 and not t2:
            return True
        if t1 == '*' or t2 == '*':
            return True
        return (t1 or '').strip() == (t2 or '').strip()

root_1 = ET.parse('file1.xml').getroot()
root_2 = ET.parse('file2.xml').getroot()

comparator = XmlTree()

if comparator.xml_compare(root_1, root_2, ["from"]):
    print("XMLs match")
else:
    print("XMLs don't match")
