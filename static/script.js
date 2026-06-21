const output =
document.getElementById("output");

async function summarizeNotes(){

    const notes =
    document.getElementById(
        "notes"
    ).value;

    output.innerText =
    "Generating...";

    const response =
    await fetch(
        "/summarize-notes",
        {
            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({
                notes
            })
        }
    );

    const data =
    await response.json();

    output.innerText =
    data.result;
}

async function summarizeYoutube(){

    const url =
    document.getElementById(
        "youtubeUrl"
    ).value;

    output.innerText =
    "Fetching transcript...";

    const response =
    await fetch(
        "/summarize-youtube",
        {
            method:"POST",

            headers:{
                "Content-Type":
                "application/json"
            },

            body:JSON.stringify({
                url
            })
        }
    );

    const data =
    await response.json();

    output.innerText =
    data.result;
}

const toggle =
document.getElementById(
    "themeToggle"
);

toggle.addEventListener(
"click",
() => {

document.body.classList.toggle(
"dark"
);

localStorage.setItem(
"theme",
document.body.classList.contains(
"dark"
)
);
}
);

if(
localStorage.getItem("theme")
=== "true"
){
document.body.classList.add(
"dark"
);
}