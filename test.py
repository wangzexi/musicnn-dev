from musicnn.tagger import top_tags

filenames = [
  './music/一路向北.wav',
  './music/mojito.wav',
]

filename = filenames[0]

tags = top_tags(filename, model='MTT_musicnn', topN=5, print_tags=False)
tags2 = top_tags(filename, model='MSD_musicnn', topN=5, print_tags=False)

print('**完成!', tags, tags2)
