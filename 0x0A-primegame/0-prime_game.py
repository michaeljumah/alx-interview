#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to determine the winner of the prime game."""
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        primes_set = primes_in_range(1, num)

        if not primes_set:
            ben_wins += 1
            continue

        maria_turn = True
        while True:
            valid_move_available = False

            # Maria's turn
            if maria_turn:
                for prime in primes_set:
                    if prime in rounds_set:
                        valid_move_available = True
                        primes_set.remove(prime)
                        rounds_set = [x for x in rounds_set if x % prime != 0]
                        break
                if not valid_move_available:
                    ben_wins += 1
                    break
            # Ben's turn
            else:
                for prime in primes_set:
                    if prime in rounds_set:
                        valid_move_available = True
                        primes_set.remove(prime)
                        rounds_set = [x for x in rounds_set if x % prime != 0]
                        break
                if not valid_move_available:
                    maria_wins += 1
                    break

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
