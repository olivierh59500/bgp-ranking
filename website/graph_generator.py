from string import Template

class GraphGenerator():
    lines = []
    keys = []
    labels = None
    title = None
    template = Template("""
window.onload = function ()
    {
        graph = new RGraph.Line('$name' $lines);
        graph.Set('chart.tooltips', $tooltips);
        graph.Set('chart.gutter', 70);
        graph.Set('chart.tickmarks', 'circle');
        graph.Set('chart.shadow', 'true');
        graph.Set('chart.background.grid.autofit', true);
        graph.Set('chart.labels', $labels);
        graph.Set('chart.text.angle', 45);
        graph.Set('chart.linewidth', 1);
        graph.Set('chart.title', '$title');
        graph.Set('chart.title.xaxis', 'Date');
        graph.Set('chart.title.yaxis', 'Rank');
        graph.Set('chart.ymin', 0);
        graph.Set('chart.ymax', $max);
        graph.Set('chart.scale.decimals', 5);
        graph.Set('chart.key', $keys);
        graph.Set('chart.contextmenu', [['Zoom entire graph', RGraph.Zoom]]);
        graph.Draw();
    }
""")
    
    def __init__(self, name):
        self.name = name

    def add_line(self, line, key):
        self.lines.append(line)
        self.keys.append(key)
    
    # xaxis
    def set_labels(self, labels):
        self.labels = labels
    
    def set_title(self, title):
        self.title = title
    
    def make_js(self):
        form_lines = ''
        tooltips = []
        real_max = 0
        for line in self.lines:
            form_lines += ', ' + str(line)
            tooltips += line
            real_max = max(real_max, max(line))
        form_keys = str(self.keys)
        self.js = self.template.substitute( name = self.name, lines = form_lines, tooltips = str(tooltips), labels = str(self.labels), title = self.title, max = real_max, keys = str(self.keys) )

if __name__ == "__main__":
    g = GraphGenerator('plop')
    g.add_line([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 'test')
    g.add_line([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 'test 2')
    g.set_labels(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    g.set_title('Test perso')
    g.make_js()
    print g.js
