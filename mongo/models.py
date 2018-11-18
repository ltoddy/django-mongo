from django.db import models


# for future
class Mongo(models.Model):
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    host = models.CharField(max_length=50, blank=True, default='localhost')
    port = models.IntegerField(blank=True, default=27017)
    timestamp = models.DateTimeField(auto_now_add=True)

    __URI_WITH_USERNAME_FMT = 'mongodb://{username}:{password}@{host}:{port}/'
    __URI_WITHOUT_USERNAME_FMT = 'mongodb://{host}:{port}/'

    def uri(self):
        if self.username and self.password:
            uri_fmt = self.__URI_WITH_USERNAME_FMT
        else:
            uri_fmt = self.__URI_WITHOUT_USERNAME_FMT
        return uri_fmt.format(username=self.username, password=self.password, host=self.host, port=self.port)

    def __repr__(self):
        return f'mongo config => ({self.uri()})'
