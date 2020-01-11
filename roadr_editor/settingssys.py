from xml.etree import ElementTree

SETTINGS_FILE = "settings.xml"

class settings_system():
    def __init__(self):
        self.noSettings = None
        self.assetPath = None

        self.checkFile()

    def checkFile(self):
        try:
            root = ElementTree.parse(SETTINGS_FILE).getroot()

            self.noSettings = False
        except:
            self.noSettings = True

    def parse(self):
        root = ElementTree.parse(SETTINGS_FILE).getroot()
        self.assetPath = root.find("assetpath").text

        self.noSettings = False

    def save(self):
        root = ElementTree.Element("roadr_editor")
        ElementTree.SubElement(root, "assetpath").text = self.assetPath

        tree = ElementTree.ElementTree(root)
        tree.write(SETTINGS_FILE)

        self.noSettings = False