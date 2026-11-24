
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Sample document
text = """
Artificial Intelligence is transforming modern industries by automating repetitive tasks and improving decision-making.

Machine Learning enables computers to learn patterns from historical data without being explicitly programmed for every task.

Deep Learning uses neural networks to process complex information and is widely used in image recognition and natural language processing.
"""

# Initialize the recursive text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""]
)

# Split the document
chunks = splitter.split_text(text)

# Display the results
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)
    print("Length:", len(chunk))
    print("-" * 40)

print("\nTotal chunks:", len(chunks))
