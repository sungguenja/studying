function startAjax() {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() { // 요청에 대한 콜백
	if (xhr.readyState === xhr.DONE) { // 요청이 완료되면
    		if (xhr.status === 200 || xhr.status === 201) {
      			console.log(xhr.responseText);
				alignAjax(xhr.responseText)
    		} else {
      			console.error(xhr.responseText);
    		}
  		}
	};
	xhr.open('GET','http://localhost:8080/projectB/todos')
	xhr.send()
};

function alignAjax(data) {
	var TodoCell = document.getElementById("Todo");
	var DoneCell = document.getElementById("Done");
	var DoingCell = document.getElementById("Doing");
	var innerdata = JSON.parse(data)
	console.log(innerdata)
	for(var i=innerdata.length-1; i>=0; i--) {
		var cell = document.createElement("div")
		var title = document.createElement("h3")
		title.innerText = innerdata[i].title
		cell.appendChild(title)
		var text = document.createElement('p')
		text.innerText = `등록날짜:${innerdata[i].regDate},${innerdata[i].name},우선순위 ${innerdata[i].sequence}`
		cell.appendChild(text)
		cell.className = "todo-cell";
		if(innerdata[i].type === "TODO") {
			var button = document.createElement('button')
			button.innerText = '->'
			button.dataset.code = innerdata[i].todoId
			button.dataset.ttype = innerdata[i].type
			button.addEventListener('click',function() {
				buttonEvent(event.target.dataset.code,event.target.dataset.ttype)
			})
			cell.appendChild(button)
			TodoCell.appendChild(cell)
		} else if(innerdata[i].type === "DOING") {
			var button = document.createElement('button')
			button.innerText = '->'
			button.dataset.code = innerdata[i].todoId
			button.dataset.ttype = innerdata[i].type
			button.addEventListener('click',function() {
				buttonEvent(event.target.dataset.code,event.target.dataset.ttype)
			})
			cell.appendChild(button)
			DoingCell.appendChild(cell)
		} else if(innerdata[i].type === "DONE") {
			console.log(DoneCell)
			DoneCell.appendChild(cell)
		}
	}
};

function buttonEvent(id,type){
	console.log(id,type)
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() { // 요청에 대한 콜백
	if (xhr.readyState === xhr.DONE) { // 요청이 완료되면
	    if (xhr.status === 200 || xhr.status === 201) {
	      	console.log(xhr.responseText);
	    } else {
	      	console.error(xhr.responseText);
	    }
	  }
	};
	xhr.open('PUT',`http://localhost:8080/projectB/todos?todoId=${id}&type=${type}`)
	xhr.send()
	location.reload()
}

setTimeout(startAjax())