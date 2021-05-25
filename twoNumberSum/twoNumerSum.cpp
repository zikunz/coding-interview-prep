#include <unordered_set>

#include <vector>

using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum)
{
    unordered_set<int> hash_table;
    vector<int> answer;

    for (auto i = array.begin(); i != array.end(); ++i)
    {
        hash_table.insert(*i);
    }

    for (auto i = array.begin(); i != array.end(); ++i)
    {
        auto got = hash_table.find((targetSum - *i));
        if (got != hash_table.end() && (*i != *got))
        {
            answer.push_back(*i);
            answer.push_back(*got);
            return answer;
        }
    }

    return answer;
}