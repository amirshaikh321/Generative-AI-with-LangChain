from langchain_text_splitters import CharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader

text = """The Royal Challengers Bangalore, popularly known as RCB, is more than just an IPL team — it’s an emotion wrapped in red and gold. Every season begins with roaring optimism, bold team combinations, and the unshakable belief that this year is the year. From electrifying starts to nail-biting finishes, RCB matches rarely lack drama.

What truly sets RCB apart is its loyal fanbase. Win or lose, the chants echo through the M. Chinnaswamy Stadium and across social media, turning every match into a festival. The team has always been known for its aggressive brand of cricket, explosive batting line-ups, and moments of individual brilliance that stay etched in IPL history.

RCB’s journey has had its fair share of heartbreaks and near-misses, but that’s what makes supporting them special. Hope is never in short supply, and every new season feels like a fresh script waiting to be written. In the IPL, RCB stands as a symbol of passion, perseverance, and the never-ending chase for glory."""


# loader = PyPDFLoader(file_path='Text_splitter\Character_splitter.py')

# docs = loader.load()

text_splitter = CharacterTextSplitter(chunk_size = 50,
                                      chunk_overlap = 5,
                                      separator='')

result = text_splitter.split_text(text=text)
print(result[0])