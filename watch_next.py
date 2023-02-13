import spacy
nlp = spacy.load('en_core_web_md')

def suggestion(desc):

    desc = nlp(desc)

    # establish storage variable for movies in text file movies.txt
    movies = []

    # establish storage variable for highest similarity movie
    movie_similarity = 0
    movie = None

    # open and store data from movies.txt
    with open ("movies.txt", "r") as f:
        lines = f.readlines()
    
        for line in lines:
            movies.append(line)

    for token in movies:
        token_ = nlp(token[9:])
        
        # check similarity
        if desc.similarity(token_) > movie_similarity:
            movie_similarity = desc.similarity(token_)
            movie = token[0:9]

    return movie

print(suggestion('''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''))

    