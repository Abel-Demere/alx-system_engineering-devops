#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
    puts "Usage: #{$PROGRAM_NAME} <string>"
    exit 1
  end
  
  # Extract the argument from command line
  input_string = ARGV[0]
  
  # Define the regular expression pattern with repetition token '#3'
  pattern = /hbt*n/
  
  # Use the match method to find all occurrences of the pattern in the input string
  matches = input_string.scan(pattern)
  
  # Output the matched string(s)
  puts matches.join
  