// alert('it is working')
// https://jservice.xyz/api/random-clue?valie=true

// const div = document.querySelector('div#trivia');
// const question = `
// <h3>Category</h3>
// <details>
//     <summary>Question that I will ask you</summary>
// This is the answer, which will be hidden.
// </details>`; //backticks go-to for JS strings, can use to interpolate
// // console.log(div); //will give ALL properties of div; don't log all the time, will slow down page
// // console.log({div}); //will make variable key and output value
// // console.log(div.innerHTML); //property with string value of Loading...
// // div.innerHTML = "Hello, class!"; //using JS to manipulate the DOM
// // console.log(div.innerHTML);
// div.innerHTML = question;

const triviaToHTML = (clue) => {
    const div = document.querySelector('#trivia');
    const answer = div.answer
    const question = div.question
    const category = div.category.title

    const html = `
    <h3>${category}</h3>
    <details>
        <summary>${question}</summary>
        ${answer}
    </details>
    `

    div.innerHTML = html;
}

const fetchAndParse = async (url, fetchOptions={}) => {
    // hit url, get response
    let response = await fetch(url, fetchOptions); // without await, this is a Promise; with await, Promise will resolve to Response
    if (response.ok) {
        let data = await response.json();
        return data;
    }
    else {
        console.error("Something went wrong, please come back later");
    }
}

// const div = document.querySelector('#trivia');

// hit url, get response
let data = await fetchAndParse('https://jservice.xyz/api/random-clue?valie=true');
createClueHtml(data);


// let url = 'https://jservice.xyz/api/random-clue?valie=true'
// let response = await fetch(url); // without await, this is a Promise; with await, Promise will resolve to Response
// // console.log({response});


// turn response into json (get json from response)
// const data = await response.json(); // without await, this is a Promise; with await, Promise will resolve to Response
// console.log({data});

// // parse json and get question, answer, category
// const category = data.category.title;
// // const question = data.question;
// // const answer = data.answer;
// const {question, answer} = data; // destructuring (data is object, getting those properties)

// const trivia = triviaToHTML(category, question, answer);
// const trivia = triviaToHTML(data);
// div.innerHTML = trivia;

// url = 'https://jservice.xyz/api/categories'
// response = await fetch(url);
data = await fetchAndParse('https://jservice.xyz/api/categories');
// const categories = data.categories;
// const {categories} = data;

const selectTag = document.querySelector('#categoryId');

for (const category of categories.slice(0,100)) {
    const option = document.createElement('option');
    option.value = category.id;
    option.innerHTML = category.id;
    selectTag.appendChild(option);
}

const form = document.querySelector('form');
form.addEventListener('submit', async (event) => {
    event.preventDefault(); // stops browser from sending form
    // get all values from user submission
    const formData = new FormData(form);
    const clueFromUser = Object.fromEntries(formData);

    // console.log({clueFromUser});

    // prepare data to submit to api
    const url = 'https://jservice.xyz/api/clues';
    const body = JSON.stringify(clueFromUser);
    const fetchOptions = {
        method: 'POST',
        body, // just like body: body ... js figures it out
        headers: {
            'Content-Type': 'application/json',
        }
    }

    const clueFromApi = await fetchAndParse(url, fetchOptions);
    createClueHtml = triviaToHTML(clueFromApi);
    // const answer = clueFromApi.answer
    // const question = clueFromApi.question
    // const category = clueFromApi.category.title
    // console.log(clueFromApi);
});
