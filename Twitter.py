

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tweets = pd.read_csv('tweets.csv')

tweets = tweets['Tweet text']
choice = input("Enter [M]entions or [H]ahstags")

mention_dict = {}
hash_dict = {}

if choice == 'm':
    for tweet in tweets:
        for word in tweet.split():  #split each word
            if word.startswith('@'): #find @
                key = word.lower()  #lower word
                if key in mention_dict:
                    mention_dict[key] +=1
                else:
                    mention_dict[key] = 1
    df = pd.DataFrame(list(mention_dict.items()), columns=['Mentions', 'Frequency'])
    print(df)
    print("Sorted Alphabetically")  #alphabetically
    df = df.sort_values(by='Mentions', ascending=True)
    print(df)
    print("Sorted descending by Frequency")   #descending by frequency
    df = df.sort_values(by='Frequency', ascending=False)
    print(df)
    x_pos = np.arange(len(mention_dict.values()))   #start bar plot
    plt.barh(df['Mentions'], x_pos, align="center", alpha =0.5)
    plt.ylabel("Mention")
    plt.xlabel("Frequency")
    plt.title("Popular Mentions")
    plt.show()


elif choice == 'h':
    for tweet in tweets:
        for word in tweet.split():
            if word.startswith('#'):
                key = word.lower()
                if key in hash_dict:
                    hash_dict[key] +=1
                else:
                    hash_dict[key] = 1
    df = pd.DataFrame(list(hash_dict.items()), columns=['Hashtag', 'Frequency'])
    print(df)
    print("Sorted Alphabetically")
    df = df.sort_values(by='Hashtag', ascending=True)
    print(df)
    print("Sorted descending by Frequency")
    df = df.sort_values(by='Frequency', ascending=False)
    print(df)
    x_pos = np.arange(len(hash_dict.values()))
    plt.barh(df['Hashtag'], x_pos, align="center", alpha=0.5)
    plt.ylabel("Hashtag")
    plt.xlabel("Frequency")
    plt.title("Popular Hashtags")
    plt.show()


