#!/usr/bin/env ruby
##regex only maatching cap letters
if ARGV.length == 1
    puts ARGV[0].scan(/[A-Z]*/).join("")
    exit
end
