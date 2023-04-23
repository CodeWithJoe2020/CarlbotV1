import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import csv
import string

# Open the file in read mode
with open("video_titles.txt", "r") as f:
    # Read all the lines into a list
    video_titles = f.readlines()

# Strip any whitespace characters from the end of each line
video_titles = [title.strip() for title in video_titles]

# Print the video titles
#print(video_titles)
# define the text to be cleaned
text = video_titles

# remove punctuation
text = [word.translate(str.maketrans("", "", string.punctuation)) for word in text]

# lowercase
text = [word.lower() for word in text]

# remove stop words
stop_words = set(stopwords.words("english"))
text = [word for word in text if word not in stop_words]

# stemming/lemmatization
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
text = [stemmer.stem(word) for word in text]
text = [lemmatizer.lemmatize(word) for word in text]

print(text)


# save to CSV file
with open('cleaned_data3.csv', mode='w') as file:
    writer = csv.writer(file)
    for row in text:
        writer.writerow([row])
