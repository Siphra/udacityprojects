# Wrangling class load
import pandas as pd
import requests
from bs4 import BeautifulSoup
import glob
import sqlalchemy
from sqlalchemy import create_engine


df = pd.read_csv(r"I:\python\pycharmprojects\udacityproject1\csv from classes\bestofrt.tsv" , sep='\t')
print(df.head())

url = 'https://www.rottentomatoes.com/m/et_the_extraterrestrial'
response = requests.get(url)           # use requests to get the html

with open("et_the_extraterrestrial.html", mode='wb') as file:
    file.write(response.content)       # save file downloaded from requests

soup = BeautifulSoup(response.content, 'lxml') #create variable to hold response from above, and use with BeautifulSoup

print(soup.find('title').contents)

'''
# List of dictionaries to build file by file and later convert to a DataFrame
df_list = []
folder = 'rt_html'
for movie_html in os.listdir(folder):
    with open(os.path.join(folder, movie_html)) as file:
        # Your code here
        soup = BeautifulSoup(file, 'lxml')
        title = soup.find('title').contents[0][:-len(' - Rotten Tomatoes')]
        audience_score = soup.find('div', class_='audience-score meter').find('span').contents[0][:-1]
        num_audience_ratings = soup.find('div', class_='audience-info hidden-xs superPageFontColor').find_all('div')[1].contents[2].strip().replace(',','')
        # Note: a correct implementation may take ~15 seconds to run
        
        
        # Append to list of dictionaries
        df_list.append({'title': title,
                        'audience_score': int(audience_score),
                        'number_of_audience_ratings': int(num_audience_ratings)})
df = pd.DataFrame(df_list, columns = ['title', 'audience_score', 'number_of_audience_ratings'])
'''

'''
USING GLOB
df_list = []
for ebert_review in glob.glob('ebert_reviews/*.txt'):
    with open(ebert_review, encoding='utf-8') as file:
        title = file.readline()[:-1]
        # Your code here
        review_url = file.readline()[:-1]
        review_text = file.read()    
        

        # Append to list of dictionaries
        df_list.append({'title': title,
                        'review_url': review_url,
                        'review_text': review_text})
df = pd.DataFrame(df_list, columns = ['title', 'review_url', 'review_text'])
df.head()
'''

'''

Try not to use REQUESTS library for images, use PIL and IO libraries as below : 

from PIL import Image
from io import BytesIO
r = requests.get(url)
i = Image.open(BytesIO(r.content))
'''

'''
SQLAlchemy :
CONNECT:

# Create SQLAlchemy Engine and empty bestofrt database
# bestofrt.db will not show up in the Jupyter Notebook dashboard yet
engine = create_engine('sqlite:///bestofrt.db')

STORE:
# Store cleaned master DataFrame ('df') in a table called master in bestofrt.db
# bestofrt.db will be visible now in the Jupyter Notebook dashboard
df.to_sql('master', engine, index=False)

READ:
df_gather = pd.read_sql('SELECT * FROM master', engine)
'''

def gather(source,out_name):

    """
    This function is used to pull in any generic data type and output a file to be used later for analysis
    The intent of this function is to prevent abuse in scraping or downloading files and to provide a
    generic input/output for the file(s) being produced.

    :param source:  The source, file, URL, etc. for data to be brought in and saved locally.
    :return: out_name.EXT a file will be produced which has the appropriate extension
    """
    import requests as req
    from bs4 import BeautifulSoup as BS
    import glob
    source = str(source)
    out_name = str(out_name)
    try:
        if source == '*.?sv'
            delimit = source.Sniffer()
            file = pd.read_csv(source, sep = delimit)
            file.to_csv(out_name, delimiter = delimit )
        elif source == 'http*':
            r = req.get(source)
            file = open(r(out_name + '.txt'), 'w')
            file.write(r.content())
            file.close()
        else:
            print("File Format not supported in this function")
    except:
        print("something went wrong hoss")

gather('I:\python\pycharmprojects\udacityproject1\csv from classes\twitter-archive-enhanced.csv',wrangle_project)






