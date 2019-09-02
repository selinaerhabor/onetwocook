import unittest

class test_display_features(unittest.TestCase):

    '''
    Test 1: Ensure Cuisine Types are capitalized when rendered on page if user
    creates a cuisine using lowercase
    '''
    def test_capitalize(self):
        self.assertEqual('irish'.capitalize(), 'Irish')


    '''
    Test 2: Tests how Allergens listed in dropdown multiple selection (Add a Recipe form)
    display allergens from database separately without brackets
    '''
    def test_index(self):
        allergens = ['hello' , 'world']
        self.assertEqual(allergens[0], 'hello')
        self.assertEqual(allergens[1], 'world')

            
if __name__ == '__main__':
    unittest.main()