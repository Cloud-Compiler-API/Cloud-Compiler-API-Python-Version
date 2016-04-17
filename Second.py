from First import Scrape

class Learn(object):
    """this class provides a way to learn"""
    def __init__(self):
        print "initialized"


    def display(self,g):
        print g
        pass

if __name__ == '__main__':
    print "hi"
    ob = Learn()
    #execute import filename
    #filename.classname(.function)
    print ob.__doc__
    print Scrape.url
    ob.display("value")
    ob.

