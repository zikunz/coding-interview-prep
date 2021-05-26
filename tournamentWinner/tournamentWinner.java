import java.util.*;

class Program {

    public String tournamentWinner(
        ArrayList < ArrayList < String >> competitions, ArrayList < Integer > results) {

        Map < String, Integer > map = new HashMap < String, Integer > ();

        for (int i = 0; i < competitions.size(); i++) {
            String teamName = "";
            if (results.get(i) == 0) {
                teamName = competitions.get(i).get(1);
            } else {
                teamName = competitions.get(i).get(0);
            }
            if (map.containsKey(teamName)) {
                map.put(teamName, map.get(teamName) + 3);
            } else {
                map.put(teamName, 3);
            }
        }

        String winner = Collections.max(map.entrySet(), Comparator.comparingInt(Map.Entry::getValue)).getKey();
        return winner;
    }
}