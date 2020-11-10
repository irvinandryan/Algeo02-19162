from stemmy import output #ini nanti outputnya diganti buat beberapa file
TabTerm = []
for i in output.split():
    if not i in TabTerm:
        TabTerm.append(i)
print(TabTerm)
