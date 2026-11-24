# pip install langchain langchain-community pypdf


# from langchain_community.document_loaders import PyPDFLoader

# # 1. Define the PDF path
# pdf_path = "documents/Deep learning.pdf"

# # 2. Initialize the PDF loader
# loader = PyPDFLoader(pdf_path)

# # 3. Load the PDF
# documents = loader.load()

# # 4. Display the number of pages
# print("Total documents:", len(documents))

# # 5. Display the first document
# print("\nPage Content:")
# print(documents[1].page_content)

# # 6. Display its metadata
# print("\nMetadata:")
# print(documents[1].metadata)


###################################################################


from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

# Load all PDF files from a folder
loader = DirectoryLoader(
    "documents/",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

print("Total pages loaded:", len(documents))

for doc in documents:
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))
    print("Content:", doc.page_content[:100])
    print("-" * 50)
