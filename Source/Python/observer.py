from random import random

class Subscriber:
    """Базовый подписчик для сервера"""
    def __init__(self, server):
        self.server = server
        self.server.addsubscriber(self)
    def newnews(self, newssource, count):
        pass
    def getnews(self, newssource):
        print(self.server.getnews(newssource))

class VKSubscriber(Subscriber):
    """подписчик на новости VK"""
    def newnews(self, newssource, count):
        if(newssource == 'vk'):
            self.getnews(newssource)
class TwitterSubscriber(Subscriber):
    """подписчик на новости Twitter"""
    def newnews(self, newssource, count):
        if(newssource == 'twitter'):
            self.getnews(newssource)

class Observer:
    """Сервер, может подписывать и отписывать на себя другие классы, а также уведомлять их о новых событиях внутри себя"""
    subscribers = list()
    newslist = dict({'vk': 0, 'facebook': 0, 'twitter': 0, 'youtube': 0})
    
    def event(self):
        for key in self.newslist:
            self.newslist[key] = round(4* random())

        print(self.newslist)
        
        self.notifysubscribers()

    def addsubscriber(self, subscriber : Subscriber):
        self.subscribers.append(subscriber)

    def removesubscriber(self, subscriber : Subscriber):
        self.subscribers.remove(subscriber)

    def notifysubscribers(self):
        for subscriber in self.subscribers:
            for key in self.newslist:
                subscriber.newnews(key, self.newslist[key])

    def getnews(self, sourcenews):
        if sourcenews in self.newslist:
            return self.newslist[sourcenews]


server = Observer()

twitter = TwitterSubscriber(server)
vk = VKSubscriber(server)

server.event()
