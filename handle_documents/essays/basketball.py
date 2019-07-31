import matplotlib.pyplot as plt
import numpy as np


def one_of_one_win_prob(shot_prob: float) -> float:
    """
    Calculates the probability of winning a game 
    with one chance to make one shot.
    """
    return shot_prob


def two_of_three_win_prob(shot_prob: float) -> float:
    """
    Calculates the probability of winning a game with
    three chances to make at least two shots from the
    probability of making a single shot.
    """
    return 3 * shot_prob ** 2 - 2 * shot_prob ** 3


p_range = np.linspace(0, 1, 100)
probs_1_of_1 = [one_of_one_win_prob(p) for p in p_range]
probs_2_of_3 = [two_of_three_win_prob(p) for p in p_range]

plt.plot(p_range, probs_1_of_1, label="One of One to Win")
plt.plot(p_range, probs_2_of_3, label="Two of Three to Win")
plt.ylabel("Probability of Winning Game")
plt.xlabel("Probability of Making a Single Shot")
plt.legend()
plt.show()

