from typing import List


class ScoreCalculate:

    def score_calculator(self, score: List[int]) -> str:
        """
        Returns Individual score of player 1 and 2
        """
        player1:int = 0
        player2:int = 0
        strike_with_player = 1

        for runs in score:
            if runs % 2 == 0: #even
                if strike_with_player == 1:
                    player1 += runs
                else:
                    player2 += runs
            else: #odd
                if strike_with_player ==1:
                    player1 += runs
                    strike_with_player =2
                else: #strike with player 2 and he scores odd runs
                    player2 += runs
                    strike_with_player = 1
        return f"p1:{player1}, p2:{player2}"


if __name__ == "__main__":
    try:
        score: List[int] = [int(x) for x in input("Enter score separated by space: ").split()]
        sc: ScoreCalculate = ScoreCalculate()
        print(sc.score_calculator(score=score))
    except Exception as e:
        print(f"Following exception has occurred:   {e}")