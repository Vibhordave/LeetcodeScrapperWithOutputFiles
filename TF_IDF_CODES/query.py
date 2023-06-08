import math,os,chardet



current_dir = os.path.dirname(os.path.abspath(__file__))
sibling_dir = os.path.join(current_dir, "..", "Qdata")
txt_dir = os.path.join(current_dir, "..", "Text_files")

index_path=os.path.join(sibling_dir,"index.txt")
data_path=os.path.join(current_dir,"..","TF_IDF_DATA")

vocab_file=os.path.join(data_path,"vocab.txt")
idf_file=os.path.join(data_path,"idf-values.txt")
doc_file=os.path.join(data_path,"documents.txt")
inverted_file=os.path.join(data_path,"inverted-index.txt")


def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

my_encoding = find_encoding(index_path)

def load_vocab():
    vocab = {}
    with open(vocab_file, 'r',encoding=my_encoding) as f:
        vocab_terms = f.readlines()
    with open(idf_file, 'r',encoding=my_encoding) as f:
        idf_values = f.readlines()
    
    for (term,idf_value) in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())
    
    return vocab

def load_documents():
    documents = []
    with open(doc_file, 'r',encoding=my_encoding) as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]

    print('Number of documents: ', len(documents))
    # print('Sample document: ', documents[0])
    return documents

def load_inverted_index():
    inverted_index = {}
    with open(inverted_file, 'r',encoding=my_encoding) as f:
        inverted_index_terms = f.readlines()

    for row_num in range(0,len(inverted_index_terms),2):
        term = inverted_index_terms[row_num].strip()
        documents = inverted_index_terms[row_num+1].strip().split()
        inverted_index[term] = documents
    
    print('Size of inverted index: ', len(inverted_index))
    return inverted_index



vocab_idf_values = load_vocab()
documents = load_documents()
inverted_index = load_inverted_index()


def get_tf_dictionary(term):
    tf_values = {}
    if term in inverted_index:
        for document in inverted_index[term]:
            if document not in tf_values:
                tf_values[document] = 1
            else:
                tf_values[document] += 1
                
    for document in tf_values:
        tf_values[document] /= len(documents[int(document)])
    
    return tf_values

def get_idf_value(term):
    return math.log(len(documents)/vocab_idf_values[term])

def doc_name(ind):
    with open(index_path,'r',encoding=my_encoding) as new:
        lines=new.readlines()
        
    return lines[ind]

def calculate_sorted_order_of_documents(query_terms):
    potential_documents = {}
    for term in query_terms:
        if vocab_idf_values[term] == 0:
            continue
        tf_values_by_document = get_tf_dictionary(term)
        idf_value = get_idf_value(term)
        # print(term,tf_values_by_document,idf_value)
        for document in tf_values_by_document:
            if document not in potential_documents:
                potential_documents[document] = tf_values_by_document[document] * idf_value
            else :potential_documents[document] += tf_values_by_document[document] * idf_value

    # print(potential_documents)
    # divite by the length of the query terms
    for document in potential_documents:
        potential_documents[document] /= len(query_terms)

    potential_documents = dict(sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))
    i=0
    for document_index in potential_documents:
        if i<11 :print('Document: ', doc_name(int(document_index)), ' Score: ', potential_documents[document_index])
        else: break
        i+=1


query_string = input('Enter your query: ')
query_terms = [term.lower() for term in query_string.strip().split()]

# print(query_terms)
calculate_sorted_order_of_documents(query_terms)