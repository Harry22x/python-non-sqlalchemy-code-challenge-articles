class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self._title_set = True
        Article.all.append(self)
        

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if (not hasattr(self, '_title_set') and isinstance(value, str) and 4<len(value)<51):
            self._title = value
        else:
             raise Exception("Title must be a string of length greater than 4 and less than 51 and cannot be changed once instantiated")
      

    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(magazine,Magazine):
            self._magazine = magazine
        else:
            raise Exception("Magazine must be an instance of the Magazine class")

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        if isinstance(author,Author):
            self._author = author
        else:
            raise Exception("Author must be an instance of the Author class")


class Author:

    def __init__(self, name):
        self._name = None
        self.name = name
        self._name_set = True
 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if (not (hasattr(self, '_name_set')) and isinstance(value,str) and len(value)>0 ):
            self._name = value
        else:
            raise Exception("Name must be a string of length greater than 0 and cannot be changed once instantiated")
        
    def articles(self):
        pass
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        pass
        return list({article.magazine for article in Article.all if article.author == self })        

    def add_article(self, magazine, title):
        pass
        return Article(self,magazine,title)

    def topic_areas(self):
        pass
        topic_list = list({article.magazine.category for article in Article.all if article.author == self})
        if len(topic_list) == 0:
            return None
        else:
            return topic_list
        

class Magazine:
    
    def __init__(self, name, category):
        self.name = name
        self.category = category


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if(isinstance(value,str) and 1<len(value)<17):
            self._name = value
        else:
            raise Exception("Name must be a string of length greater than 0 and less than 17 and cannot be changed once instantiated")
        

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if(len(value)>0 and isinstance(value,str)):
            self._category = value
        else:
            raise Exception("Category must be a string of length greater than 0")


    def articles(self):
        pass
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        pass
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        pass
        title_list = [article.title for article in Article.all if article.magazine == self]
        if len(title_list) == 0:
            return None
        else:
            return title_list
    def contributing_authors(self):
        pass
        author_list = [article.author for article in Article.all if article.magazine == self]
        author_list_filtered = []
        for author in author_list:
            if(author_list.count(author)>2):
                author_list_filtered.append(author)
        if len(author_list_filtered) == 0:
            return None
        else:
            return list(set(author_list_filtered))

    @classmethod
    def top_publisher(cls):
       
        if not Article.all:
            return None
        
       
        magazine_article_count = {}
        
       
        for article in Article.all:
            if article.magazine in magazine_article_count:
                magazine_article_count[article.magazine] += 1
            else:
                magazine_article_count[article.magazine] = 1
        
        if not magazine_article_count:
            return None
        
        top_magazine = max(magazine_article_count, key=magazine_article_count.get)
        
        return top_magazine  
   