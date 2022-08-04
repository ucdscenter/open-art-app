import pickle
import vptree
from similar_art.similar_tree import *


tree = pickle.load(open('similar_art/data/wikiarts_tree.txt', 'rb'))

query_path = '../../wikiarts/Baroque/aleksey-antropov_portrait-of-anna-vasiliyevna-buturlina.jpg'
results = extract_similar_images(query_path, tree)
print(similar_image_paths(results))



