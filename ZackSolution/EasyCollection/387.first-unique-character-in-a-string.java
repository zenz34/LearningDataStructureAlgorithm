class FirstUniqueChar {
  public int firstUniqChar(String s) {
    HashMap<Character, Integer> map = new HashMap<>();

    for (int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);
      map.put(ch, 1 + map.getOrDefault(ch, 0));
    }

    for (int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);
      if (map.get(ch) == 1) {
        return i;
      }
    }

    return -1;
  }
}