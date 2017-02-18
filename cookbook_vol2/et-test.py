import os
import subprocess
import xml.etree.ElementTree as ET


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def formatting(message):
    print("\n" * 2)
    print("=" * 80)
    print("\t" * 2 + '::::' + " " +
          color.BOLD + message + color.END +
          " " + '::::' + "\t" * 2)


def find_it():
    root.findall("dict")


key = 'Lightshow_version'
detail = -2
command = 'system_profiler -xml -detailLevel %d' % detail
command_list = [i for i in command.split(' ')]
command_string = subprocess.check_output(command_list)
formatting('FILE from popen() on command')
output_as_file = os.popen(command)
print(output_as_file)
print(type(output_as_file))
formatting('TREE from parse() from command')
tree_from_parse = ET.parse(output_as_file)
print(tree_from_parse)
print(type(tree_from_parse))
formatting("ELEMENT/ROOT from getroot() on TREE")
root = tree_from_parse.getroot()
print(root)
print(type(root))
# Top-level elements
find_it()
print(root.findall("."))
formatting("TREE from parse() from file path")
tree_from_parse = ET.parse(os.path.abspath('xml_test-data/sp.xml'))
print(tree_from_parse)
print(type(tree_from_parse))
formatting("ELEMENT/ROOT with fromstring() from subprocess")
root = ET.fromstring(command_string)
print(root)
print(type(root))
# Top-level elements
find_it()
print(root.findall("."))
print("\n")
found = root.findall('.//dict[key=%r]' % key)
print(found)
print(root.getchildren())

for child in found:
    grandchildren = child.getchildren()
    print("Child tag: %r" % child.tag)
    print("Child text: %r" % child.text)
    for grandchild in grandchildren:
        print("Grandchild tag: %r" % grandchild.tag)
        print("Grandchild text: %r" % grandchild.text)


# All 'neighbor' grand-children of 'country' children of the top-level
# elements
# root.findall("./country/neighbor")
#
# # Nodes with name='Singapore' that have a 'year' child
# root.findall(".//year/..[@name='Singapore']")
#
# # 'year' nodes that are children of nodes with name='Singapore'
# root.findall(".//*[@name='Singapore']/year")
#
# # All 'neighbor' nodes that are the second child of their parent
# root.findall(".//neighbor[2]")
