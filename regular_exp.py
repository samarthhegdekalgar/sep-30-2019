import re

data = '''
555-444-1234
123-456-8790
098-123-0987
'''

regex_string = r'^(\d{3})(\-\d{3})(\-\d{4})$'
date_time_regex = r'^(\d{1,2})\s(\d{1,2})\s(\d{4})\s(\d{1,2}\:\d{1,2}\:\d{1,2})'
email_regex = r'^((\w)*\@(\w(\.)?)+\.(\w){2,3})$'

regex = re.compile(regex_string, re.MULTILINE)

# search_obj = regex.search(data)
find_obj = re.finditer(regex, data)
for value in find_obj:
    print(value.group())
