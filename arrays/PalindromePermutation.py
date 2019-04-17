"""
#106, #121, #134, #136
Check if a string is a permutation of a palindrome

Input: Tact Coa
Output: True ( taco cat, atco cta)
"""
import unittest


# Time Complexity: O(N)
# Space Complexity: O(N)
def is_palindrome_permutation(string):

    seen = {}
    for char in string:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1

    found_odd = False
    for elem in seen:
        if seen[elem] % 2 != 0:
            if not found_odd:
                found_odd = True
            else:
                return False

    return True


class Test(unittest.TestCase):
    true_case = [('abcdcba'), ('XyyXZ=Z='), ('')]
    false_case = [('abcda'), ('XyZX'), ('=-')]

    def test_with_extra_space(self):
        for item in self.true_case:
            self.assertTrue(is_palindrome_permutation(item))
            # self.assertTrue(is_unique_without_extra_space(item))

        for item in self.false_case:
            self.assertFalse(is_palindrome_permutation(item))
            # self.assertFalse(is_unique_without_extra_space(item))


if __name__ == "__main__":
    unittest.main()