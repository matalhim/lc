class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items_dict: dict = {}

        for key, value in items1:
            items_dict[key] = items_dict.get(key, 0) + value
        
        for key, value in items2:
            items_dict[key] = items_dict.get(key, 0) + value
        
        return sorted(items_dict.items())


