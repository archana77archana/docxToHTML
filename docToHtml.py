import pypandoc
import sys
from tidylib import tidy_document

output = pypandoc.convert(sys.argv[1], 'html', extra_args=['--extract-media=./'])
output, errors = tidy_document(output, options={
        'numeric-entities': 1,
        'wrap': 80,
})

print(errors)
output = output.replace(u"\u2018", '&lsquo;').replace(u"\u2019", '&rsquo;')
output = output.replace(u"\u201c", "&ldquo;").replace(u"\u201d", "&rdquo;")
with open(sys.argv[2],'w') as f:
	f.write(output)
print('done')