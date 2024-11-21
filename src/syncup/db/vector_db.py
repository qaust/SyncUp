"""
Creates a vector db for clinical trial descriptions
"""

import  chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="test_collection")