class Solution {
    private ArrayList<String> temp;

    public void solve(int idx, String digits, StringBuilder list, HashMap<Integer, String> map) {
        if (idx >= digits.length()) {
            temp.add(list.toString());
            return;
        }
        int num = digits.charAt(idx) - '0';
        String str = map.get(num);
        for (int i = 0; i < str.length(); i++) {
            list.append(str.charAt(i));
            solve(idx + 1, digits, list, map);
            list.deleteCharAt(list.length() - 1);
        }
    }

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) return new ArrayList<>();
        temp = new ArrayList<>();
        StringBuilder list = new StringBuilder();
        HashMap<Integer, String> map = new HashMap<>();
        map.put(2, "abc");
        map.put(3, "def");
        map.put(4, "ghi");
        map.put(5, "jkl");
        map.put(6, "mno");
        map.put(7, "pqrs");
        map.put(8, "tuv");
        map.put(9, "wxyz");

        solve(0, digits, list, map);
        return temp;
    }
}