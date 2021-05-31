var today = new Date()
var  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

var day = today.getDate()
const permm = today.getMonth() + 1
const peryyyy = today.getFullYear();
var mm = today.getMonth() + 1
var yyyy = today.getFullYear();
var month = today.toLocaleString('default', { month: 'long' })

var ul = document.getElementById("dayscontain")
var curpage = 0
var numdays;
var home = true
var getDaysInMonth = function(month,year) {
    // Here January is 1 based
    //Day 0 is the last day in the previous month
   return new Date(year, month, 0).getDate()
  // Here January is 0 based
  // return new Date(year, month+1, 0).getDate();
  };




function buildmonth(change){

    numdays = getDaysInMonth(mm+change, yyyy)

    for (i=1; i <= numdays; i++){

        var li = document.createElement('li');
        var a = document.createElement('a');
        var linkText = document.createTextNode(i);
    
    
        a.appendChild(linkText);
        a.href = "/htmldays/"+mm+"-"+i+"-"+yyyy+".php";
        a.type = "submit"
        a.id = mm+"-"+i+"-"+yyyy
        console.log(a.id)
        

        document.body.appendChild(a);
    
    
        li.appendChild(a)
        ul.appendChild(li)
    
        if (i === day && home === true){
            li.id = "active"
            changeclass()
        }
    }
}



function start(){
    document.getElementById("monthstr").innerText = month
    document.getElementById("yearstr").innerText = yyyy
    dayscontain = document.getElementById("dayscontain")
    buildmonth(curpage)
}
function changeclass(){
    document.getElementById('active').className = "active";
    
}
function changemontgeneral(){
    if (mm+curpage === 13){
        curpage = 0
        yyyy++
        document.getElementById("yearstr").innerText = yyyy
        mm = 1


    }
    if (mm+curpage === 0){
        curpage = 0
        yyyy--
        document.getElementById("yearstr").innerText = yyyy
        mm = 12
    }
    document.getElementById("monthstr").innerText = months[mm+curpage-1]
    }
    





function dethome() {
    if (mm+curpage === permm && yyyy === peryyyy){
        home = true
    }
    else{
        home = false
    }
}
function changemonthinc(){
    curpage++
    dethome()
    removeAllChildNodes(ul)
    changemontgeneral()
    buildmonth(curpage)
   
}

function changemonthdec(){
    curpage--
    dethome()
    removeAllChildNodes(ul)
    changemontgeneral()
    buildmonth(curpage)
}
function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}
window.onload = start