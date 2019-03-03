import os

# Create a new file
def writeFile(path, data):
    f = open(path,'w')
    f.write(data)
    f.close()

# Create directories for the crawling project
def createDir(directory):
    if not os.path.exists(directory):
        print('Creating project directory' + directory)
        os.makedirs(directory)

# Create crawling files 'QUEUE & CRAWLED'
def createDataFiles(projectName,base_url):
    queue = projectName + '/queue.txt'
    crawled = projectName + '/crawled.txt'
    if not os.path.isfile(queue):
        writeFile(queue, base_url)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')

# Add data to an existing file
def addToFile(path, data):
    with open (path, 'a') as f:
        f.write(data + "\n")

# Delete file content
def delFileContent(path):
    with open(path, 'w'):
        pass

# Convert file to a set
def fileToSet(fileName):
    res = set()
    with open (fileName,'rt') as f:
        for line in f:
            res.add(line.replace('\n', ''))
    return res

# Convert a set to a file
def setToFile(links,fileName):
    delFileContent(fileName)
    for link in sorted(links):
        addToFile(fileName,link)
