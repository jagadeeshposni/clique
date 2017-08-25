#!/perl/bin/perl
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;
use DBI; 

print header;
print start_html("Thank You");
print h2("Thank You");
my $db="padmini1132";     
my $host="localhost";     
my $userid="root";     
my $passwd="padmini";     
my $connectionInfo="dbi:mysql:$db;$host"; 
my $name = param('name');    
my $title = param('title');     
my $description = param('description');     
my $language = param('language');     
#print $name;
my %form;
foreach my $p (param()) {
    $form{$p} = param($p);
    print "$p = $form{$p}<br>\n";
}
# connect to database    
my $dbh = DBI->connect($connectionInfo,$userid,$passwd); 
# prepare and execute query    
my $query = "INSERT INTO requests (name,title,description,language) VALUES(\"$name\",\"$title\",\"$description\",\"$language\");";     
my $sth = $dbh->prepare($query) || die "Could not prepare SQL statement ... maybe invalid?";     
$sth->execute() || die "Could not execute SQL statement ... maybe invalid?";
#print $name;
print br;
#print a({-href=>"logout.cgi"}, "Logout");
print br;
#print a({-href=>"landing_page.cgi"}, "Homepage");

print "<center>";

#print "                          ";
print "<button class='button positive' onclick='javascript:history.back()'>
             <img alt='ok' src='http://www.blueprintcss.org/blueprint/plugins/buttons/icons/key.png' /> ";
			 print a({-href=>"landing_page.cgi?un=".$name}), "Homepages</button>";
print "<button class='button negative' ><img alt='ok' src='http://www.blueprintcss.org/blueprint/plugins/buttons/icons/cross.png' /> ";
print a({-href=>"logout.cgi"}),"Logout</button></center><br><br><br>";
print "</center>","<br>";
print end_html;