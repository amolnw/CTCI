"""
Check if one string is permutation of the other
"""
import unittest


# Time Complexity: O(NLogN) - Timsort
# Space Complexity: O(1)
def check_permutation_without_extra_space(string1, string2):

    if len(string1) != len(string2) or sorted(string1) != sorted(string2):
        return False
    else:
        return True


# Time Complexity: O(N)
# Space Complexity: O(N)
def check_permutation_with_extra_space(string1, string2):

    if len(string1) != len(string2):
        return False

    seen = {}

    for char in string1:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1

    for char in string2:
        if char not in seen:
            return False
        else:
            seen[char] -= 1
            if seen[char] < 0:
                return False

    return True


class Test(unittest.TestCase):
    true_case = (('abcd', 'cbda'), ('XyZ=', 'Zy=X'), ('', ''))
    false_case = (('abcda', 'abdc'), ('XyZX', 'XyZZ'), ('==', '=%'))

    def test_with_extra_space(self):
        for item in self.true_case:
            self.assertTrue(check_permutation_with_extra_space(*item))
            self.assertTrue(check_permutation_without_extra_space(*item))

        for item in self.false_case:
            self.assertFalse(check_permutation_with_extra_space(*item))
            self.assertFalse(check_permutation_without_extra_space(*item))


if __name__ == "__main__":
    unittest.main()