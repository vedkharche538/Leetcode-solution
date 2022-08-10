"""
    _summary_: Minimum Rounds to Complete All Tasks

You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.


Constraints:

1 <= tasks.length <= 105
1 <= tasks[i] <= 109
"""


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # Time: O(N) Space: O(N)
        task_occurence = collections.defaultdict()
        for task in tasks:
            task_occurence[task] = task_occurence.get(task, 0) + 1

        # Whenever modulo is [1, 2], no of rounds require to finish will be (occurence // 3) + 1
        # example - 16 % 3 = 1 ==> it will require 3, 3, 3, 3, 2, 2 which is (16 // 3) + 1
        # example - 17 % 3 = 2 ==> it will require 3, 3, 3, 3, 3, 3 which is (17 // 3) + 1

        rounds = 0
        for occurence in task_occurence.values():
            if occurence == 1:
                return -1
            if occurence % 3 in [1, 2]:
                rounds += (occurence // 3) + 1
            else:
                rounds += (occurence // 3)
        return rounds
