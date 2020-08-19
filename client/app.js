// function onPageLoad()
// {

// }


function get_mid()
{
}

function validate()
{
    var f = document.getElementById('mid').value.toLowerCase();

    if(!f || f=="")
    {
        alert("File cannot be empty !")
    }

    else if (!f.endsWith('.mid') && !f.endsWith('.midi')) 
    {
        alert('Please upload midi file only.');
        return false;
    }

    else
    {
        alert("Uploaded !")
        get_mid()
    }

       
}


// window.onload=onPageLoad