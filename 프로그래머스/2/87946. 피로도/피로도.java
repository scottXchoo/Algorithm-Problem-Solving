/**
문제분석
- 최소 필요 피로도 : 탐험을 시작하기 위해 필요
- 소모 피로도 : 탐험 후, 소모되는 피로도
- 목표 : 최대한 많은 탐험을 가능한 던전 수는?

제한사항
- k : 5000 이하
- 던전의 개수 : 8 이하?!?
- ["최소 필요 피로도", "소모 피로도"]
- 최소 필요 피로도 >= 소모 피로도

아이디어
- 무식하게 모든 경우의 수 체크하기? 던전의 개수가 8 이하
- dungeouns의 길이 = N => N!만큼의 시간복잡도 걸림
- 

**/
import java.util.*;

class Solution {
    public int solution(int k, int[][] dungeons) {
        int answer = -1;
        int n = dungeons.length;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
        List<List<Integer>> perms = new ArrayList<>();
        permute(nums, 0, perms);
        for (List<Integer> perm : perms) {
            int _k = k;
            int cnt = 0;
            for (int p : perm) {
                int idx = p - 1;
                int minPiro = dungeons[idx][0];
                int usedPiro = dungeons[idx][1];
                if (_k >= minPiro) {
                    _k -= usedPiro;
                    cnt += 1;
                }
                if (cnt > answer) {
                answer = cnt;
                }
            }
        }
        
        return answer;
    }
    
    private static void permute(int[] nums, int start, List<List<Integer>> result) {
        if (start == nums.length) {
            List<Integer> permutation = new ArrayList<>();
            for (int num : nums) {
                permutation.add(num);
            }
            result.add(permutation);
        } else {
            for (int i = start; i < nums.length; i++) {
                swap(nums, start, i);
                permute(nums, start + 1, result);
                swap(nums, start, i);
            }
        }
    }
    
    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}