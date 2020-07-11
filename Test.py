# Test


# Test through unittest


# Variety of Assert Methods

"""
Method                          Use

assertEqual(a,b)                Verify that a == b
assertNotEqual(a,b)             Verify that a != b
assertTrue(x)                   Verify that x is True
assertFalse(x)                  Verify that x is False
assertIn(item,list)             Verify that item is in list
assertNotIn(item, list)         Verify that item is not in list
"""

# Single function

import unittest

from function import get_formatted_name

class TestNamesCase(unittest.TestCase):
    """Test for 'function.py'"""

    def test_first_last_name(self):
        """Do names like 'moazzam muhammd' work?"""
        test_formatted_name = get_formatted_name('moazzam', 'muhammad')

        self.assertEqual(test_formatted_name, 'Moazzam Muhammad')
    
    def test_first_last_middle_name(self):
        """Do name like'hafiz muhammad uzair"""
        test_formatted_name = get_formatted_name('hafiz', 'uzair', 'muhammad')

        self.assertEqual(test_formatted_name, 'Hafiz Muhammad Uzair')

if __name__ == '__main__':
    unittest.main()

print("\n====================")


# Single Class


class AnonymousSurvey:
    """Collect Survey data"""

    def __init__(self, question):
        """Store a question and prepare to store response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show question"""
        print(self.question)

    def store_response(self, new_response):
        """store the response to survey"""
        self.responses.append(new_response)
    
    def show_result(self):
        """Show the survey report"""
        print("Survey report:\n")
        for response in responses:
            print(response)



class AnonymousSurvey(unittest.TestCase):
    """Test the class"""
                                                                                # SetUp() method is testing master for all starting with test_

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What is your favoriate programming language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Python', 'C# ', 'C++', 'C']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

print("\n====================")