let errorMessage1 = document.getElementById('errorMessage1');
let email1 = document.getElementById('emailform');

document.getElementById('contactform').onsubmit=function(){
  if(email1.value=="" || email1.value=="info@truegrademetals.com" || email1.value=="info@truegrademetals.com"){
    errorMessage1.innerHTML="Please input your E-mail";
    return false;
  }else if(!emailTrue.test(email1.value)){
    errorMessage1.innerHTML="Please input the right E-mail";
    return false;
  }else if(document.getElementById('titleform').value==""){
    errorMessage1.innerHTML="Please input the subject";
    return false;
  }else if(document.getElementById('contentform').value==""){
    errorMessage1.innerHTML="Please input the content";
    return false;
  }else{
    errorMessage1.innerHTML="&emsp;";
    return true;
    feedback();
  };
};