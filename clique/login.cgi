#!/perl/bin/perl -T
use CGI;
use DBI;
use strict;
use warnings;
use CGI::Session;

my $session = new CGI::Session("driver:File", undef, {Directory=>'/tmp'});

# getting the effective session id:
  my $CGISESSID = $session->id();

# storing data in the session
$session->param('username', "username");
# or
$session->param(-name=>'password', -value=>"password");

# retrieving data
my $username = $session->param("username");
my $password = $session->param("password");

# connect to the database
my $dbh = DBI->connect("DBI:mysql:database=padmini1132;host=localhost;port=3306", "root", "padmini") 
  or die $DBI::errstr;

# check the username and password in the database
my $statement = qq{SELECT id FROM users WHERE username=? and password=?};
my $sth = $dbh->prepare($statement)
  or die $dbh->errstr;
$sth->execute($username, $password)
  or die $sth->errstr;
my ($userID) = $sth->fetchrow_array;

# create a JSON string according to the database result
my $json = ($userID) ? 
  qq{{"success" : "login is successful", "userid" : "$userID"}} : 
  qq{{"error" : "username or password is wrong"}};

# return JSON string
print $session->header(-type => "application/json", -charset => "utf-8");
#print $json;
