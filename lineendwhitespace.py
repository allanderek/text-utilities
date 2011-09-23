"""A simple module implementing a utility to remove white space at the
   end of each line.
"""
import argparse
import shutil

def main():
  """The main method"""
  description = "Remove white space from the end of lines"
  parser = argparse.ArgumentParser(description=description)
  # Might want to make the type of this 'FileType('r')'
  parser.add_argument('filenames', metavar='F', nargs='+',
                      help="a plain text file to format")
  parser.add_argument('--remove-blank-lines', action='store_true',
                      help="Remove completely blank lines")
   
  arguments = parser.parse_args()

  for filename in arguments.filenames:
    # So we first copy the original file over to a similarly named
    # file with the '.orig' suffix.
    orig_copy_filename = filename + ".orig" 
    shutil.copy2(filename, orig_copy_filename)

    # Now we will read from the original-copy and write a new file
    # to the original filename copy.
    orig_file = open(orig_copy_filename, "r")
    new_file = open(filename, "w")

    for line in orig_file:
      # Removing white space at the end of the line is simple
      # in python with the 'rstrip' method.
      output_line = line.rstrip()
      # So if the output line is empty and we've been asked to
      # remove blank lines, then don't output anything, but otherwise
      # output the stripped line.
      if output_line or not arguments.remove_blank_lines:
        new_file.write(output_line)
        # We must output a newline, because the newline would have
        # been removed by rstrip.
        new_file.write("\n")

    # Don't forget to close both files.
    new_file.close()
    orig_file.close()
   
if __name__ == "__main__":
  main()
