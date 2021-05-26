# Time Complexity: O(N), where N represents number of elements in competitions / results
# Space Complexity: O(K), where K represents number of teams


def tournamentWinner(competitions, results):
    currBestTeam = competitions[0][0]
    teamNamePoints = {currBestTeam: 0}

    for idx, competition in enumerate(competitions):
        homeTeam, awayTeam = competition

        if results[idx] == 1:
            winnerTeam = homeTeam
        else:
            winnerTeam = awayTeam

        if winnerTeam in teamNamePoints:
            teamNamePoints[winnerTeam] += 3
        else:
            teamNamePoints[winnerTeam] = 3

        if teamNamePoints[winnerTeam] > teamNamePoints[currBestTeam]:
            currBestTeam = winnerTeam

    return currBestTeam