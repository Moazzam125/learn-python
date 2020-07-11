from collections import OrderedDict

import random


favorite_languages = OrderedDict()
favorite_languages['moazzam'] = 'python'
favorite_languages['muzammyl'] = 'c++'

for name, language in favorite_languages.items():
    print(name.title() + "'s favoriate language is " + language.title() + ".")