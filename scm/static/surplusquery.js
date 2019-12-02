var xmlhttp = new XMLHttpRequest();

function sendRequest() {
	var qs = "";
	qs += "/surplusQuery?";
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
    titleDiv.setAttribute("class", "green z-depth-1");
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
    window.location.href = "/surplusPage";
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
    esDiv.innerHTML = "<i>Surplus Quantity</i> = " + jsonresponse["sq"] +
                        "<br><i>Inventory Costs</i> = " + jsonresponse["ic"] +
                        "<br><i>Projected Shortages</i> = " + jsonresponse["sh"] +
                        "<br><i>Rejection Cost</i> = " + jsonresponse["rc"] +
                        "<br><i>Unavailability Cost</i> = " + jsonresponse["uc"];
    var rDiv = resultDiv.children;
    var rDivLen = resultDiv.children.length;
    var add = "true"
    if(document.getElementById("es") == undefined) {
        r1.insertCell(0).appendChild(esDiv);
    }

    window.scrollTo(0, document.body.scrollHeight);
}