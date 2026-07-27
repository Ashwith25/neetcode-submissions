class Solution:
    def getKey(self, string):
        res= []
        for i in range(1, len(string)):
            res.append((ord(string[i])-ord(string[i-1]))%26)

        return tuple(res)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strings:
            key = self.getKey(string)
            hashmap[key] = hashmap.get(key, []) + [string]

        return list(hashmap.values())