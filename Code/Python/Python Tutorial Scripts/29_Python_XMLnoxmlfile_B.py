import xml.sax

class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("-----PERSON-----")
            print("ID: {}".format(attrs['id']))
    
    def characters(self, content):
        if self.current == "name":
            self.name == content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print("Name: {}".format(self.name))
        elif self.current == "age":
            print("Age: {}".format(self.age))
        elif self.current == "weight":
            print("Weight: {}".format(self.weight))
        elif self.current == "height":
            print("Height: {}".format(self.height))
        self.current = ""

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')