import java.util.HashMap;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> existingNums = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i += 1) {
            if (existingNums.containsKey(nums[i])) {
                return true;
            } else {
                existingNums.put(nums[i], 0);
            }
        }

        return false;
    }
}