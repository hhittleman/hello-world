var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  //Get user-enetered password from input box
  var pw = document.getElementById("pw").value.toLowerCase();
  //create strong password variable
  var isStrongPw = true;

  //compare if pw = in dictionary
  for (var i = 0; i < wordsList.length; i++) {

    //change strong password variable 
    if (wordsList[i] == pw) {
      isStrongPw = false;
      //break to exit out of the for loop
      break;
    }
  }

  //use strong password variable to announce if password is strong or weak
  if (isStrongPw == true) {
    alert("your password is strong");

  } else {
    alert("your password is weak");


  }


}
