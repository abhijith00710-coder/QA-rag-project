
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence is transforming modern industries.
Machine Learning is a subset of Artificial Intelligence.
Deep Learning uses neural networks to learn complex patterns.
Natural Language Processing helps computers understand human language.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)
    print("Length:", len(chunk))
