#!/usr/bin/env perl 

use strict; 
use warnings; 

if ($#ARGV < 1) { 
  print "Usage: ./make_proper_wig.pl <bam> <strand>\n";
  print "Requires samtools v1+; strand can be + or -\n"; 
  exit 1
}

my $bam = shift @ARGV;
my $strand = shift @ARGV; 

my $strandstr;
if ($strand eq "+") {
  $strandstr = "forward"; 
} else { 
  $strandstr = "reverse"
} 

if ($strand ne "+" && $strand ne "-") { 
  die "ERROR: Strand can be + or - only!\n"; 
} 

if ($strand eq "+") { 
  system "samtools view -b -F 16 $bam | samtools depth -d 0 - > ${bam}_${strandstr}.wig"; 
} else {
  system "samtools view -b -f 16 $bam | samtools depth -d 0 - > ${bam}_${strandstr}.wig";
}

open COV,"<","${bam}_${strandstr}.wig" or die "$!"; 

my $tag = $bam; 
$tag =~ s/.bam//g; 

printf "track type=wiggle_0 name=%s\n",$tag;
my $lastC = ""; 

while (<COV>) { 
  my ($c, $start, $depth) = split;
  print "variableStep chrom=$c span=1\n" if ($c ne $lastC);
  $lastC = $c; 
  if ($strand eq "+") {
    print "$start\t$depth\n"; 
  } else { 
    print "$start\t-$depth\n";
  } 
} 

system "rm ${bam}_${strandstr}.wig";
close COV;
exit 0;
