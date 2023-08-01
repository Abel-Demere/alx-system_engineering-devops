#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
    puts "Usage: #{$PROGRAM_NAME} <string>"
    exit 1
  end
  
  # Extract the argument from command line
  input_string = ARGV[0]
  
  # Define the regular expression pattern
  pattern = /^h.n$/
  
  # Use the match method to check if the input string matches the pattern
  match = input_string.match(pattern)
  
  # Output the result
  puts match ? match[0] : ""
  