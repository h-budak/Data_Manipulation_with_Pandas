import pandas as pd
# Loading the data and investigating it
jeopardy_data = pd.read_csv("jeopardy.csv")
#print(jeopardy_data.columns)

# Renaming misformatted columns
jeopardy_data = jeopardy_data.rename(columns = {" Air Date": "Air Date", " Round" : "Round", " Category": "Category", " Value": "Value", " Question":"Question", " Answer": "Answer"})
#print(jeopardy_data.columns)
#print(jeopardy_data["Question"])

# Filtering a dataset by a list of words
def filter_data(data, words):
  # Lowercases all words in the list of words as well as the questions. Returns true is all of the words in the list appear in the question.
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  # Applies the labmda function to the Question column and returns the rows where the function returned True
  return data.loc[data["Question"].apply(filter)] 

# Testing the filter function
filtered = filter_data(jeopardy_data, ["King", "England"])
print(filtered["Question"]) 