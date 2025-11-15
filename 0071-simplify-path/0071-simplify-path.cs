public class Solution
{
    public string SimplifyPath(string path)
    {
        List<string> dicts = new List<string>();
        string temp = "";
        
        for (int i = 0; i < path.Length; i++)
        {
            if (path[i] != '/')
            {
                temp += path[i];
                continue;
            }

            ProcessFolder(temp, dicts);
            temp = "";
        }

        ProcessFolder(temp, dicts);

        return "/" + string.Join("/", dicts);
    }

    private void ProcessFolder(string folder, List<string> dicts)
    {
        if (folder == "" || folder == ".") 
            return;

        if (folder == "..")
        {
            if (dicts.Count > 0)
                dicts.RemoveAt(dicts.Count - 1);
            return;
        }

        dicts.Add(folder);
    }
}
