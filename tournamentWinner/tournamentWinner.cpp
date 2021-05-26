#include <bits/stdc++.h>

using namespace std;
typedef pair<string, int> si;
#define homeTeamWon 1

string tournamentWinner(vector<vector<string>> competitions, vector<int> results) {

    unordered_map<string, int> teamName_score;
    string currentBestTeam = "";
    teamName_score.insert({currentBestTeam, 0});
    int size = competitions.size();
    string winningTeam;

    for (int i = 0; i < size; ++i) {
        if (results[i] == homeTeamWon) {
            winningTeam = competitions[i][0];
        }
        else {
            winningTeam = competitions[i][1];
        }
        unordered_map<string, int>::iterator it = teamName_score.find(winningTeam);
        if (it != teamName_score.end()) {
            (*it).second += 3;
        }
        else {
            teamName_score.insert({ winningTeam, 3});
        }
        if (teamName_score[winningTeam] > teamName_score[currentBestTeam]) {
            currentBestTeam = winningTeam;
        }
    }

    return currentBestTeam;
}
