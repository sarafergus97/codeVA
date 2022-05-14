# GRAVEYARD 
# Happiness Calculation
'''
happiness = pd.read_csv('Tweets/Hedonometer.csv')
hed_dict = {}
hed_words = list(happiness["Word"])
hed_vals =list(happiness["Happiness Score"])
for i in range(len(hed_words)):
    hed_dict[hed_words[i]]= hed_vals[i]
def happiness_calculator(words):
    words = [word for word in words if word not in stop_words]
    return happiness[happiness["Word"].isin(words)]

#Average tweet happiness
print("Looking at the whole tweet...")
tweet_avgs = []
dem_tweets_test = list(dem_tweets["Tweet"])

print(len(dem_tweets_test))
for tweet in dem_tweets_test:
    accum = 0
    tweet = tweet.split()
    for i in range(len(tweet)):            
        for ele in tweet[i]:
            if ele in punc:
                tweet[i] = tweet[i].replace(ele, "").lower()
    for word in tweet:
        if word in too_common:
            pass
        else:
            try:
                accum += hed_dict[word]
            except:
                pass
    tweet_avgs.append(accum/(len(tweet)))
Dtweet_avgs = tweet_avgs

plt.hist(Dtweet_avgs)
plt.title("The whole tweet: Democrat")
plt.show()

tweet_avgs = []

rep_tweets_test = list(rep_tweets["Tweet"])
for tweet in rep_tweets_test:
    accum = 0
    tweet = tweet.split()
    for i in range(len(tweet)):            
        for ele in tweet[i]:
            if ele in punc:
                tweet[i] = tweet[i].replace(ele, "").lower()
    for word in tweet:
        if word in too_common:
            pass
        else:
            try:
                accum += hed_dict[word]
            except:
                pass
    tweet_avgs.append(accum/(len(tweet)))
Rtweet_avgs = tweet_avgs


plt.hist(Rtweet_avgs, color = "red")
plt.title("The whole tweet: Republican")
plt.show()


plt.boxplot([Dtweet_avgs,Rtweet_avgs] , labels=["Democrat", "Republican"])
plt.show()

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
'''
# Unordered bar graph
'''
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
'''
#General word frequency
'''
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
'''
'''
dem_counts = []
rep_counts = []
words = []
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
plt.show()   '''
'''
common_dem = [word[0] for word in most_common_dem[:20]]
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

'''