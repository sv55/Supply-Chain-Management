var xmlhttp = new XMLHttpRequest();

function sendRequest() {
	var qs = "";
	qs += "/deliveryQuery?";
    var allElements = document.getElementsByTagName("*");
    for(var i = 0; i < allElements.length; ++i) {
        if(allElements[i].type == "number") {
            qs += (allElements[i].id + "=" + allElements[i].value + "&");
        }
    }
	
	if (xmlhttp.readyState == 4 || xmlhttp.readyState == 0) {
		xmlhttp.open("GET", qs, true);
		xmlhttp.onreadystatechange = handleResponse;
		xmlhttp.send(null);
	}
}

function addResultsBar() {
    var resultDiv = document.getElementById("rdd");
    var titleDiv = document.createElement("nav");
    titleDiv.setAttribute("id", "resultBar");
    titleDiv.setAttribute("class", "deep-orange z-depth-1");
    resultDiv.appendChild(titleDiv);

    var ulDiv = document.createElement("ul");
    ulDiv.setAttribute("class", "hide-on-med-and-down");
    titleDiv.appendChild(ulDiv);

    var liDiv = document.createElement("li");
    liDiv.setAttribute("class", "left");
    liDiv.innerHTML = "&nbsp;&nbsp;Results";
    ulDiv.appendChild(liDiv);
}

function resetData() {
    window.location.href = "/deliveryPage";
}

function handleResponse() {
	var resultDiv = document.getElementById("resultDiv");
    if(document.getElementById("resultBar") == undefined) {
        addResultsBar();
    }
	jsonresponse = JSON.parse(xmlhttp.responseText);

    var rTable = document.getElementById("rtable");
    var r1 = rTable.insertRow(0);
    var r2 = rTable.insertRow(1);

    var esDiv = document.createElement("div");
    esDiv.setAttribute("class", "card-panel z-depth-2");
    esDiv.setAttribute("id", "es");
    esDiv.innerHTML = "<font color='deep-orange'><h5><u>Jobsite</u></h5></font>" +
                        "<br><i>Surplus Costs</i> = " + jsonresponse["jq"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["jdc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["jidc"];
    var rDiv = resultDiv.children;
    var rDivLen = resultDiv.children.length;
    var add = "true"
    if(document.getElementById("es") == undefined) {
        r1.insertCell(0).appendChild(esDiv);
    }

    var mesDiv = document.createElement("div");
    mesDiv.setAttribute("class", "card-panel z-depth-2");
    mesDiv.setAttribute("id", "mes");
    mesDiv.innerHTML = "<font color='deep-orange'><h5><u>Warehouse</u></h5></font>" +
                        "<br><i>Surplus Costs</i> = " + jsonresponse["wq"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["wdc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["widc"];
    if(document.getElementById("mes") == undefined) {
        r1.insertCell(1).appendChild(mesDiv);
    }

    var lesDiv = document.createElement("div");
    lesDiv.setAttribute("class", "card-panel z-depth-2");
    lesDiv.setAttribute("id", "les");
    lesDiv.innerHTML = "<font color='deep-orange'><h5><u>Sub Contractor</u></h5></font>" +
                        "<br><i>Surplus Costs</i> = " + jsonresponse["sq"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["sdc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["sidc"];
    if(document.getElementById("les") == undefined) {
        r2.insertCell(0).appendChild(lesDiv);
    }

    window.scrollTo(0, document.body.scrollHeight);
}