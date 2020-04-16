class ValidAnagram {
  public boolean isAnagram(String s, String t) {
    HashMap<Character, Integer> map = new HashMap<>();

    for (int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);
      map.put(ch, 1 + map.getOrDefault(ch, 0));
    }

    for (int i = 0; i < t.length(); i++) {
      char ch = t.charAt(i);

      if (!map.containsKey(ch)) {
        return false;
      } else {
        int count = map.get(ch) - 1;
        if (count == 0) {
          map.remove(ch);
        } else {
          map.put(ch, count);
        }
      }
    }

    return map.size() == 0 ? true : false;
  }
}