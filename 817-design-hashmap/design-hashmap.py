class MyHashMap:

    def __init__(self):
        self.map = []
        

    def put(self, key: int, value: int) -> None:
        for i in self.map:
            if i[0]==key:
                i[1]=value
                return
        self.map.append([key,value])


    def get(self, key: int) -> int:
        for k in self.map:
            if k[0]==key:
                return k[1]
        return -1

    def remove(self, key: int) -> None:
        for k in self.map:
            if k[0] == key:
                self.map.remove(k)
                return


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)