"""
Implementation of KNN clustering algorithm
"""


def euclidean_distance(point1: tuple, point2: tuple):
    """
    Calculate the euclidean distance between two points
    """
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]

    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

# calculate the distances
def gather_distances(feature1, feature2):
    """
    Calculate the euclidean distance for two vectors.

    Returns the distance between the first data point
    and every point in the data including itself.
    """
    distance = 0.0
    for i in range(len(feature1) - 1):
        distance += (feature1[i] - feature2[i]) ** 2

    return distance**0.5

# find the nieghbors
def get_neighbors(data, test_row, num_nieghbors):
    """
    Calculates the distance between a test row and the remaining data.
    Then sorts the data by distance and returns the n nearnest neighbors.
    """
    distances = []

    for row in data:
        distance = gather_distances(test_row, row)

        distances.append((row, distance))
        distances.sort(key=lambda tup: tup[1])

    neighbors = []

    for index in range(num_nieghbors):
        neighbors.append(distances[index][0])

    return neighbors

def predict_class(train, test_row, num_nieghbors):

    neighbors =  get_neighbors(train, test_row, num_nieghbors)

    # get the last value (class) from the neighbors list of lists
    output = [row[-1] for row in neighbors]

    predicted_class = max(set(output), key=output.count)

    return predicted_class


if __name__ == "__main__":

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

    print("KNN Implementation")

    target = dataset[-1]
    prediction = predict_class(dataset, target, 3)
    print(f'Expected {target[-1]}, Got {prediction}')
