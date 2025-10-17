public class MyHashSet {
    private List<int> set;

    public MyHashSet() {
        set = new List<int>();
    }
    
    public void Add(int key) {
        foreach (int x in set) {
            if (x == key){
                return;
            }
        }
        set.Add(key);
    }
    
    public void Remove(int key) {
        for (int i = set.Count - 1; i >= 0; i--) {  
            if (set[i] == key) {
                set.RemoveAt(i);
            }
        }
    }
    
    public bool Contains(int key) {
        foreach (int x in set) {
            if (x == key){
                return true;
            }
        }
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.Add(key);
 * obj.Remove(key);
 * bool param_3 = obj.Contains(key);
 */