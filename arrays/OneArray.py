"""
Check if two strings are one or zero edits away

Input: pale, ple
Output: true

Input: pales, pale
Output: true

Input: pale, bale
Output: true

Input: pale, bake
Output: false
"""
import unittest


# Time Complexity: O(N)
# Space Complexity: O(N)
def is_one_array(string1, string2):

    if abs(len(string1) - len(string2)) > 1:
        return False

    longer_string = string1 if len(string1) > len(string2) else string2
    shorter_string = string1 if len(string1) < len(string2) else string2

    iterator_shorter_string = 0
    iterator_longer_string = 0
    found_difference = False

    while iterator_shorter_string < len(shorter_string) and iterator_longer_string < len(longer_string):
        if shorter_string[iterator_shorter_string] != longer_string[iterator_longer_string]:
            if not found_difference:
                found_difference = True
                if len(shorter_string) == len(longer_string):
                    iterator_shorter_string += 1
                    iterator_longer_string += 1
                else:
                    iterator_longer_string += 1
            else:
                return False
        else:
            iterator_shorter_string += 1
            iterator_longer_string += 1

    return True


class Test(unittest.TestCase):
    true_case = (('abcd', 'abd'), ('abcd', 'abdd'), ('abd', 'abcd'))
    false_case = (('abcda', 'abdc'), ('abcd', 'abcdda'))

    def test_with_extra_space(self):
        for item in self.true_case:
            self.assertTrue(is_one_array(*item))

        for item in self.false_case:
            self.assertFalse(is_one_array(*item))


if __name__ == "__main__":
    unittest.main()