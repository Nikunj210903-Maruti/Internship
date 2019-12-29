import { add_student } from './add_student.js'
import { submit_student } from './submit_student.js'

let student=[]	

let student_add=(e)=>
{
	let temp_student=add_student(e)
	if(temp_student)
	{
		student=[...student,temp_student]
		//student.push(temp_student)
	
	}
}

let student_submit=(e)=>
{
	let temp_student=submit_student(e)
	if(temp_student)
	{
		student=[...student,temp_student]
		//student.push(temp_student)
		console.log("Student Detail : ")
		console.table(student)
	}
}

window.student_add=student_add
window.student_submit=student_submit