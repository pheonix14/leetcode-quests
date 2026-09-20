// Created by pheonix14 at 2026/09/21 00:23
// leetgo: 1.4.18
// https://leetcode.com/problems/two-sum/

// @lc code=begin

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
    return [];
};

// @lc code=end
