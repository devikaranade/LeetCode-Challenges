class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # joe -> 1 -> home
        # joe -> 2 -> about 
        # joe -> 3 -> career

        # james -> 4 -> home
        # james -> 5 -> cart
        # james -> 6 -> maps
        # james -> 7 -> home

        # mary -> 8 -> home
        # mary -> 9 -> about
        # mary -> 10 -> career

        users = defaultdict(list)
        pattern_count = defaultdict(int)
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x:(x[0], x[1])):
            users[user].append(site)
        
        for user, hist in users.items():
            patterns = set(combinations(hist,3))
            for pattern in patterns:
                pattern_count[pattern]+=1

        print(pattern_count)

        max_count = max(pattern_count.values())
        print(max_count)
        
        most_common = [pattern for pattern in pattern_count if pattern_count[pattern] == max_count]

        
        return sorted(most_common)[0]
        
        
