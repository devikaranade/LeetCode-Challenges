class MyHashMap:

    def __init__(self):
        self.hashMap = [None for _ in range(1000001)]
        
    def put(self, key: int, value: int) -> None:
        self.hashMap[key]=value

    def get(self, key: int) -> int:
        if self.hashMap[key]!= None:
            return self.hashMap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.hashMap[key]:
            self.hashMap[key]=None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)