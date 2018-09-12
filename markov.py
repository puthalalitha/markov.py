"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()


    return contents
print(open_and_read_file("green-eggs.txt"))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    chains = {}
    for i in range(len(words)- 2):
        key = (words[i], words[i+1])
        value= words[i + 2]

        if key in chains:

            chains[key].append(value)
        else:
            chains[key] = [value]


    #print (chains)
    return chains
#print("$$$$$$$$$$$$$$$$$$")
make_chains(open_and_read_file("green-eggs.txt"))

def make_text(chains):
    """Return text from chains."""

    words = []#create empty list
    random_key = choice(list(chains.keys()))# creating random key from dictionaru
    words.extend(list(random_key))#append the random value of random key to word_list
    #random_value = choice(list(chains[random_key]))
    #random_value = choice(list(chains[random_key]))
    #print("***********")
    #print(random_key)
    #print(random_value)

    while random_key in chains:#loop through all random keys and produce value
        random_value = choice(chains[random_key])
        words.append(random_value)#append the random value of random key to word_list
            

        next_key = (random_key[1], random_value)
        random_key = next_key

        # if next_key in chains:
        #     words.append(str(next_key))#append the random key into word_list
        #     words.append(random_value)#append the random value of random key to word_list
        #     #print(words)



    #print(next_key)
    
    #words.append(str(next_key))#append the random key into word_list
    #words.append(random_value)#append the random value of random key to word_list



    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
