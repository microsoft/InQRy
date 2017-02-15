#!/usr/bin/env python
from xml import dom
import datetime
import time
import os
import xml.etree.ElementTree as ET


def group(seq, n):
    """group([0, 3, 4, 10, 2, 3, 1], 3) => [(0, 3, 4), (10, 2, 3)]
       Group a sequence into n-subseqs, discarding incomplete subseqs.
    """
    return [seq[i:i+n] for i in xrange(0, len(seq)-n+1, n)]
#
#
# def remove_whitespace_nodes(node):
#     """Removes all of the whitespace-only text descendants of a DOM node."""
#     remove_list = []
#     for child in node.getchildren():
#         if child.nodeType == dom.Node.TEXT_NODE and not child.data.strip():
#             remove_list.append(child)
#         elif child.getchildren():
#             remove_whitespace_nodes(child)
#     for child in remove_list:
#         node.removeChild(child)
#         child.unlink()


class OSXSystemProfiler:
    "Provide information from the Mac OS X System Profiler"
    def __init__(self, detail=-2):
        """detail can range from -2 to +1.  Larger numbers return more info.
           Beware of +1, can take many minutes to get all info!"""
        self.system_profiler_output = os.popen(
            'system_profiler -xml -detailLevel %d' % detail)
        self.root = ET.parse(self.system_profiler_output).getroot()
        # remove_whitespace_nodes(self.root)

    def _content(self, node):
        "Get the text node content of an element, or an empty string"
        if node.text:
            return node.text
        else:
            return ''

    def _convert_value_node(self, node):
        # """Convert a 'value' node (i.e. anything but 'key') into a Python data
        #    structure"""
        # if node.tag == 'string':
        #     return self._content(node)
        # elif node.tag == 'integer':
        #     return int(self._content(node))
        # elif node.tag == 'real':
        #     return float(self._content(node))
        # elif node.tag == 'date':  # <date>2004-07-05T13:29:29Z</date>
        #     return datetime.datetime(
        #         *time.strptime(self._content(node), '%Y-%m-%dT%H:%M:%SZ')[:5])
        # elif node.tag == 'array':
        #     return [self._convert_value_node(n) for n in node.getchildren()]
        if node.tag == 'dict':
            return dict([(self._content(n), self._convert_value_node(m)) for n, m in group(node.getchildren(), 2)])
    #     else:
    #         raise ValueError('Unknown tag %r' % node.tag)

    def __getitem__(self, key):
        # pyxml's xpath does not support /element1[...]/element2...
        nodes = self.root.findall('.//dict[key=%r]' % key)
        # results = []
        for node in nodes:
            children = node.getchildren()

            for child in children:
                print(child.getchildren())
        #     v = self._convert_value_node(node)[key]
        #     if isinstance(v, dict) and '_order' in v:
        #         # this is just information for display
        #         pass
        #     else:
        #         results.append(v)
        # return results

    # def all(self):
    #     """Return the complete information from the system profiler
    #        as a Python data structure"""
    #     return self._convert_value_node(
    #         self.root.documentElement.firstChild)


    # def main():
    #     from optparse import OptionParser
    #     from pprint import pprint
    #     info = OSXSystemProfiler()
    #     parser = OptionParser()
    #     parser.add_option("-f", "--field", action="store", dest="field",
    #                       help="display the value of the specified field")
    #     options, args = parser.parse_args()
    #     if args:
    #         parser.error("no arguments are allowed")
    #     if options.field is not None:
    #         pprint(info[options.field])
    #     else:
    #         # print some keys known to exist in only one important dict
    #         for k in ['cpu_type', 'current_processor_speed', 'l2_cache_size',
    #                   'physical_memory', 'user_name', 'os_version', 'ip_address']:
    #             print '%s: %s' % (k, info[k][0])


info = OSXSystemProfiler()
info['cpu_type']
info['current_processor_speed']
info['l2_cache_size']
info['physical_memory']
info['user_name']

if __name__ == '__main__':
    pass
