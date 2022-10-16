let namex = document.querySelector("#name");
let date = document.querySelector("#date");
let type = document.querySelector("#type");
let issuedby = document.querySelector("#issuedby");
let id = document.querySelector("#id");

let result = document.querySelector(".result_text");
let result_js = document.querySelector(".result_text_js");
let submit_btn = document.querySelector(".action-button");
let copy_btn = document.querySelector("#copy_btn");
let copy_btn_js = document.querySelector("#copy_btn_js");

let reload_btn = document.querySelector("#reload_btn");

var idcode = document.querySelector("#idcode")
var idencoded = document.querySelector("#idencoded");

var noti_data = document.getElementById("notification_enteralldata");
var done_page = document.getElementById("done");
var error_page = document.getElementById("error");
var create_page = document.querySelector(".card-form");
var create_page_image = document.querySelector(".card-image");

var id_decoded = "";
var id_encoded = "";

// Generates the ID
function id_gen() {
    let id_gen = Math.floor(Math.random() * (999999 - 100000 + 1) + 100000);
    id_gen = id_gen.toString()
    let id_gen_space=id_gen.match(/.{1,3}/g);
    id.value = id_gen_space.join(" ")
}

// Generates the HTML code for the verification page
function generate(namex, date, type, issuedby, id){
    let final_string = `<!DOCTYPE html>
<html>
    <head>
        <meta charset='UTF-8'>
        <meta name='robots' content='noindex'>
        <title>Zertifikat - ${id}</title>
    </head>
    <link rel="stylesheet" type="text/css" href="./assets/css/stylesheet.css">
    <body>
        <div id='infoform'>
            <div id='status'>
                <center>
                <h3>Gültiges Zertifikat</h3>
                <h3>ID: ${id}</h3>
                </center>
            </div>
            <center>
                <h3>Name</h3>
                <p>${namex}</p>
                <h3>Ausstellung</h3>
                <p>${date}</p>
                <h3>Zertifikat Typ</h3>
                <p>${type}</p>
                <h3>Ausgestellt von</h3>
                <p>${issuedby}</p>
                <a href='../index.html'><button id='back'>Zurück</button></a>
            </center>
        </div>
    </body>
</html>`;
    result.value = final_string;
    idcode.innerText = id;
}

// Generates the JS Code for the verification sytem
function generate_js(id) {
    id_decoded = id;
    id_encoded = btoa(id_decoded);
    toString(id_encoded)
    id_encoded = id_encoded.substr(4)
    
    let final_string_js = ` else if (vid_encoded == "${id_encoded}") {
            window.location.replace("./pages/${id_encoded}.html")
        }`;
    
    result_js.value = final_string_js;
    idencoded.innerText = id_encoded;

}

// Copy functions
function copy(){
    result.select();
    document.execCommand("copy");
}

function copy_js(){
    result_js.select();
    document.execCommand("copy");
}

// If BTN clicked generate the code and change the page
submit_btn.addEventListener("click", () => {
    // Check if everything is entered
    if (namex.value && type.value && issuedby.value && id.value != "") { 
        generate(namex.value, date.value, type.value, issuedby.value, id.value);
        generate_js(id.value, id_decoded.value, id_encoded.value);
        
        create_page.style = "display: none";
        create_page_image.style = "display: none";
        noti_data.style = "display: none";
        done_page.style = "display: block";
        namex.value = "";
        date.value = "";
        type.value = "";
        issuedby.value = "";
        id.value = "";
    }
    
    else {
        noti_data.style = "display: block";
    }
    
});

// If reload BTN clicked go back to creation
reload_btn.addEventListener("click", () => {
    id_gen()
    create_page.style = "display: block";
    create_page_image.style = "display: block";
    done_page.style = "display: none";
});

// Event listener for Copy BTNs
copy_btn.addEventListener("click", () => {
    copy();
})

copy_btn_js.addEventListener("click", () => {
    copy_js();
})
