"""A simple module implementing a utility to format XML. It doesn't
   actually do any of the work, but simply uses the xml.dom.minidom
   library module to do the actual work.
"""
import xml.dom.minidom
import argparse
import shutil

def main():
  """Format each of the given xml files"""
  description = "Format xml files"
  parser = argparse.ArgumentParser(description=description)
  # Might want to make the type of this 'FileType('r')'
  parser.add_argument('filenames', metavar='F', nargs='+',
                      help="an xml file to format")

  arguments = parser.parse_args()

  for filename in arguments.filenames:
    # As usual for formatting utilities we create a copy
    # of the existing file first.
    shutil.copy2(filename, filename + ".orig") 
    dom = xml.dom.minidom.parse(filename)
    document = dom.toprettyxml(indent="  ", encoding="UTF-8")
    xml_file = open(filename, "w")
    xml_file.write(document)
    xml_file.close()


if __name__ == "__main__":
  main()
