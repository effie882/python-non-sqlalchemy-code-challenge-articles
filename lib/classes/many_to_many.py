class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        

        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        """Return the immutable title of the article"""
        return self._title
        
    @title.setter
    def title(self, value):
        """Prevent modification of title"""
        if not hasattr(self, "_title"):
            if isinstance(value, str) and 5 <= len(value) <= 50:
                self._title = value
            else:
                raise Exception("Titile must be a string between 5 and 50 characters")
            pass

        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self._name = name

    @property
    def name(self):
        """Return the immutable name of the author"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Prevent modification of a name (ignore reassignment)"""
        pass

    def articles(self):
        """Return a list of all articles written by this author"""
        return [article for article in Article.all if article.author == self]
        pass

    def magazines(self):
        """Return unique magazines this author has written for"""
        return list(set([article.magazine for article in self.articles()]))
        pass

    def add_article(self, magazine, title):
        """Creates and returns a new Article for this author"""
        return Article(self, magazine, title)
        pass

    def topic_areas(self):
        """Return a list of unique topic areas (magazine categories) for this author"""
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))
        pass

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise Exception("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        """Allow name changes, with validation (ignore invalid values)"""
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        """Allow category changes, must be a non-empty string between 2 and 50 chars"""
        if isinstance(value, str) and (2 <= len(value.strip()) <= 50):
            self._category = value
    
    def articles(self):
        """Return all articles that belong to this magazine"""
        return [article for article in Article.all if article.magazine == self]
        pass

    def contributors(self):
        """Return unique authors who have written articles for this magazine"""
        return list(set(article.author for article in self.articles()))
        pass

    def article_titles(self):
        """Return a list of titles of all articles written for this magazine"""
        titles = [article.title for article in self.articles()]
        return titles if titles else None
        pass

    def contributing_authors(self):
        """Return authors who have written more than 2 articles for this magazine"""
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None
        pass