var f = document.getElementById('mid').value.toLowerCase();

function validate() 
{
    if (f.endsWith('.mid') || f.endsWith('.midi')) 
    {
        alert(Uploaded)
    }

    else 
    {
        alert("Please upload midi file !")
    }

}

function flash()
{   
    if (f.endsWith('.mid') || f.endsWith('.midi')) 
    {
        alert("Generating Music")
    }

    else 
    {
        alert("Error !")

    }
}