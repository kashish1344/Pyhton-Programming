text_1='''
Born on December 27, 1965 Salman Khan is the son of the legendary writer Salim Khan,
who penned many super-hits in the yesteryear's like Sholay (1975), Deewaar (1975), and Don (1978). 
Salman started his acting carrier in 1988 by doing a supporting role in the movie Biwi Ho To Aisi (1988). 
The following year he had the leading role in the box office romantic hit When Love Calls (1989). 
From there he became a heart throb of Indian cinema.
'''

text_2 = '''
Abdul Rashid Salim Salman Khan (pronounced (About this soundlisten); 27 December 1965) is an Indian actor, producer, singer, painter and television personality who works in Hindi films.
In a film career spanning over thirty years, Khan has received numerous awards, including two National Film Awards as a film producer, and two Filmfare Awards for acting. 
He is cited in the media as one of the most commercially successful actors of Indian cinema. Forbes included him in their 2015 list of Top-Paid 100 Celebrity Entertainers in the world;
Khan tied with Amitabh Bachchan for No. 71 on the list, both with earnings of $33.5 million. 
According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, 
Khan was the highest-ranked Indian with 82nd rank with earnings of $37.7 million.
He is also known as the host of the reality show, Bigg Boss since 2010
 
'''

def pre_process(text):
    tokens = text.lower().split()
    stopwords = ['a','as','are','by','of','this','the','that','was','is',
                 'in','it','for','at','to','be','on','also','has','been','and',
                 'its','can','often','with','use','used']

    words=[]
    for token in tokens:
        if token not in stopwords:
            words.append(token)
    print(words)
    return  set(words)

set_1 = pre_process(text_1)
set_2 = pre_process(text_2)

sim = len(set_1.intersection(set_2)) / len(set_1.union(set_2))
print(round(sim, 2) * 100)