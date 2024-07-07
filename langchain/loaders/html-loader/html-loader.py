from langchain_community.document_loaders import UnstructuredHTMLLoader
import nltk
nltk.download('punkt')

html_file_path = "/Users/brais.maneiro/Downloads/htmlCourse/index.html"

loader = UnstructuredHTMLLoader(html_file_path)

data = loader.load()

print("fin")