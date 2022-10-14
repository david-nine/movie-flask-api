function getMovieInfow() {
    return fetch('http://localhost:5000/movies').then(movieInfo => {
        return movieInfo.json().then(json => {
            console.log(json);
        })
    })
}

function getMovieInfo() {
    $.ajax({
        url: `http://localhost:5000/movies`,
        contentType: 'application/json',
        headers: {'Content-Type': 'application/json'},
        dataType: 'json',
        method: 'GET',
        success: function (data) {
            console.log(data);
            buildCard()
        }
    })
}

async function buildCard() {
    for (let i = 0; i < 10; i++) {
        $("#movie-list").append(getCardStructure(i) + '<br>');
        $("#movie-list").append('<br>');
        $(`.card-title-${i}`).text();
        $(`.card-img-${i}`).attr("src", ``);
        $(`.card-text-${i}`).text();
        $(`.temp-${i}`).text('Temperatura: ');
        $(`.max-temp-${i}`).text('Máxima: ');
        $(`.min-temp-${i}`).text('Mínima: ');
    }
}

function addInfor() {
    $("#movie-list").append("<H1>AAAA</H1>");
}

function getCardStructure(classCode) {
    return `<div class="card" style="width: 18rem;">`
        + `<img class="card-img-top card-img-${classCode}" alt="Movie Banner">`
        + `<div class="card-body">`
        + `<h5 class="card-title card-title-${classCode}"></h5>`
        + `<p class="card-text card-text-${classCode}"></p>`
        + `</div>`
        + `<ul class="list-group list-group-flush">`
        + `<li class="list-group-item list-group-rat-${classCode}"></li>`
        + `<li class="list-group-item list-group-dur-${classCode}"></li>`
        + `<li class="list-group-item list-group-dat-${classCode}"></li>`
        + `</ul>`
        + `</div>`
}

document.getElementById('movie-list').addEventListener('click', getMovieInfo)