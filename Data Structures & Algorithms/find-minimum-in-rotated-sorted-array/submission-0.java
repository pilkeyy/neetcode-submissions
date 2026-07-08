class Solution {
    public int findMin(int[] nums) {
        int min = nums[0];
        int l = 0;
        int r = nums.length -1;
        while(l < r){
            int middle = l + (r - l)/2;
            if(nums[l] < min){
                min = nums[l];
            }
            if(nums[r] < min){
                min = nums[r];
            }
            if(nums[middle] < min){
                l = l + 1;
            } else{
                r = r - 1;
            }
        }
        return min;        
    }
}
