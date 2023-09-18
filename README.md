
# Resume Matcher using CountVectorizer

CountVectorizer is used to transform a given text into a vector on the basis of the frequency (count) of each word that occurs in the entire text. CountVectorizer creates a matrix in which each unique word is represented by a column of the matrix, and each text sample from the document is a row in the matrix. The value of each cell is nothing but the count of the word in that particular text sample. CountVectorizer fit_transform is used to get the cosine similarity between resume information and job description informations.


## PROPOSED METHOD

* Extract Company_name, position_title and core_responsibilities fields for each job description from the Hugging-face dataset using csv reader.
* Process the extracted job description. Remove the new lines and other unwanted information.
* Traverse resume dataset and extract the texts from resumes using PyPDF2 and pdfplumber.
* Process the extracted  text form resumes, Remove the new lines and other unwanted information.
* Compare the processed resume texts to processed job descriptions using CountVectorizer.fit_transform().
* Store the resume details and cosine similarity value returned from CountVectorizer.fit_transform() in a result dictionary.
* To get top five matching resumes sort the result list in descending order and display first five resumes and its matching score.













## Run Locally

Clone the project

```bash
  git clone https://github.com/ShashankAG25/Resume-Matcher.git
```

Go to the project directory

```bash
  cd Resume-Matcher
```

Install dependencies

```bash
 pip install PyPDF2
```
```bash
 pip install pdfplumber
```
```bash
 pip install -U scikit-learn
```

Update the path in main.py and run

```bash
  python3 main.py
```



## Screenshots

![Results]file:///home/shashank/Pictures/Screenshots/Screenshot%20from%202023-09-18%2013-10-52.png


