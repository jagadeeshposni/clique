#!/perl/bin/perl

use CGI qw(:standard);				# Include standard HTML and CGI functions
use CGI::Carp qw(fatalsToBrowser);      	# Send error messages to browser
use DBI;

&printheader;
if (param()) { 
	
	
		}
&printcontent;
print "<button class='button negative' ><img alt='ok' src='http://www.blueprintcss.org/blueprint/plugins/buttons/icons/cross.png' /> ";
print a({-href=>"logout.cgi"});
print "Logout</button><br><br><br>";
#print "</center>","<br>";		
&printtail;	




sub printheader {

  print header(), 
  	start_html(-title => 'Landing Page', 
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
					start_form();
					print "<b><h2>Welcome to Clique...</h2></b>";
					print '<fieldset><legend>';
					print label("Hello ".param("un"));
					print '</legend>';
	#my $un=param("un");
					my $un=param("un");
					#print $un;
					my $url='/cgi-bin/myapp/view_requests.cgi?un=';
					$url=$url.$un;
					print '<center>';
					print b(a{-href=>$url},"Requisitions");print ' <br><br> ';
					print b(a{-href=>'/cgi-bin/myapp/create_req.cgi'},"Post a Request");
					end_form();
					print '</center></fieldset>';
  }
