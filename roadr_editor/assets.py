from xml.etree import ElementTree
import os

class asset_file():
    def __init__(self, name, id, filename):
        self.name = name
        self.id = id
        self.filename = filename

class asset_system():
    def __init__(self, assetFolder):
        self.maps = [0] * 1000
        self.objs = [0] * 1000
        self.tiles = [0] * 1000
        self.assetDir = assetFolder
        self.map_path = None
        self.obj_path = None
        self.tile_path = None
        self.assetFile = os.path.join(self.assetDir, "assets.xml")

    def parseDef(self):
        root = ElementTree.parse(self.assetFile).getroot()
        self.map_path = root.find("maps/path").text
        self.obj_path = root.find("objs/path").text
        self.tile_path = root.find("tiles/path").text

        for tag in root.findall("maps/map"):
            self.maps[int(tag.find("id").text)] = asset_file(tag.find("name").text, tag.find("id").text, tag.find("file").text)

        for tag in root.findall("objs/obj"):
            self.objs[int(tag.find("id").text)] = asset_file(tag.find("name").text, tag.find("id").text, tag.find("file").text)

        for tag in root.findall("tiles/tile"):
            self.tiles[int(tag.find("id").text)] = asset_file(tag.find("name").text, tag.find("id").text, tag.find("file").text)

    def trim(self, arr):
        count = 0

        for item in arr:
            if item != 0:
                count += 1

        newArr = [0] * count
        i = 0

        while i < count:
            newArr[i] = arr[i]
            i += 1

        return newArr

    def trimAll(self):
        self.maps = self.trim(self.maps)
        self.objs = self.trim(self.objs)
        self.tiles = self.trim(self.tiles)

    def mergePaths(self):
        for asset in self.maps:
            asset.filename = os.path.join(self.assetDir, self.map_path, asset.filename)

        for asset in self.objs:
            asset.filename = os.path.join(self.assetDir, self.obj_path, asset.filename)
        
        for asset in self.tiles:
            asset.filename = os.path.join(self.assetDir, self.tile_path, asset.filename)

    def checkFolder(self):
        try:
            root = ElementTree.parse(self.assetFile).getroot()
            self.map_path = root.find("maps/path").text
            self.obj_path = root.find("objs/path").text
            self.tile_path = root.find("tiles/path").text

            if(self.map_path is not None and self.obj_path is not None and self.tile_path is not None):
                return True
            else:
                return False
        except:
            return False