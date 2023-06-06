class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] = hashMap[nums[i]] + 1
            else:
                hashMap[nums[i]] = 1
        
        answer = []

        sorted_values = []
        answer = []
        for val in hashMap.values():
            sorted_values.append(val)
        sorted_values.sort()

        while len(answer) < k:
            max_value = max(hashMap, key=hashMap.get)
            answer.append(max_value)
            del hashMap[max_value]
        
        return answer


            