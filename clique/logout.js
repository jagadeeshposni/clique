function logout() {
window.location="cgi-bin/myapp/logout.cgi";
}

function Back(){
history.go(-1);
}


while (my @row = $sth2->fetchrow_array ) {
			print "</h4><li>@row\n";
				}
			print "</ul>";
			
			
			
			print "<table>\n";
			while ((my $name, my $title, my $description, my $language) = $sth2->fetchrow_array)
			{
				print "  <tr>\n";
				print "    <td>$name</td>\n";
				print "    <td>$title</td>\n";
				print "    <td>$description</td>\n";
				print "    <td>$language</td>\n";
				print " </tr>\n";
			}
			print "</table>\n";
			