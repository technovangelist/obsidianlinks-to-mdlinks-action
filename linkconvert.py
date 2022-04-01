from utils import getAllDocumentPaths
docsdirectory = os.environ["INPUT_SRCROOTDIRECTORY"]
allpaths = getAllDocumentPaths(docsdirectory)

print(allpaths)
