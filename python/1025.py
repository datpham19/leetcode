"""
1025. Divisor Game
Easy

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]
        for i in range(N+1):
             for j in range(1, i//2 + 1):
                    if i % j == 0 and (not dp[i - j]):
                        dp[i] = True
                        break
        return dp[N]

    def divisorGame1(self, N: int) -> bool:
        return not N%2