import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import statistics as stats
from wordcloud import WordCloud


INCLUDE_COMMON = 500
NUM_WORDS = 1000

happiness = pd.read_csv('./Hedonometer.csv')
english_words = pd.read_csv('./english-word-list-total.csv', delimiter = ";")
too_common = list(english_words['word'][:INCLUDE_COMMON])
stop_words = ["https", "co", "RT", 'amp', '&amp;', 'http', 'thanks'] + too_common

def search(term, most_common, party= "NA", print_out = True):
    #look for word in common words
    hit = [tweet for tweet in most_common if tweet[0].lower() == term.lower()]
    if len(hit) == 0:
        rank = 0
        num = 0
        hit = None
        if print_out:
            print("Not common")
    else:  
        rank = most_common.index(hit[0])
        num = hit[0][1]
        if print_out:
            print(term, "is the ", rank, "most common word for", party,". It was used", num, "times")
    return rank, num, hit

def combine(terms, most_common, party):
    #consider multiple words to be the same
    total = 0
    for term in terms:
        rank, num, hit = search(term, most_common, party, False)
        total += num
        #if rank!= 0:
        #    most_common.remove(hit)
    i = 1
    for pair in most_common:
        if pair[1]>total:
            i+=1
        else:
            break
    print("All together, these words are used", total, "times and rank", i)


def make_word_cloud(tweets, title, exclude = []):
    #create visual of common words
    words = ""
    for item in tweets["Tweet"]:
        if len(item)> 1:
            words = words + item

    
    add_stop_words = stop_words + list(exclude)
        
    word_cloud = WordCloud(min_word_length = 3,stopwords = add_stop_words, collocations = False, background_color = 'white').generate(words)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.title(title, fontsize = 30)
    plt.tight_layout(pad = 0)
     
    plt.show()
    
def sift(common_words):
    most_common = []
    for pair in common_words:
        if pair[0].lower() in stop_words or len(pair[0])< 3:
            pass
        else:
            most_common.append((pair[0].lower(), pair[1]))
    return most_common

def happiness_calculator(words):
    words = [word for word in words if word not in stop_words]
    return happiness[happiness["Word"].isin(words)]

print("preparing variables...")
#Read Tweets, separate by party
tweets = pd.read_csv('./ExtractedTweets.csv')

tweets["Tweet"] =tweets["Tweet"].str.replace('[^\w\s]','')
tweets["Tweet"] =tweets["Tweet"].str.lower()

dem_tweets = tweets[tweets["Party"]=="Democrat"]
rep_tweets = tweets[tweets["Party"]=="Republican"]

hed_dict = {}
hed_words = list(happiness["Word"])
hed_vals =list(happiness["Happiness Score"])
for i in range(len(hed_words)):
    hed_dict[hed_words[i]]= hed_vals[i]


# print("Looking at the whole tweet...")
# tweet_avgs = []
# dem_tweets_test = list(dem_tweets["Tweet"])

# print(len(dem_tweets_test))
# for tweet in dem_tweets_test:
#     accum = 0
#     tweet = tweet.split()
#     for i in range(len(tweet)):            
#         for ele in tweet[i]:
#             if ele in punc:
#                 tweet[i] = tweet[i].replace(ele, "").lower()
#     for word in tweet:
#         if word in too_common:
#             pass
#         else:
#             try:
#                 accum += hed_dict[word]
#             except:
#                 pass
#     tweet_avgs.append(accum/(len(tweet)))
# Dtweet_avgs = tweet_avgs

# plt.hist(Dtweet_avgs)
# plt.title("The whole tweet: Democrat")
# plt.show()

# tweet_avgs = []

# rep_tweets_test = list(rep_tweets["Tweet"])
# for tweet in rep_tweets_test:
#     accum = 0
#     tweet = tweet.split()
#     for i in range(len(tweet)):            
#         for ele in tweet[i]:
#             if ele in punc:
#                 tweet[i] = tweet[i].replace(ele, "").lower()
#     for word in tweet:
#         if word in too_common:
#             pass
#         else:
#             try:
#                 accum += hed_dict[word]
#             except:
#                 pass
#     tweet_avgs.append(accum/(len(tweet)))
# Rtweet_avgs = tweet_avgs


# plt.hist(Rtweet_avgs, color = "red")
# plt.title("The whole tweet: Republican")
# plt.show()


# plt.boxplot([Dtweet_avgs,Rtweet_avgs] , labels=["Democrat", "Republican"])
# plt.show()


#Get most common words and their counts
most_common_dem0 = Counter(" ".join(dem_tweets["Tweet"]).split()).most_common(NUM_WORDS)
most_common_rep0 = Counter(" ".join(rep_tweets["Tweet"]).split()).most_common(NUM_WORDS)

#most_common_dem = [(pair[0].lower(), pair[1]) for pair in most_common_dem0 if pair[0] not in stop_words]
#most_common_rep = [(pair[0].lower(), pair[1]) for pair in most_common_rep0 if pair[0] not in stop_words]
most_common_dem = sift(most_common_dem0)
most_common_rep = sift(most_common_rep0)
print(most_common_dem[:10])

#Could make a whole separate data frame: word, rep_count, dem_count, total_use

data = {"word": [], "dem_count": [], "rep_count": [], "total": []}
dem_counts = []
rep_counts = []
words = []
#dict_try = {}
for pair in most_common_dem[:20]:
    word = pair[0]
    words.append(word)
    dem_counts.append(pair[1])
    rank, rep_count, hit = search(word, most_common_rep, print_out = False)
    rep_counts.append(rep_count)
    data["word"].append(word)
    data["dem_count"].append(pair[1])
    data["rep_count"].append(rep_count)
    data['total'].append(pair[1] + rep_count)
    #dict_try[word] = [dem_counts, rep_counts, dem_counts+rep_counts]
for pair in most_common_rep[:20]:
    word = pair[0]
    words.append(word)
    rep_counts.append(pair[1])
    rank, dem_count, hit = search(word, most_common_dem, print_out = False)
    dem_counts.append(dem_count)
    data["word"].append(word)
    data["dem_count"].append(dem_count)
    data["rep_count"].append(pair[1])
    data['total'].append(dem_count + pair[1])

plt.bar(words, dem_counts, color = "blue")
plt.bar(words, rep_counts, color = "red", bottom = dem_counts)
plt.xticks(rotation = "vertical")
plt.legend(["Democrat Frequency", "Republican Frequency"])
plt.show()   

data = {"word": [], "dem_count": [], "rep_count": [], "total": []}
dem_counts = []
rep_counts = []
words = []
#dict_try = {}
for pair in most_common_dem[:20]:
    word = pair[0]
    words.append(word)
    dem_counts.append(pair[1])
    rank, rep_count, hit = search(word, most_common_rep, print_out = False)
    rep_counts.append(rep_count)
    data["word"].append(word)
    data["dem_count"].append(pair[1])
    data["rep_count"].append(rep_count)
    data['total'].append(pair[1] + rep_count)
    #dict_try[word] = [dem_counts, rep_counts, dem_counts+rep_counts]
for pair in most_common_rep[:20]:
    word = pair[0]
    words.append(word)
    rep_counts.append(pair[1])
    rank, dem_count, hit = search(word, most_common_dem, print_out = False)
    dem_counts.append(dem_count)
    data["word"].append(word)
    data["dem_count"].append(dem_count)
    data["rep_count"].append(pair[1])
    data['total'].append(dem_count + pair[1])

plt.bar(words, dem_counts, color = "blue")
plt.bar(words, rep_counts, color = "red", bottom = dem_counts)
plt.xticks(rotation = "vertical")
plt.legend(["Democrat Frequency", "Republican Frequency"])
plt.show()   



count_df = pd.DataFrame(data) 
print(count_df.head())
count_df = count_df.sort_values(by = ["total"], ascending = False)
print(count_df.head())
plt.bar(count_df["word"], count_df["dem_count"], color = "blue")
plt.bar(count_df['word'], count_df["rep_count"],  bottom = count_df["dem_count"], color = "red")
plt.xticks(rotation = "vertical")
plt.legend(["Democrat Frequency", "Republican Frequency"])
plt.show()


common_dem = [word[0] for word in most_common_dem[:20]]
print(common_dem)
common_rep = [word[0] for word in most_common_rep[:20]]

data = {"word": [], "dem_count": [], "rep_count": [], "total": []}
dem_counts = []
rep_counts = []
words = []
#dict_try = {}
for pair in most_common_dem[:30]:
    if pair[0] not in common_rep:
        word = pair[0]
        words.append(word)
        dem_counts.append(pair[1])
        rank, rep_count, hit = search(word, most_common_rep, print_out = False)
        rep_counts.append(rep_count)
        data["word"].append(word)
        data["dem_count"].append(pair[1])
        data["rep_count"].append(rep_count)
        data['total'].append(pair[1] + rep_count)
        #dict_try[word] = [dem_counts, rep_counts, dem_counts+rep_counts]
for pair in most_common_rep[:30]:
    if pair[0] not in common_dem:
        word = pair[0]
        words.append(word)
        rep_counts.append(pair[1])
        rank, dem_count, hit = search(word, most_common_dem, print_out = False)
        dem_counts.append(dem_count)
        data["word"].append(word)
        data["dem_count"].append(dem_count)
        data["rep_count"].append(pair[1])
        data['total'].append(dem_count + pair[1])

plt.bar(words, dem_counts, color = "blue")
plt.bar(words, rep_counts, color = "red", bottom = dem_counts)
plt.xticks(rotation = "vertical")
plt.legend(["Democrat Frequency", "Republican Frequency"])
plt.show()   



count_df = pd.DataFrame(data) 
print(count_df.head())
count_df = count_df.sort_values(by = ["total"], ascending = False)
print(count_df.head())
plt.bar(count_df["word"], count_df["dem_count"], color = "blue")
plt.bar(count_df['word'], count_df["rep_count"],  bottom = count_df["dem_count"], color = "red")
plt.xticks(rotation = "vertical")
plt.legend(["Democrat Frequency", "Republican Frequency"])
plt.show()

word_freq = []
for pair in most_common_rep:
    #if pair[1]>500:
    word_freq.append(pair[1])

plt.hist(word_freq, alpha = 0.5, color = "red", bins = 16)
#plt.show()

word_freq = []
for pair in most_common_dem:
    #if pair[1]>500:
    word_freq.append(pair[1])

plt.hist(word_freq, alpha = 0.5, bins = 16,color = "blue")
plt.xlabel("Frequency of Word")
plt.show()





#Word Clouds
make_word_cloud(dem_tweets, "Democrats\n")
make_word_cloud(rep_tweets, "Republicans\n")
just_words_dem = [val[0] for val in most_common_dem]

just_words_rep = [val[0] for val in most_common_rep]



make_word_cloud(dem_tweets, "Unique to Democrats\n", just_words_rep)
make_word_cloud(rep_tweets, "Unique to Republicans\n", just_words_dem)


print("implementing search...")
#Search a word
just_words_dem = [word.lower() for word in just_words_dem]
just_words_rep = [word.lower() for word in just_words_rep]
search("gun", most_common_dem, "democrats")
search("gun", most_common_rep, "republicans")



#ALL THIS STUFF: TAKE OUT THE TOO COMMON WORDS
#get subset of happiness data corresponding with most used words
print("examining happiness...")
happiness_scores_dem= happiness_calculator(just_words_dem)
plt.hist(happiness_scores_dem["Happiness Score"])
plt.title("Happiness of Words used by Democrats")
plt.show()
plt.boxplot(happiness_scores_dem["Happiness Score"])
plt.title("Happiness of Words used by Democrats")
plt.show()

happiness_scores_rep = happiness_calculator(just_words_rep)
plt.hist(happiness_scores_rep["Happiness Score"], color = "red")
plt.title("Happiness of Words used by Republicans")
plt.show()
plt.boxplot(happiness_scores_rep["Happiness Score"])
plt.title("Happiness of Words used by Republicans")
plt.show()


print("examining frequency...")
freq_d = []
words = happiness_scores_dem["Word"]
scores_d = happiness_scores_dem["Happiness Score"]
for word in words:
    index0 = just_words_dem.index(word)
    freq_d.append(most_common_dem[index0][1])


plt.scatter(scores_d, freq_d, alpha = 0.2, color = "blue")
#plt.show()

freq_r = []
words = happiness_scores_rep["Word"]
scores_r = happiness_scores_rep["Happiness Score"]
for word in words:
    index0 = just_words_rep.index(word)
    freq_r.append(most_common_rep[index0][1])


        
plt.scatter(scores_r, freq_r, alpha = 0.2, color = "red")
plt.xlabel("happiness")
plt.ylabel("frequency")
plt.legend(["Democrats", "Republicans"])
plt.show()

print("normalizing for frequency...")
normalize = []
Rscores = list(scores_r)
for i in range(len(Rscores)):
    normalize.extend([Rscores[i]]*freq_r[i])

plt.hist(normalize, color = "red")
plt.show()

normalize = []
Dscores = list(scores_d)
for i in range(len(Dscores)):
    normalize.extend([Dscores[i]]*freq_d[i])

plt.hist(normalize)
