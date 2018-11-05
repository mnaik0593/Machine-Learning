import math
from collections import Counter
from nltk.corpus import stopwords

vector_dict = {}

def load_docs():
    print("Loading Documents")
    Doc1 = ('d1','Instead of going to Starbucks I can make a coffee at home which can help me save my money')
    Var1 = ('d2','with huge memory and a great power backup dell is on of the best laptops')
    Var2 = ('d3','I am using dell for the past five years and its simply amazing huge memory space')
    Var3 = ('d4','Dell is the Superb Combination of massive memory, great power backup and fastest RAM')
    Var4 = ('d5','Best laptop to buy at affordable price with huge memory space')
    Var5 = ('d6','Dell provides great features with long battery life and fastest RAMP')
    return(Doc1,Var1,Var2,Var3,Var4,Var5)
    
def process_docs(all_dcs):
 stop_words = stopwords.words('english')
 all_words = []                                         
 counts_dict = {}                                       
 for doc in all_dcs:
    words = [x.lower() for x in doc[1].split() if x not in stop_words]
    words_counted = Counter(words)                      
    unique_words = list(words_counted.keys())           
    counts_dict[doc[0]] = words_counted                 
    all_words = all_words + unique_words                       
 n = len(counts_dict)                                     
 df_counts = Counter(all_words)                          
 compute_vector_len(counts_dict, n, df_counts)       
    
def compute_vector_len(doc_dict, no, df_counts):
  global vector_dict
  for doc_name in doc_dict:                                      
    doc_words = doc_dict[doc_name].keys()                #get all the unique words in the doc
    wd_tfidf_scores = {}
    for wd in list(set(doc_words)):                      #for each word in the doc
        wds_cts = doc_dict[doc_name]                     #get the word-counts-dict for the doc
        wd_tf_idf = wds_cts[wd] * math.log(no / df_counts[wd], 10)   #compute TF-IDF
        wd_tfidf_scores[wd] = round(wd_tf_idf, 4)        #store Tf-IDf scores with word
    vector_dict[doc_name] = wd_tfidf_scores 
    
    
def get_cosine(text1, text2):
     vec1 = vector_dict[text1]
     vec2 = vector_dict[text2]
     intersection = set(vec1.keys()) & set(vec2.keys())
     #NB strictly, this is not really correct, needs vector of all features with zeros
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     if not denominator:
        return 0.0
     else:
        return round(float(numerator) / denominator, 3)

all_docs = load_docs()
process_docs(all_docs)
for keys,values in vector_dict.items(): print(keys, values)
text1 = 'd1'
text2 = 'd2'
cosine = get_cosine(text1, text2)
print('Cosine for doc1 and var1:', cosine)
text1 = 'd1'
text2 = 'd3'
cosine = get_cosine(text1, text2)
print('Cosine for doc1 and var2:', cosine)
text1 = 'd1'
text2 = 'd4'
cosine = get_cosine(text1, text2)
print('Cosine for doc1 and var3:', cosine)
text1 = 'd1'
text2 = 'd5'
cosine = get_cosine(text1, text2)
print('Cosine for doc1 and var4:', cosine)
text1 = 'd1'
text2 = 'd6'
cosine = get_cosine(text1, text2)
print('Cosine for doc1 and var5:', cosine)



