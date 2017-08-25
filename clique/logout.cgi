#!/perl/bin/perl -T
use CGI;
use strict;
use warnings;

print <<END;
Content-type: text/html

<html>
<body>
<h4> You have logged out. Click here to <a href ="/login.html">Login </a>again.</h4>
</body>
</html>
END
