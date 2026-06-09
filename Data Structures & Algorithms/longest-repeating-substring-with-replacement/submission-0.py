class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        max_f = 0
        max_window = 0
        freq_map = {}

        for r in range(len(s)):

            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            max_f = max(max_f, freq_map[s[r]])

            window_size = r - l + 1

            if window_size - max_f > k:
                freq_map[s[l]] -= 1
                l += 1

            window_size = r - l + 1
            max_window = max(max_window, window_size)
        
        return max_window