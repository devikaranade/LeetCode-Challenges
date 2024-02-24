class FileSystem:

    def __init__(self):
        self.map = defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        if len(path)==0 or path == "/" or (path in self.map):
            return False
        if path.count("/")>1:
            parent_path = "/".join(path.split("/")[:-1])
            if parent_path not in self.map:
                return False
        self.map[path]=value
        return True
        

    def get(self, path: str) -> int:
        if path not in self.map:
            return -1
        return self.map[path]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)