#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
    puts "Usage: #{$PROGRAM_NAME} <phone_number>"
    exit 1
  end
  
  # Extract the argument from command line
  phone_number = ARGV[0]
  
  # Define the regular expression pattern
  pattern = /^\d{10}$/
  
  # Use the match method to check if the input string matches the pattern
  match = phone_number.match(pattern)
  
  # Output the result
  puts match ? match[0] : ""
  