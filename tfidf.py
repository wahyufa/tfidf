import math

def tf(n_terms, total_terms):
	tf = n_terms / total_terms
	return tf

def idf(n_docs, n_docs_with_term):
    idf = math.log10(n_docs/n_docs_with_term)
    return idf