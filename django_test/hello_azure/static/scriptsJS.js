let variable = true;
function changeCtoF() 
{
    variable = !variable;
    if(variable)
    {
        let a = document.getElementsByClassName('val');
        for(let i=0;i<=a.length;i++)
        {
            let v = a[i].innerHTML;
            let pV = parseFloat(v);
            let cV = pV-273.15;
            a[i].innerText = String(cV.toFixed(1));
        }
        document.getElementById("info").innerHTML="Currently showing temperature in Kelvin";
    }
    else
    {
        let a = document.getElementsByClassName('val');    
        for(let i=0;i<=a.length;i++)
        {
            let v = a[i].innerHTML;
            let pV = parseFloat(v);
            let cV = pV+273.15;
            a[i].innerText = String(cV.toFixed(2));
        }
        document.getElementById("info").innerHTML="Currently showing temperature in Celcius";
    }
}  
function changeTheme(e) 
{
    if(document.body.style.backgroundColor == 'lightcyan')
    {
        document.body.style.backgroundColor='rgb(44,44,44)';
        document.body.style.color='rgb(190, 58, 31)';
        let a = document.getElementsByClassName('res');
        for(let i=0;i<=a.length;i++)
        {
            a[i].style.borderColor='white';
        }
        document.getElementById('f').style.borderColor='white';
    }
    else
    {
        document.body.style.backgroundColor='lightcyan';
        document.body.style.color='black';
        let a = document.getElementsByClassName('res');
        for(let i=0;i<=a.length;i++)
        {
            a[i].style.borderColor='black';
        }
        document.getElementById('f').style.borderColor='black';
    }
}