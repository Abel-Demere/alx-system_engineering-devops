#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
    puts "Usage: #{$PROGRAM_NAME} <string>"
    exit 1
  end
  
  # Extract the argument from command line
  input_string = ARGV[0]
  
  # Define the regular expression pattern
  pattern = /[A-Z]/
  
  # Use the scan method to find all occurrences of capital letters in the input string
  matches = input_string.scan(pattern)
  
  # Output the result
  puts matches.join
  