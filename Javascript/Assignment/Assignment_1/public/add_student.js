import { validation } from './validation.js';

export function add_student(e,student)
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
			document.getElementById("name").value=""
			document.getElementById("maths_marks").value=""
			document.getElementById("science_marks").value=""

			temp_student={name,maths_marks,science_marks,total}
			//temp_student={"name":name,"maths_marks":maths_marks,"science_marks":science_marks,"total":total}
			return temp_student;
		
		
		}
		else
		{
			let error = "All three fields are required and Name must be in letters and Marks Must be in range of 0 and 50"
			document.getElementById("error-msg").innerHTML="<h3>"+error+"</h3>"
			return null;
		}

	
		
	}

window.add_student=add_student;