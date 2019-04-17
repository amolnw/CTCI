"""
Find if a string has all unique characters without using additional data structure
"""
import unittest


# Time Complexity: O(N^2)
# Space Complexity: O(1)
def is_unique_without_extra_space(string):

    if len(string) > 128:
        return False

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[j] == string[i]:
                return False
    return True


# Time Complexity: O(N)
# Space Complexity: O(N)
def is_unique_with_extra_space(string):

    if len(string) > 128:
        return False

    seen = [False for i in range(128)]
    for char in string:
        if not seen[ord(char)]:
            seen[ord(char)] = True
        else:
            return False
    return True


class Test(unittest.TestCase):
    true_case = [('abcd'), ('XyZ='), ('')]
    false_case = [('abcda'), ('XyZX'), ('==')]

    def test_with_extra_space(self):
        for item in self.true_case:
            self.assertTrue(is_unique_with_extra_space(item))
            self.assertTrue(is_unique_without_extra_space(item))

        for item in self.false_case:
            self.assertFalse(is_unique_with_extra_space(item))
            self.assertFalse(is_unique_without_extra_space(item))


if __name__ == "__main__":
    unittest.main()