import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn("English", my_survey.responses)
        
    def test_store_three_responses(self):
        question = "What language did you first learn speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
            
    def setUp(self):
        question= "What language did you first learn to speak?"
        self.my_survey= AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()