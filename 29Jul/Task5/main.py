from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

str1 = "Summer is a charming flirt. Easy-going and casual. Summer doesn't huff and puff to win our affections. It has us at \"Hello.\" Winter broods like the tortured protagonist of big fat Russian novels. It is daunting and dramatic, burning with a slow intensity. The season's reputation precedes itself, and often, not in a good way. It has a way of whittling down everything to its bare bones. Even relationships not attuned to its ebbs and flows can fray. At a dinner conversation I once attended, I listened in bemusement as a recent divorcee made the case that it was the Scandinavian frost that had cooled his ex-wife's ardour. How original."

str2 = "One of the finer books I read this year was John Kaag's Hiking With Nietzsche, in which Kaag, a professor of philosophy, rekindles his passion for the German thinker while tracing picturesque hiking trails in the mountains of Switzerland. It's a near-precise rendering of the travelogue as a self-help book. A young Kaag was an avowed Nietzsche acolyte but given the ravages of responsibilities and adulthood, the writer put his affinity to test by undertaking physically enduring hikes through the Alps, revisiting haunts that the philosopher escaped to, in search of solitude and salve. The journey's demands, coupled with his own inner turmoil, are catnip for anybody feeling at cross purposes with their own life."

str3 = "If there's a phrase I would prefer to retire from online bios, personal or professional, it is, \"I love travel.\" Or some approximation of that sentiment. To clarify, I am not against travellers or those who proudly flaunt their passion for travel. On the contrary, editing a travel magazine has now made me oddly protective of travellers and their ilk. My submission is that \"love to travel,\" suggested so casually, just doesn't feel adequate to the depth of emotion it sparks in true devotees. In February, the month of love as endowed by our great gifting industrial complex, we are wrestling with what \"love for travel\" means in tangible, life-affecting terms. The early throes of discovering travel might not be too dissimilar to the beginnings of a feverish affair. A fleeting scene, sound or feeling that at first arouses, then enchants and eventually lures us into a hypnotic state, evoking wooly-eyed reveries about what could be."

vect = TfidfVectorizer(binary = True)

corpus = [str1, str2, str3]
vect.fit(corpus)

vecstr1 = vect.transform([str1]).toarray()
vecstr2 = vect.transform([str2]).toarray()
vecstr3 = vect.transform([str3]).toarray()
sim = cosine_similarity(vecstr1, vecstr2)
print(sim)
print('Cosine similarity between text 1 and 2:', cosine_similarity(vecstr1, vecstr2))

print('Cosine similarity between text 2 and 3:', cosine_similarity(vecstr2, vecstr3))

print('Cosine similarity between text 1 and 3:', cosine_similarity(vecstr1, vecstr3))
