


setTimeout(showstatus, 4000);
function showstatus() {
  document.getElementById('alerts').style.display = "block";
  document.getElementById('status').style.display = "none";
}

$(document).ready(function () {
  $('#btn').click(function () {
    $('#search').toggle(500)
  })
})

function validate() {
  let fname = document.forms["form"]["fname"].value;
  let lname = document.forms["form"]["lname"].value;
  let email = document.forms["form"]["email"].value;
  if (fname == "" || lname == "" || email == "") {
    alert("Name must be filled out");
    return false;
  }
  else {
    window.location.href = "/formsubmition.html";
    return false;
  }
}






