#!/usr/bin/perl
# use this script to remove all externala and aliases
use strict;
use warnings;
use Getopt::Long;
#use Storable qw(nstore store_fd nstore_fd freeze thaw dclone store retrieve);
use Fcntl qw(:DEFAULT :flock);
#use Digest::MD5 qw(md5 md5_hex md5_base64);
use POSIX 'strftime';
use Text::CSV;
my ($input_file, $output_file);

GetOptions(
	'input=s'=>\$input_file,
	'output=s'=>\$output_file )  || die "ERROR: Unable to get command line arguments";

die "Input File not defined" unless $input_file;
die "Output File not defined" unless $output_file;
die "Input file not readable" unless -R $input_file;
#die "Input file $input_file not writeable" unless can_write($input_file);




#Main code
main();




sub main
{
	#Read into memory
	my @lines;

	#TSV
	#open(INPUT, '<', $input_file) or die "Can't open $input_file";
	#mess with this if needed for windows endings
	#local $/ = "\r\n";

	#CSV
	#
	my $csv = Text::CSV->new({ binary => 1 });
	#open my $data, "<:encoding(UTF-8)", $input_file or die "$input_file $!";
	open my $data, "<", $input_file or die "$input_file $!";



	#my @headers;

	#while (<INPUT>)
	#{
		#chomp $_;
		#and this
		#my @fields = split(/\t/, $_);
		#push @lines, \@fields;

		#}

		#close(INPUT);
	while (my $row = $csv->getline($data))
	{
		my @fields = @$row;
		#SKIP if header line
		next if $fields[0] eq  "From";
		#Toms bit
			my @a = split(/,/, $fields[1]);
			my @from_array=();
			foreach my $b(@a)
			{
        		if ($b =~ /syngenta.com/)   {       push @from_array,$b;          }
			}
			$fields[1] = join(',', @from_array);
			push @lines, \@fields;

	}

	close($data);


	#output pass
	open(OUTPUT, '>', $output_file) or die "Can't open output file to write";
	#print OUTPUT join("\t", @headers), "\r\n";
	foreach my $line (@lines)
	{
		print OUTPUT join("\t", @$line), "\r\n";
	}
	close(OUTPUT);




}


sub can_write
{
	my $file_test = shift;
	sysopen(FH,  $file_test, O_APPEND) or return 0;
	close FH;
	return 1;

}

