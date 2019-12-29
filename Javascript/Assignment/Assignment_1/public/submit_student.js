import {validation} from './validation.js';

export function submit_student(e)
	{
		
		e.preventDefault();

		let temp_student;
		let name=document.getElementById("name").value
		let maths_marks=parseInt(document.getElementById("maths_marks").value)
		let science_marks=parseInt(document.getElementById("science_marks").value)
		let total=maths_marks+science_marks


		if (validation(name,maths_marks,science_marks))
		{

			document.getElementById("error-msg").innerHTML=""
			let temp_student={name,maths_marks,science_marks,total}
			//temp_student={"name":name,"maths_marks":maths_marks,"science_marks":science_marks,"total":total}
			

			document.getElementById("data").innerHTML="<h3>You entered data successfully , to see data in tabular form please go to your console window in browser</h3>"
			return temp_student;

			
		}
		else
		{
			let error = "All three fields are required and Name must be in letters and Marks Must be in range of 0 and 50"
			document.getElementById("error-msg").innerHTML="<h3>"+error+"</h3>"
			return null;
		}
		
		
	}

window.submit_student=submit_student;
