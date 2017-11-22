
import os
from jinja2 import Environment, FileSystemLoader

root = os.path.dirname(os.path.abspath(__file__))  
 
class Report(object):
    def __init__(self, path, name):
        self.name = name
        self.path = path
        self.html = os.path.join(path,'{}.html'.format(name.replace(' ','')))

        self.sections = []

   
    def add(self, **content):
        style={}
        if 'table' in content:
            content['table'] = self.table(content.get('table'))

        if 'size' in content:
            style['size'] = content.pop('size')

        if 'color' in content:
            style['color'] = contents.pop('color')

        if 'font' in content:
            style['font'] = content.pop('font')

        if 'style':
            content['style'] = style

            
        self.sections.append(content)



    def create(self):
        environment = Environment(loader = FileSystemLoader(os.path.join(root,'templates')))
        template = environment.get_template('section.html')
        output = template.render(sections = self.sections, title = self.name)

        with open(self.html,'w') as f :
            f.write(output)



    def table(self,data):
        environment = Environment(loader = FileSystemLoader(os.path.join(root,'templates')))
        template = environment.get_template('tables.html')
        output = template.render(columns = data.columns, 
                                rows    = data.values
                               )

        return output
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            