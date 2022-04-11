from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import fileIO


def print_analysis_total(positive, negative, neutral):
    print('-----------------------Vader-----------------------------------------------------')
    print("Positive:" + positive)
    print("Negative:" + negative)
    print("Neutral:" + neutral)
    print("-----------------------------------------------------------------------------------")


def print_polarity_result(polarity):
    print("##########Vader###########")
    if polarity > 0:
        print('Positive')
    elif polarity < 0:
        print('Negative')
    elif polarity == 0:
        print('Neutral')
    print("#################################")

def print_results(positive, negative, neutral,total_polarity):
    print_analysis_total(positive, negative, neutral)
    print_polarity_result(total_polarity)

def pie_chart(positive, negative, neutral):
    y = np.array([positive, negative, neutral])
    mylabels = ["Positives", "Negatives", "Neutrals"]
    p, tx, autotexts = plt.pie(y, labels=mylabels,
                               autopct="", shadow=True)

    for i, a in enumerate(autotexts):
        a.set_text("{}".format(y[i]))
    plt.axis('equal')
    plt.show()


def bar_chart(positive, negative, neutral):
    labels = ['positive', 'negative', 'neutral']
    sentiment = [float(positive), float(negative), float(neutral)]
    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots()
    rects = ax.bar(x, sentiment, width, label='pos')
    ax.set_ylabel('number of users')
    ax.set_title('Sentiment analysis result of ')
    ax.set_xticks(x, labels)

    ax.bar_label(rects, padding=3)

    plt.bar(labels, sentiment, color= ['Blue', 'Red', 'green'])
    plt.show()

def create_charts(positive, negative, neutral):
    pie_chart(positive, negative, neutral)
    bar_chart(positive, negative, neutral)

def create_tweet_json_object(tweet,vader_result):
    tweet_json_object = {
        "id": tweet.id,
        "lang": tweet.lang,
        "retweet_count": tweet.retweet_count,
        "favorite_count": tweet.favorite_count,
        "full_text": tweet.full_text,
        "vader_result" : vader_result,
        "by_hand_result" : ""
    }

    return tweet_json_object

def choose_country():
    print("Choose the country you want to analise")
    print("1) America Trend Analysis")
    print("2) Turkey Trend Analysis")
    print("0 to exit")

    while(True):
        try: 
            choice_input = int(input())     
        except:
            print("enter a number")
            continue

        if choice_input < 0 and choice_input > 2:
            print("enter a number from 0 to 2")
            continue

        break

    return choice_input

def remove_stop_words(sentence):
    stop_words = fileIO.read_stop_words()
    tmp_arr = sentence.split(" ")
    sent_arr = sentence.split(" ")
    result = []

    for word in tmp_arr:
        if word in stop_words:
            sent_arr.remove(word)

    result.append(" ".join(sent_arr))
    return " ".join(result)