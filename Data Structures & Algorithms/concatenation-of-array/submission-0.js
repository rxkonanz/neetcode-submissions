class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        
        let ans = nums.join(",") + "," + nums.join(",");
        ans = ans.split(",");
        let response = [];
        for(var i = 0; i < ans.length; i++){
            response.push(parseInt(ans[i]))
        }
        return response;
    }
}
