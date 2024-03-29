from sqlalchemy import Column, Integer, String,Text, create_engine, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""Variables
"""
base = declarative_base()



"""Tables"""
class memory(base):
    __tablename__ = 'memory'
    id = Column('id',Integer, primary_key=True, autoincrement=True)
    keywords = Column('keywords',Text)
    summary = Column('summary',Text)
    conversation = Column('conversation',Text)

    def __init__(self, id, keywords, summary, conversation):
        self.id = id
        self.keywords = keywords
        self.summary = summary
        self.conversation = conversation



    def __repr__(self):
        return "<memory(id='%s', keywords='%s', summary='%s', conversation='%s')>" % (
            self.id, self.keywords, self.summary, self.conversation)

class knowledge(base):
    __tablename__ = 'knowledge'
    id = Column('id',Integer, primary_key=True, autoincrement=True)
    keywords = Column('keywords',Text)
    summary = Column('summary',Text)

    def __init__(self, id, keywords, summary):
        self.id = id
        self.keywords = keywords
        self.summary = summary

    def __repr__(self):
        return "<knowledge(id='%s', keywords='%s', summary='%s')>" % (
            self.id, self.keywords, self.summary)

"""Functions"""            
def sanitize(string):
    '''This function removes unwanted characters from the string that can break memory interactions.'''
    string = results_to_string(string)
    unwanted_characters = ['\n',"'s",'"',"'",'?','!','.',':',';','(',')','[',']','{','}','<','>','/','\\','|','@','#','$','%','^','&','*','_','-','+','=','~','`']
    for character in unwanted_characters:
        string = string.replace(character,'')
    return string

def search(phrase):
    '''This function searches the memory for related summaries of previous conversations that matches the phrase.'''
    phrase = sanitize(phrase)
    search_queries = phrase.split(' ')
    filter = [memory.keywords.like("%"+sq+"%") for sq in search_queries]
    results = sessionmind.query(memory).filter(or_(*filter)).order_by(memory.id.desc()).limit(6)
    return [result.summary for result in results]

def searchk(phrase):
    '''This function searches the knowledge bank for related matches the phrase.'''
    phrase = sanitize(phrase)
    search_queries = phrase.split(' ')
    filter = [knowledge.keywords.like("%"+sq+"%") for sq in search_queries]
    results = sessionmind.query(knowledge).filter(or_(*filter)).order_by(knowledge.id.desc()).limit(11)
    return [result.summary for result in results]
   

def results_to_string(results):
    return '\n'.join([str(result) for result in results])


def store_memory(keywords, summary, conversation):
    '''This function stores the keywords, summary, abd conversation in the memory database.'''
    keywords = keywords
    summary = summary
    conversation = conversation
    insert = memory(None,keywords,summary,conversation)
    sessionmind.add(insert)
    sessionmind.commit()
    return True

def last_conversation():
    results = sessionmind.query(memory).order_by(memory.id.desc()).first()
    return results.summary

def last_keywords():
    results = sessionmind.query(memory).order_by(memory.id.desc()).first()
    return results.keywords

#write a function that returns all the conversations in the database
def all_conversations():
    results = sessionmind.query(memory).order_by(memory.id.desc()).all()
    return [result.conversation for result in results]

def all_summaries():
    results = sessionmind.query(memory).order_by(memory.id.desc()).all()
    return [result.summary for result in results]

def all_knowledge():
    results = sessionmind.query(knowledge).order_by(knowledge.id.desc()).all()
    return [result.summary for result in results]




#lol



"""Load Memory database."""

engine = create_engine('sqlite:///mind.db', echo=False)
base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)
sessionmind = session()






