import os


def getAllDocumentPaths(source_directory):
    allpaths = list()

    for (dirpath, dirnames, filenames) in os.walk(source_directory):
        dirnames.sort()
        filenames.sort()
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            allpaths.append(path)
    allpaths.sort(reverse=True)

    return allpaths
