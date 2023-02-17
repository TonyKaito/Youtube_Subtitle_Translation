import os
import spacy
from collections import Counter
from youtube_transcript_api import YouTubeTranscriptApi

nlp = spacy.load("ja_core_news_sm")
print(nlp.Defaults.stop_words)

transcript_list = YouTubeTranscriptApi.list_transcripts("53me-ICi_f8")
transcript_data = transcript_list.find_manually_created_transcript(['ja', 'zh-Hant'])
transcript = transcript_data.fetch()
print(transcript)

sentences = []
for i in range(len(transcript)):
  sentences.append(transcript[i]['text'])

print(sentences)

word_list = [nlp(sentence) for sentence in sentences]
words = []
for i in range(len(word_list)):
  for j in range(len(word_list[i])):
    if word_list[i][j].lemma_ not in nlp.Defaults.stop_words and not word_list[i][j].is_punct:
      words.append(word_list[i][j].lemma_)

print(words, Counter(words))



