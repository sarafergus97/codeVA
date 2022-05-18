####### IMPORT LIBRARIES #######
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

####### CONSTANTS #######
INCLUDE_COMMON = 500
NUM_WORDS = 1000

####### FUNCTIONS #######

# Helper Functions
def sift(common_words):
    #get most common words that are not in stopwords or too short
    most_common = []
    for pair in common_words:
        if pair[0].lower() in stop_words or len(pair[0])< 3:
            pass
        else:
            most_common.append((pair[0].lower(), pair[1]))
    return most_common

def search(term, most_common, party= "NA", print_out = True):
    # Seach for a word to determine rank and number of occurances
    hit = [tweet for tweet in most_common if tweet[0].lower() == term.lower()]
    if len(hit) == 0: #word is not in list of common words
        print("Not Common")
        return 0, 0, None
    rank = most_common.index(hit[0]) #word is common
    num = hit[0][1]
    if print_out:
        print(term, "is the ", rank, "most common word for", party,". It was used", num, "times")
    return rank, num, hit

def build_df(data, most_commonp1, most_commonp2, p1, p2, num = 20):
    #build data frame of words and counts (DF created outside of function)
    for pair in most_commonp1[:num]:
        word = pair[0]
        rank, count2, hit = search(word, most_commonp2, print_out = False)
        data["word"].append(word)
        data[p1].append(pair[1])
        data[p2].append(count2)
        data['total'].append(pair[1] + count2)
    return data

# Visualization Functions
def make_word_cloud(tweets, title, exclude = []):
    #create visual of common words
    words = ""
    for item in tweets["Tweet"]:
        #only include words greater than one letter
        if len(item)> 1: 
            words = words + item
    #do not include stop_words (constant) or passed in exclusion words
    add_stop_words = stop_words + list(exclude) 
    #create and show word cloud
    word_cloud = WordCloud(min_word_length = 3,stopwords = add_stop_words, collocations = False, background_color = 'white').generate(words)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.title(title, fontsize = 30)
    plt.tight_layout(pad = 0)
    plt.show()

def make_bar_graph(count_df):
    #create bar graph of most used words, broken by party
    plt.bar(count_df["word"], count_df["dem count"], color = "blue")
    plt.bar(count_df['word'], count_df["rep count"],  bottom = count_df["dem count"], color = "red")
    plt.xticks(rotation = "vertical")
    plt.subplots_adjust(bottom=0.3)
    plt.title("Common Word Frequency by Party")
    plt.ylabel("Number of Uses")
    plt.legend(["Democrat Frequency", "Republican Frequency"])
    plt.show()


####### READ IN DATA #######
print("Preparing...")
english_words = pd.read_csv('Tweets/english-word-list-total.csv', delimiter = ";")
tweets = pd.read_csv('Tweets/ExtractedTweets.csv')

####### PREPARE DATA #######
too_common = list(english_words['word'][:INCLUDE_COMMON])
too_common = [i for i in too_common if type(i)==str]
stop_words = ["https", "co", "RT", 'amp', '&amp;', 'http', 'thanks'] + too_common

tweets["Tweet"] =tweets["Tweet"].str.replace('[^\w\s]','')
tweets["Tweet"] =tweets["Tweet"].str.lower()

# Subsets of the dataframe by party
dem_tweets = tweets[tweets["Party"]=="Democrat"]
rep_tweets = tweets[tweets["Party"]=="Republican"]

#Get most common words and their counts
most_common_dem0 = Counter(" ".join(dem_tweets["Tweet"]).split()).most_common(NUM_WORDS)
most_common_rep0 = Counter(" ".join(rep_tweets["Tweet"]).split()).most_common(NUM_WORDS)
most_common_dem = sift(most_common_dem0)
most_common_rep = sift(most_common_rep0)

#Get just the words
just_words_dem = [val[0] for val in most_common_dem]
just_words_rep = [val[0] for val in most_common_rep]

####### FUNCTION CALLS #######
print("Making word clouds...")
#Word Clouds: Basic
#make_word_cloud(dem_tweets, "Democrats\n")
#make_word_cloud(rep_tweets, "Republicans\n")
#Word Clouds: Excluse most common in other party
#make_word_cloud(dem_tweets, "Unique to Democrats\n", just_words_rep)
#make_word_cloud(rep_tweets, "Unique to Republicans\n", just_words_dem)

#Bar Graph
'''
print("Making bar graph...")
data = {"word": [], "dem count": [], "rep count": [], "total": []}
data = build_df(data, most_common_dem, most_common_rep, "dem count", "rep count")
data = build_df(data, most_common_rep, most_common_dem, "rep count", "dem count")
count_df = pd.DataFrame(data) 
count_df = count_df.sort_values(by = ["total"], ascending = False)
#make_bar_graph(count_df)

#Search a word
print("implementing search...")
just_words_dem = [word.lower() for word in just_words_dem]
just_words_rep = [word.lower() for word in just_words_rep]
search("Trump", most_common_dem, "democrats")
search("Trump", most_common_rep, "republicans")

try_all = Counter(" ".join(tweets["Tweet"]).split()).most_common(NUM_WORDS)
try_all = sift(try_all)
print(try_all[:10])
'''

for item in dem_tweets["Tweet"]:
    if "republicans" in item:
        print(item)
        print()