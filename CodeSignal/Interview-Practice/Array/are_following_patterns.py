# https://app.codesignal.com/interview-practice/task/3PcnSKuRkqzp8F6BN/solutions
def areFollowingPatterns(strings, patterns):
    string_to_pattern = {}
    pattern_to_string = {}
    for i in range(len(strings)):
        pattern = patterns[i]
        string = strings[i]
        if string in string_to_pattern:
            if pattern == string_to_pattern[string]:
                continue
            else:
                return False
        else:
            string_to_pattern[string] = pattern
            
        if pattern in pattern_to_string:
            if string == pattern_to_string[pattern]:
                continue
            else:
                return False
        else:
            pattern_to_string[pattern] = string

    return True
