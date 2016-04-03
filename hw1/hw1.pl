#!/usr/bin/perl
#rsait001 Ryota Saito 
# writing "cat" cmd in perl

#@ARGV stores cmdline args into an array
if(scalar @ARGV == 0){
	exit 0
}

foreach $i (@ARGV){
	# $i now contains all text file names
	#open file for reading (< means stdin, $fh is file descriptor)
	open( $fh, '<', $i);
	#$line i in the scope of the file
	while ( $line = <$fh> ) {
		print "$line";
	}

    close $fh;
} 
