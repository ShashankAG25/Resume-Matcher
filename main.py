import time
import os
from process_texts import clean_text, clean_list
from resume_matcher import match_resumes
import csv

print("\n\n\t.......... Resume matcher is running ..........")
path = "DataSet"  # path to Resumes
pathJd = "DataSet/HuggingFaceJD.csv"  # path to Job description


def compare_each_resume(jd, company_name, position):  # Takes the Job description and compare each resume
    results = {}
    for root_dir, sub_dir, files in os.walk(path):
        i = 0
        for file in files:
            if file.endswith(".pdf"):
                if i < 20:  # Comparing only 20 resumes from each category of resumes for testing purpose
                    FilePath = os.path.join(root_dir, file)
                    resume = clean_text(FilePath)  # removing new lines and other unwanted information
                    results[FilePath] = match_resumes(resume, jd)
                    i += 1

    res = dict(sorted(results.items(), key=lambda x: x[1], reverse=True)[:5])
    print("\nTop five matching resumes for the role " + str(position) + " at " + str(company_name) + " are :\n")
    time.sleep(1)
    i = 1
    for key, value in res.items():
        print(str(i) + ". " + str(key) + " matches " + str(value) + "%")
        i += 1
        time.sleep(1)


try:
    with open(pathJd, "r") as f:  # Path to job description
        reader = csv.reader(f, delimiter=",")
        header = next(reader)
        for i, line in enumerate(reader):
            if i < 10:  # only 10 job description for testing
                print("\nPlease wait... Finding the best match for " + str(line[2]) + " at " + str(line[0]))
                get_cleaned = [
                    line[0] + line[2] + line[
                        4]]  # extracting only Company_name, position_title and core_responsibilities
                job_description = clean_list(get_cleaned)  # removing new lines and other unwanted information
                compare_each_resume(job_description, line[0], line[2])
except Exception as e:
    print(e)

print("\nDone!...")
