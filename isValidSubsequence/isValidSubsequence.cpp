using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence) {
    int sequence_index = 0;

    for (auto i = array.begin(); i != array.end(); ++i) {
        if (*i == sequence[sequence_index]) {
            sequence_index++;
        }
    }

    if (sequence_index == sequence.size()) {
        return true;
    }
    else {
        return false;
    }
}
