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
def createDataFiles(projectName,baseUrl):
    queue = projectName + '/queue.txt'
    crawled = projectName + '/crawled.txt'
    if not os.path.isfile(queue):
        writeFile(queue, baseUrl)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')
