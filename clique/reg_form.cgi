#!/perl/bin/perl

use CGI qw(:standard);				# Include standard HTML and CGI functions
use CGI::Carp qw(fatalsToBrowser);      	# Send error messages to browser

my $js = q~function test_func(){ 
var x=document.getElementById("username").value;
if (x==null || x=="")
  {
  alert("Username must be filled out");
  return false;
  }
var password=document.getElementById("password").value;
if(password==null||password=="")
{
	alert("Please provide your password");
	return false;
}

var password2=document.getElementById("password2").value;
if(password2==null||password2=="")
{
	alert("You need to enter the password twice");
	return false;
}


if(password!=password2)
{
	alert("Passwords should match");
	return false;	
}


 
if(!document.getElementById("lang1").checked){
if(!document.getElementById("lang2").checked){
if(!document.getElementById("lang3").checked){
if(!document.getElementById("lang4").checked){
{
alert("Please provide your skill set");
return false;
}}}}}


var description =document.getElementById("description").value;
if(description==null||description=="")
{
	alert("Please say something about yourself");
	return false;
}

}~;
&printheader;
if (param()) { 
	&displayorder
		}
&printform;	
&printtail;	




sub printheader {

  print header(), 
  	start_html(-title => 'Registration Page', 
 -style => { 
 -src=>['http://www.blueprintcss.org/blueprint/screen.css','http://www.blueprintcss.org/blueprint/plugins/buttons/screen.css','/cgi-bin/myapp/myprint.css']
 },-script=>{-code=>$js}), 
  
	hr;
}




sub printtail {

	print "<button class='button positive' onclick='javascript:history.back()'>
             <img alt='ok' src='http://www.blueprintcss.org/blueprint/plugins/buttons/icons/key.png' /> 
             Go back
            </button><br><br><br>";
    print address("ntalatam\@nisum.com"),
  	end_html(); 
}




sub printform {

  

	print qq!
	<form method="post" name="form1" action="registration_success.cgi" onSubmit="return test_func()">
	
    <div id="center" class="container">
      <fieldset>
        <legend>Brief yourself to Register \!</legend>

			<label>Preferred Username</label><br>
			<input type="text" id="username" name="username" size="30" class="text"/></br>
            <label>Preferred password</label>
            <br />
            <input type="password" id="password" name="password" class="text" size="30" />
			<br/>
			<label>Preferred password again</label>
            <br />
            <input type="password" id="password2" name="password2" class="text" size="30" />
			<br/>
			
			<label>Skillset</label><br>
			<input type="radio" id="lang1" name="language" value="c"/>C<br>
			<input type="radio" id="lang2" name="language" value="java"/>Java<br>
			<input type="radio" id="lang3" name="language" value="cgi"/>CGI<br>
			<input type="radio" id="lang4" name="language" value="html"/>HTML <br>
			<label>How do you rate yourself in the above skillset ?</label>
			<select name="rating">
				<option value="excellent">Excellent</option>
				<option value="good">Good</option>
				<option value="average">Average</option>
				<option value="poor">Poor</option>
			</select><br>
			<label>Something about yourself....</label>
			<br/>
			<textarea rows="4" cols="50" name="description" id="description"></textarea>
			<br/>
          <p>
            <button type="submit">
             <img alt="ok" src="http://www.blueprintcss.org/blueprint/plugins/buttons/icons/tick.png" /> 
             Register \!
            </button>
          </p>

      </fieldset>

  </div>
	
</form>!

}
