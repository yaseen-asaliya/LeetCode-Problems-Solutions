public class Solution {
    public IList<string> SubdomainVisits(string[] cpdomains) {
        Dictionary<string, int> dict = new Dictionary<string, int>();
        IList<string> res = new List<string>();

        for (int i = 0; i < cpdomains.Length; i++) {
            string[] temp = cpdomains[i].Split(' ');
            string[] subDomains = temp[1].Split('.');
            string tempSubDomain = "";
            string prevSubDomain = "";
            int tempLen = subDomains.Length;

            for (int j = tempLen - 1; j >= 0; j--) {
                if (j == tempLen - 1)
                    tempSubDomain = subDomains[j];
                else
                    tempSubDomain = subDomains[j] + "." + prevSubDomain;

                if (!dict.ContainsKey(tempSubDomain)) {
                    dict[tempSubDomain] = Convert.ToInt32(temp[0]);
                }
                else {
                    dict[tempSubDomain] += Convert.ToInt32(temp[0]);
                }
                prevSubDomain = tempSubDomain;
            }
        }

        foreach (var t in dict) {
            res.Add(t.Value.ToString() + " " + t.Key);
        }

        return res;
    }
}