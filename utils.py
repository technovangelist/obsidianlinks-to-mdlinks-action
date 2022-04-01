import os
import re


def getAllDocumentPaths(source_directory):
    allpaths = list()

    for (dirpath, dirnames, filenames) in os.walk(source_directory):
        dirnames.sort()
        filenames.sort()
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            # path.replace(source_directory, "")
            allpaths.append(path)
    allpaths.sort(reverse=True)

    return allpaths


def getFileFullText(path):
    with open(path) as f:
        fulltext = f.read()

    return fulltext


def replaceLinks(text, allpaths):
    foundmatches = re.findall(
        r'(?P<fullwikilink>\[\[(?P<linkpage>.*?)\]\]?)', text)
    outputtext = text
    for item in foundmatches:
        fullwikilink = item[0]
        linkpage = item[1] + ".md"
        linkpage = re.sub(r'^.*\|', '', linkpage)
        pageurl = ''
        for path in allpaths:
            filename = path.split("/")[-1]
            print('linkpage:', linkpage)
            print("filename:", filename)

            if linkpage == filename:
                pageurl = path
                break

        print(pageurl)
        newoutputtext = outputtext.replace(
            fullwikilink, "[" + pageurl + "]("+pageurl+")")
    return newoutputtext


def replaceurl(path, allpaths):
    fulltext = getFileFullText(path)
    replacedtext = replaceLinks(fulltext, allpaths)
    print(replacedtext)
    with open(path, "w") as f:
        f.write(replacedtext)
