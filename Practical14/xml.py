import xml.dom.minidom
import xml.sax
import time
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

# File name
xml_file = 'go_obo.xml'

# DOM parsing
def parse_dom(xml_file):
    start_time = datetime.now()
    doc = xml.dom.minidom.parse(xml_file)
    terms = doc.getElementsByTagName('term')
    counts = defaultdict(int)
    
    for term in terms:
        ontology = term.getElementsByTagName('namespace')[0].firstChild.data
        counts[ontology] += 1

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    return counts, duration

# SAX parsing
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.counts = defaultdict(int)
        self.current_ontology = ""
        self.is_namespace = False
    
    def startElement(self, tag, attributes):
        if tag == "namespace":
            self.is_namespace = True

    def characters(self, content):
        if self.is_namespace:
            self.current_ontology = content
    
    def endElement(self, tag):
        if tag == "namespace":
            self.counts[self.current_ontology] += 1
            self.is_namespace = False

def parse_sax(xml_file):
    start_time = datetime.now()
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    return handler.counts, duration

# Running both parsers
dom_counts, dom_duration = parse_dom(xml_file)
sax_counts, sax_duration = parse_sax(xml_file)

# Ensure both methods return the same results
assert dom_counts == sax_counts, "DOM and SAX parsing results differ!"

# Plotting the results
ontologies = list(dom_counts.keys())
counts = list(dom_counts.values())

plt.figure(figsize=(10, 5))
plt.bar(ontologies, counts, color=['blue', 'green', 'red'])
plt.xlabel('Ontology')
plt.ylabel('Number of Terms')
plt.title('Number of GO Terms in Each Ontology')
plt.show()

# Print durations
print(f"DOM parsing duration: {dom_duration} seconds")
print(f"SAX parsing duration: {sax_duration} seconds")
# Comment on which ran faster
# SAX parsing ran faster if sax_duration < dom_duration else DOM parsing ran faster