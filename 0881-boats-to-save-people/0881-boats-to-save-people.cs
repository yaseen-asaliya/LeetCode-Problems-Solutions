public class Solution {
    public int NumRescueBoats(int[] people, int limit) {
        int numOfBoats = 0;
        int remain = 0;
        int p1 = 0;
        int p2 = people.Length - 1;

        Array.Sort(people);

        while (p1<= p2) {
            remain = limit - people[p2];
            p2--;
            numOfBoats += 1;

            if (p1 <= p2 && remain >= people[p1]) {
                p1+=1;
            }
        }
        return numOfBoats;
    }
}