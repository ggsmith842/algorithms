'''
Knn test file
'''

import unittest
from knn import euclidean_distance, gather_distances, get_neighbors, predict_class
class TestSuite(unittest.TestCase):
    '''
    Run unit tests.
    '''
    dataset = [
        #feature 1, feature 2, class
        [2.7810836, 2.550537003, 0],
        [1.465489372, 2.362125076, 0],
        [3.396561688, 4.400293529, 0],
        [1.38807019, 1.850220317, 0],
        [3.06407232, 3.005305973, 0],
        [7.627531214, 2.759262235, 1],
        [5.332441248, 2.088626775, 1],
        [6.922596716, 1.77106367, 1],
        [8.675418651, -0.242068655, 1],
        [7.673756466, 3.508563011, 1],
    ]

    def test_eculidean_distance(self):
        '''
        Unit test for euclidean distance.
        '''
        self.assertEqual(euclidean_distance((0,0),(3,4)), 5.0)

    def test_gather_distances(self):
        '''
        Test distances for vectors
        '''
        self.assertEqual(gather_distances([3.0, 2.0, 0], [3.0, 2.0,0]), 0.0)

    def test_get_neighbors(self):
        '''
        Test neighbors function
        '''
        self.assertEqual(get_neighbors(self.dataset, self.dataset[0], 1),[[2.7810836, 2.550537003, 0]])
        self.assertEqual(get_neighbors(self.dataset, self.dataset[0], 3),[[2.7810836, 2.550537003, 0],[3.06407232, 3.005305973, 0],[1.465489372, 2.362125076, 0]])
    
    def test_prediction(self):
        '''
        Test prediction function
        '''
        self.assertEqual(predict_class(self.dataset, self.dataset[0], 3), 0)
        self.assertEqual(predict_class(self.dataset, self.dataset[-1], 3), 1)