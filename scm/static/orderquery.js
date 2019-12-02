var xmlhttp = new XMLHttpRequest();

function sendRequest() {
	var qs = "";
	qs += "/orderQuery?";
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
    titleDiv.setAttribute("class", "blue z-depth-1");
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
    window.location.href = "/orderPage";
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
    esDiv.innerHTML = "<font color='blue'><h5><u> For Estimated Quantity </u></h5></font><i>Project Shortages</i> = " + jsonresponse["ps"] +
                        "<br><i>Surplus Costs</i> = " + jsonresponse["sc"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["dc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["idc"];
    var rDiv = resultDiv.children;
    var rDivLen = resultDiv.children.length;
    var add = "true"
    if(document.getElementById("es") == undefined) {
        r1.insertCell(0).appendChild(esDiv);
    }

    var mesDiv = document.createElement("div");
    mesDiv.setAttribute("class", "card-panel z-depth-2");
    mesDiv.setAttribute("id", "mes");
    mesDiv.innerHTML = "<font color='blue'><h5><u> For More Than Estimated Quantity </u></h5></font><i>Project Shortages</i> = " + jsonresponse["mps"] +
                        "<br><i>Surplus Costs</i> = " + jsonresponse["msc"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["mdc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["midc"];
    if(document.getElementById("mes") == undefined) {
        r1.insertCell(1).appendChild(mesDiv);
    }

    var lesDiv = document.createElement("div");
    lesDiv.setAttribute("class", "card-panel z-depth-2");
    lesDiv.setAttribute("id", "les");
    lesDiv.innerHTML = "<font color='blue'><h5><u> For Less Than Estimated Quantity </u></h5></font><i>Project Shortages</i> = " + jsonresponse["lps"] +
                        "<br><i>Surplus Costs</i> = " + jsonresponse["lsc"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["ldc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["lidc"];
    if(document.getElementById("les") == undefined) {
        r2.insertCell(0).appendChild(lesDiv);
    }

    var eoqDiv = document.createElement("div");
    eoqDiv.setAttribute("class", "card-panel z-depth-2");
    eoqDiv.setAttribute("id", "eoqd");
    eoqDiv.innerHTML = "<font color='blue'><h5><u> For Economic Order Quantity </u></h5></font><i>Project Shortages</i> = " + jsonresponse["eps"] +
                        "<br><i>Surplus Costs</i> = " + jsonresponse["esc"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["edc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["eidc"];
    if(document.getElementById("eoqd") == undefined) {
        r2.insertCell(1).appendChild(eoqDiv);
    }
    window.scrollTo(0, document.body.scrollHeight);
}