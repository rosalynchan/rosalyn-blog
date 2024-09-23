import random

class RandomGen:
    def __init__(self, random_nums, probabilities):
        self._random_nums = random_nums
        self._probabilities = self._normalize_probabilities(probabilities)
        self._cumulative_probs = self._calculate_cumulative_probs()
        # test

    def _normalize_probabilities(self, probabilities):
        total = sum(probabilities)
        return [p / total for p in probabilities]

    def _calculate_cumulative_probs(self):
        cumulative_probs = []
        cum_prob = 0
        for prob in self._probabilities:
            cum_prob += prob
            cumulative_probs.append(cum_prob)
        return cumulative_probs

    def next_num(self):
        rand_val = random.random()  # Generate random float between [0, 1)
        for i, cum_prob in enumerate(self._cumulative_probs):
            if rand_val < cum_prob:
                return self._random_nums[i]
        return self._random_nums[-1]  # Fallback in case of floating-point precision issues

# Test setup
random_nums = [-1, 0, 1, 2, 3]
probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

gen = RandomGen(random_nums, probabilities)

# Simulate 100 calls to next_num
result = {num: 0 for num in random_nums}
for _ in range(10000):
    num = gen.next_num()
    result[num] += 1

print(result)
