#!/perl/bin/perl

use CGI qw(:standard);				# Include standard HTML and CGI functions
use CGI::Carp qw(fatalsToBrowser);      	# Send error messages to browser

use DBI;
&printheader;
if (param()) { 
	#print h3("Hello ".param("un"));
	#my $un=param("un");
		}
&printcontent;	
&printtail;	




sub printheader {

  print header(), 
  	start_html(-title => 'Landing Page', 
 -style => { 
 -src=>['http://www.blueprintcss.org/blueprint/screen.css','http://www.blueprintcss.org/blueprint/plugins/buttons/screen.css','http://www.blueprintcss.org/blueprint/print.css']
 }), 
  
	hr;
}




sub printtail {

  print address("jposni\@nisum.com"),
  	end_html(); 
}




sub printcontent {

					# connect to the database
			my $dbh = DBI->connect("DBI:mysql:database=padmini1132;host=localhost;port=3306", "root", "padmini") 
			or die $DBI::errstr;

			my $sth = $dbh->prepare("SELECT * FROM requests");

			$sth->execute();
			#print param("un");
			print "<p>There are ".$sth->rows." rows to display";
			print "<ul>";
			while (my @row = $sth->fetchrow_array ) {
			print "<li>@row\n";
				}
			print "</ul>";
			$dbh->disconnect;


}
