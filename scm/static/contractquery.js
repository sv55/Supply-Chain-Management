var xmlhttp = new XMLHttpRequest();

function sendRequest() {
	var qs = "";
	qs += "/contractQuery?";
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
    titleDiv.setAttribute("class", "deep-purple z-depth-1");
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
    window.location.href = "/contractPage";
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
    esDiv.innerHTML = "<font color='purple'><h5><u>Local Supplier</u></h5></font><i>Project Shortages</i> = " + jsonresponse["ls"] +
                        "<br><i>Project Shortages Cost</i> = " + jsonresponse["lsc"] +
                        "<br><i>Quantity of Material</i> = " + jsonresponse["lq"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["ldc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["lic"] +
                        "<br><i>Quality of Supplier performance</i> = " + jsonresponse["lp"];
    var rDiv = resultDiv.children;
    var rDivLen = resultDiv.children.length;
    var add = "true"
    if(document.getElementById("es") == undefined) {
        r1.insertCell(0).appendChild(esDiv);
    }

    var mesDiv = document.createElement("div");
    mesDiv.setAttribute("class", "card-panel z-depth-2");
    mesDiv.setAttribute("id", "mes");
    mesDiv.innerHTML = "<font color='purple'><h5><u>Non Local Supplier</u></h5></font><i>Project Shortages</i> = " + jsonresponse["ns"] +
                        "<br><i>Project Shortages Cost</i> = " + jsonresponse["nsc"] +
                        "<br><i>Quantity of Material</i> = " + jsonresponse["nq"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["ndc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["nic"] +
                        "<br><i>Quality of Supplier performance</i> = " + jsonresponse["np"];
    if(document.getElementById("mes") == undefined) {
        r1.insertCell(1).appendChild(mesDiv);
    }

    var lesDiv = document.createElement("div");
    lesDiv.setAttribute("class", "card-panel z-depth-2");
    lesDiv.setAttribute("id", "les");
    lesDiv.innerHTML = "<font color='purple'><h5><u>Vendor Managed Inventory</u></h5></font><i>Project Shortages</i> = " + jsonresponse["vs"] +
                        "<br><i>Project Shortages Cost</i> = " + jsonresponse["vsc"] +
                        "<br><i>Quantity of Material</i> = " + jsonresponse["vq"] +
                        "<br><i>Direct Costs</i> = " + jsonresponse["vdc"] +
                        "<br><i>Indirect Costs</i> = " + jsonresponse["vic"] +
                        "<br><i>Quality of Supplier performance</i> = " + jsonresponse["vp"];
    if(document.getElementById("les") == undefined) {
        r2.insertCell(0).appendChild(lesDiv);
    }

    window.scrollTo(0, document.body.scrollHeight);
}