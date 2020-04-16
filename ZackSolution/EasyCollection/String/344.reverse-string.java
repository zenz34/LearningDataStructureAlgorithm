class ReverseString {
  public void reverseString(char[] s) {
    reverseString(0, s.length - 1, s);
  }

  private void reverseString(int start, int end, char[] s) {
    if (s == null) {
      return;
    }

    if (start >= end) {
      return;
    }

    char tmp = s[start];
    s[start] = s[end];
    s[end] = tmp;
    reverseString(start + 1, end - 1, s);
  }
}