#!/perl/bin/perl

use CGI qw(:standard);				# Include standard HTML and CGI functions
use CGI::Carp qw(fatalsToBrowser);      	# Send error messages to browser

my $q=new CGI;
use DBI;
&printheader;
if (param()) { 
	print h3("Hello ".param("un"));
	my $un=param("un");
		}
&printcontent;
print "<center>";

#print "                          ";
print "<button class='button positive' onclick='javascript:history.back()'>
             <img alt='ok' src='http://www.blueprintcss.org/blueprint/plugins/buttons/icons/key.png' /> 
             Go back
            </button>";
#print "<a href=javascript:history.back()>Go back</a>";
print "<button class='button negative' ><img alt='ok' src='http://www.blueprintcss.org/blueprint/plugins/buttons/icons/cross.png' /> ";
print a({-href=>"logout.cgi"}),"Logout</button></center><br><br><br>";
print "</center>","<br>";	
&printtail;	




sub printheader {

  print header(), 
  	start_html(-title => 'Requests for you', 
 -style => { 
 -src=>['http://www.blueprintcss.org/blueprint/screen.css','http://www.blueprintcss.org/blueprint/plugins/buttons/screen.css','/cgi-bin/myapp/myprint.css']
 }), 
  
	hr;
}




sub printtail {

	print "</a>";
  print address("ntalatam\@nisum.com"),
  	end_html(); 
}





sub printcontent {


			my $un=param("un");
			# connect to the database
			my $dbh = DBI->connect("DBI:mysql:database=padmini1132;host=localhost;port=3306", "root", "padmini") 
			or die $DBI::errstr;
			my $query1="SELECT skills FROM users where username='".$un."'";
			#print $query1;
			my $sth = $dbh->prepare($query1);
			$sth->execute();
			my $skill = $sth->fetchrow_array;
			#print $skill;
			#print param("un");
			my $query2="select * from requests where language='".$skill."'";
			#print $query2;
			my $sth2 = $dbh->prepare($query2);
			$sth2->execute();
			print "<h4>There are ".$sth2->rows." requests that need your attention","<br><br>";
			print "<ul>";
			print "<table align=50%>\n";
				print "  <tr>\n";
				print "    <th>Requested by</td>\n";
				print "    <th align=center>Title</td>\n";
				print "    <th>Description</td>\n";
				print "    <th>Language</td>\n";
				print " </tr>\n";
			while ((my $name, my $title, my $description, my $language) = $sth2->fetchrow_array)
			{	
				print "  <tr>";
				print "    <td>$name</td>";
				print "    <td>$title</td>";
				print "    <td>$description</td>";
				print "    <td>$language</td>";
				print " </tr>\n";
			}
			print "</table>\n";			
			print "</ul>";
			
			$dbh->disconnect;
			


}
