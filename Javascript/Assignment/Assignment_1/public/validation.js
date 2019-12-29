export function validation(...data)
   {

    	let validated = true

    	let alphabet=/^[a-zA-Z]+$/;
		if(!(data[0].match(alphabet)))
		{
			validated=false
		}
		
		if(isNaN(data[1]) ||  data[1]<0 || data[1]>50 )
		{
			validated=false
		}

		if(isNaN(data[2]) ||  data[2]<0 || data[2]>50 )
		{
			validated=false
		}

    	return validated
    }


