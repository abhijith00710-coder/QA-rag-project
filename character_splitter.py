
from langchain_text_splitters import CharacterTextSplitter

# Sample document
text = """
Artificial Intelligence is transforming modern industries.
It helps computers perform tasks that normally require human intelligence.

Machine Learning is a subset of Artificial Intelligence.
It enables computers to learn patterns from data.

Deep Learning uses neural networks to learn complex patterns.
It is widely used in image recognition and natural language processing.
"""

# Initialize the text splitter
splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=100,
    chunk_overlap=20
)

# Split the document
chunks = splitter.split_text(text)

# Display the chunks
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)
    print("Length:", len(chunk))
    print("-" * 40)

print("Total chunks:", len(chunks))
