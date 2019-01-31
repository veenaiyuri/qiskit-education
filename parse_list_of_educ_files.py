# parses the list_of_educ_files.md list and spits out, for each educational notebook, the following:
# title of the notebook
# the original location where it was cited (maybe another notebook or another URL somewhere)
# the url pointing to the notebook
contents = open('list_of_educ_files.md', 'r').readlines()
for line in contents:
    linesplit = line.split(')(')
    name_source = ''.join(linesplit[0:-1])[1:]
    name,source = name_source.split('--')
    url = ''.join(linesplit[-1:])[0:-2]
    print(name)
    print(source)
    print(url)
