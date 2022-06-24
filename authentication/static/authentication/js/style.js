const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const firstForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const container = document.querySelector(".container");
let formSignInBtn = document.getElementById("signinBtn");
let formSignUpBtn = document.getElementById("signupBtn");
let emailSignUp = document.getElementById("email1");
let emailSignIn = document.getElementById("email2");
let passwordNode = document.getElementById("password");
let confirmPasswordNode = document.getElementById("confirm_password");

emailSignUp.addEventListener("keyup", checkEmail);

formSignUpBtn.disabled = true;


function checkEmail(event){
    let email = emailSignUp;
    if(email.value.includes("@") && email.value.includes(".")){
        console.log(true);
        email.style.border = "none";
        formSignUpBtn.disabled = false;
    }
    else{
        email.style.border = "2px solid rgb(233, 145, 145)";
    }
}


confirmPasswordNode.addEventListener("keyup", checkPassword);

passwordNode.addEventListener("keyup", checkStreangth)

function checkStreangth(e){
    if(e.target.value.length <= 5){
        e.target.style.border = "2px solid red";
    }
    else{
        e.target.style.border = "none";
    }
}

function checkPassword(e){
    if(confirmPasswordNode.value != password.value){
        confirmPasswordNode.style.border = "2px solid red";
    }
    else{
        confirmPasswordNode.style.border = "none";
    }
}


formSignInBtn.addEventListener("click", submitForm)
formSignUpBtn.addEventListener("click", submitForm)


function submitForm(e){
    console.log(e.target.value);
    if(e.target.value !== "log in"){
        checkEmail();
        checkPassword();
    }
    e.target.parentNode.submit();
}

signInBtn.addEventListener("click", () => {
	container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
	container.classList.add("right-panel-active");
});

firstForm.addEventListener("submit", (e) => e.preventDefault());
secondForm.addEventListener("submit", (e) => e.preventDefault());
