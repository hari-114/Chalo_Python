def sort_colors(str):
     up=str.lower()
     split=up.split('-')
     split.sort()
     print('-'.join(split))

str='pink-Blue-Green'
sort_colors(str)