"""Generate Markov text from text files."""

from random import choice
import sys



def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

    
    return text


def make_chains(text_string, n_count):
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> chains = make_chains('hi there mary hi there juanita')
    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words_list = text_string.split()


    # your code goes here
    for i in range(len(words_list)-1):
        if i+n_count <= len(words_list)-1:
            current_key = tuple(words_list[i:i+n_count])
            if current_key not in chains:
                chains[current_key] = list([words_list[i + n_count]])
            if current_key in chains:

                chains[current_key] += ([words_list[i + n_count]])
        else:
            continue
    print(chains)
    return chains

def make_text(chains, n_count):
    """Return text from chains."""

    words = []
    keys_list = list(chains.keys())
    cur_key = choice(keys_list)
    words.extend(cur_key)
    while len(words) < n_count and cur_key in chains:
        next = choice(chains[cur_key])
        words.append(next)
        cur_key = cur_key[1:] + (next,)

    words= ' '.join(words)
    # print(words)
    return words


#input_path = 'adventure_time.txt'
input_path = "green_eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
# random_text = make_text(chains, 4)

# print(random_text)
