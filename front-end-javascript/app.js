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

const triviaToHTML = (category, question, answer) => {
    return `
    <h3>${category}</h3>
    <details>
        <summary>${question}</summary>
        ${answer}
    </details>
    `
}

const div = document.querySelector('#trivia');

// hit url, get response
const url = 'https://jservice.xyz/api/random-clue?valie=true'
const response = await fetch(url); // without await, this is a Promise; with await, Promise will resolve to Response
console.log({response});


if (response.ok) {
    // turn response into json (get json from response)
    const data = await response.json(); // without await, this is a Promise; with await, Promise will resolve to Response
    console.log({data});

    // parse json and get question, answer, category
    const category = data.category.title;
    // const question = data.question;
    // const answer = data.answer;
    const {question, answer} = data; // destructuring (data is object, getting those properties)

    const trivia = triviaToHTML(category, question, answer);
    div.innerHTML = trivia;
} else {
    div.innerHTML = "Something went wrong, please come back later";
}
