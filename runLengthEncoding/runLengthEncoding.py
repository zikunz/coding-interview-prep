# Time Complexity: O(N), where N represents length of the input sting
# Space Complexity: O(N), where N represents length of the input sting


def runLengthEncoding(string):
    runLengthEncoding = []
    letterOfInterest = string[0]
    frequency = 1

    for idx in range(1, len(string)):
        if string[idx] != letterOfInterest or frequency == 9:
            runLengthEncoding.append(str(frequency))
            runLengthEncoding.append(letterOfInterest)
            letterOfInterest = string[idx]
            frequency = 0
        frequency += 1

    runLengthEncoding.append(str(frequency))
    runLengthEncoding.append(letterOfInterest)

    return "".join(runLengthEncoding)