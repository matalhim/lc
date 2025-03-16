class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_dict: dict[int: str] = {}
        for i in range(len(names)):
            heights_dict[heights[i]] = names[i] 
        
        return [heights_dict[key] for key in sorted(heights_dict.keys(), reverse=True)]


        