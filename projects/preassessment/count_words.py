"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    map = {}
    words = s.split()
    for word in words:
        map[word] = words.count(word)
    
    top_n = [ (k, v) for k, v in map.items() ]
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    top_n = sorted(map.items(), key=lambda x: (-x[1],x[0]))
            
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n[:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()

