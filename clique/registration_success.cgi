#!/perl/bin/perl
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;
use DBI; 

print header;
print start_html("Congrats");
print h2("You have been successfully registered");
#print label("Note:Use your first name as username");
my $db="padmini1132";     
my $host="localhost";     
my $userid="root";     
my $passwd="padmini";     
my $connectionInfo="dbi:mysql:$db;$host"; 
my $username = param('username');    
my $password = param('password');     
my $skills = param('language');     
my $rating = param('rating');     
my $about= param('description');
#print $name;
my %form;
foreach my $p (param()) {
    $form{$p} = param($p);
    print "$p = $form{$p}<br>\n";
}
# connect to database    
my $dbh = DBI->connect($connectionInfo,$userid,$passwd); 
# prepare and execute query    
my $query = "INSERT INTO users (username,password,skills,rating,about) VALUES(\"$username\",\"$password\",\"$skills\",\"$rating\",\"$about\");";     
my $sth = $dbh->prepare($query) || die "Could not prepare SQL statement ... maybe invalid?";     
$sth->execute() || die "Could not execute SQL statement ... maybe invalid?";
#print $name;
print br;
print a({-href=>"/login.html"}, "You can Login now");

print end_html;