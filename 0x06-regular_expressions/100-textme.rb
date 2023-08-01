#!/usr/bin/env ruby
# Check if an argument is provided
if ARGV.length != 1
    puts "Usage: #{$PROGRAM_NAME} <log_file>"
    exit 1
  end
  
  # Extract the argument from command line
  log_file = ARGV[0]
  
  # Read the log file content
  log_content = File.read(log_file)
  
  # Define the regular expression pattern to extract the required information
  pattern = /\[from:([^]]*)\] \[to:([^]]*)\] \[flags:([^]]*)\]/
  
  # Use the scan method to find all occurrences of the pattern in the log content
  matches = log_content.scan(pattern)
  
  # Output the result
  matches.each do |match|
    sender = match[0]
    receiver = match[1]
    flags = match[2]
    puts "#{sender},#{receiver},#{flags}"
  end
  