from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resumes(resume, jd):  # Compares resume and job description and returns match_Percentage
    match_Test = [resume, jd]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(match_Test)

    match_Percentage = cosine_similarity(count_matrix)[0][1] * 100
    match_Percentage = round(match_Percentage, 2)
    return match_Percentage
