from django.contrib.contenttypes.models import ContentType

# This info object used by cartoview app manager to show app details in the app list
info = {
    "title": "Cartoview Basic App",
    "description": ''' Cartoview Basic App is an app template to start multi instance cartoview app''',
    "author": 'Cartologic',
    "tags": ['App Template'],
    "licence": 'BSD',
    "author_website": "http://www.cartologic.com",
    "single_instance": False
}


def install():
    # add any extra app installation logic
    pass


def uninstall():
    ContentType.objects.filter(app_label="cartoview_basic_app").delete()
    # add any extra app uninstall logic
