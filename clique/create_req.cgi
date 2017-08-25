#!/perl/bin/perl

use CGI qw(:standard);				
use CGI::Carp qw(fatalsToBrowser);  

my $js = q~function test_func(){ 
var x=document.getElementById("name").value;
if (x==null || x=="")
  {
  alert("Username must be filled out");
  return false;
  }
var title=document.getElementById("title").value;
if(title==null||title=="")
{
	alert("Please provide a title for your post");
	return false;
}
var description =document.getElementById("description").value;
if(description==null||description=="")
{
	alert("Please provide a description for your post");
	return false;
}
//var language =document.forms["form1"]["language"].value;
//alert(language);
if(!document.getElementById("lang1").checked){
if(!document.getElementById("lang2").checked){
if(!document.getElementById("lang3").checked){
if(!document.getElementById("lang4").checked){
{
alert("What language does the post deal with?");
return false;
}}}}}
}~;
&printheader;
&printform;	
&printtail;	




sub printheader {

  print header(), 
  	start_html(-title => 'Create a new Request', 
				-style => { 
								-src=>['http://www.blueprintcss.org/blueprint/screen.css','http://www.blueprintcss.org/blueprint/plugins/buttons/screen.css','/cgi-bin/myapp/myprint.css']
							},
 
				-script=>{-code=>$js}
		
			),  
	hr;
	
}


	
sub printtail {

	print "<center>";

#print "                          ";
print "<button class='button positive' onclick='javascript:history.back()'>
             <img alt='ok' src='http://www.blueprintcss.org/blueprint/plugins/buttons/icons/key.png' /> 
             Go back
            </button>";
#print "<a href=javascript:history.back()>Go back</a>";
print "<button class='button negative' ><img alt='ok' src='http://www.blueprintcss.org/blueprint/plugins/buttons/icons/cross.png' /> ";
print a({-href=>"logout.cgi"}),"Logout</button></center><br><br><br>";
print "</center>","<br></a>";

  print address("ntalatam\@nisum.com"),
  	end_html(); 
}




sub printform {
	
	#print '<a href="#" onMouseOver="test_func()">mouse on</a>' ;
	print qq!
	

	<form method="post" name="form1" action="request_success.cgi" onSubmit="return test_func()">
	
    <div id="center">
      <fieldset>
        <legend>Post your Question</legend>

			<label>Your Name</label></br>
			<input type="text" id="name" name="name" size="30" class="text"/></br>
            <label>Title</label>
            <br />
            <input type="text" id="title" name="title" class="text" size="30" />
			<br/>
			<label>Description</label>
			<br/>
			<textarea rows="4" cols="50" id="description" name="description"></textarea>
			<br/>
			<label>The Request deals with :</label><br>
			<input type="radio" id="lang1" name="language" value="c"/>C<br>
			<input type="radio" id="lang2" name="language" value="java"/>Java<br>
			<input type="radio" id="lang3" name="language" value="cgi"/>CGI<br>
			<input type="radio" id="lang4" name="language" value="html"/>HTML <br>
          <p>
            <button type="submit" >
             <img alt="ok" src="http://www.blueprintcss.org/blueprint/plugins/buttons/icons/tick.png" /> 
             Post Request
            </button>
          </p>
			
		  
		  
      </fieldset>

  </div>
	
</form>!
}

